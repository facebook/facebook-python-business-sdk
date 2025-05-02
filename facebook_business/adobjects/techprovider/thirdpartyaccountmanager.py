# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
from dataclasses import dataclass
from typing import List, Optional

from facebook_business import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.business import Business
from facebook_business.adobjects.extendedcredit import ExtendedCredit

from facebook_business.adobjects.techprovider.thirdpartyaccount import (
    ThirdPartyAccount,
    ThirdPartyAccountInfo,
)
from facebook_business.api import Cursor


@dataclass
class PageProps:
    id: str


@dataclass
class CreditAllocationProps:
    credit_line_id: str
    currency_amount: str
    currency: Optional[str] = "USD"

    def __post_init__(self):
        if self.currency_amount is not None and float(self.currency_amount) <= 0:
            raise ValueError("Credit allocation amount must be positive")


@dataclass
class CreateAccountInput:
    name: str
    user_access_token: str
    page: Optional[PageProps] = None
    credit_allocation: Optional[CreditAllocationProps] = None


class ThirdPartyAccountManager:

    def __init__(self, app_id, tech_provider_business_id, system_account_token):
        self.system_account_token = system_account_token
        self.tech_provider_business_id = tech_provider_business_id
        self.app_id = app_id

    def create_account(
        self, create_account_input: CreateAccountInput
    ) -> ThirdPartyAccount:
        api = FacebookAdsApi.init(
            access_token=create_account_input.user_access_token,
        )

        partner_business = Business(self.tech_provider_business_id, api=api)
        shared_page_id = None
        if (
            hasattr(create_account_input, "page")
            and create_account_input.page is not None
        ):
            shared_page_id = create_account_input.page.id

        try:
            child_business = partner_business.create_owned_business(
                params={
                    Business.Field.name: create_account_input.name,
                    "shared_page_id": shared_page_id,
                    "timezone_id": Business.TimezoneId.value_1,
                    Business.Field.vertical: Business.Vertical.other,
                    "page_permitted_tasks": [
                        Business.PagePermittedTasks.advertise,
                        Business.PagePermittedTasks.analyze,
                    ],
                }
            )
        except Exception as e:
            raise e
        print(f"Successfully created Child Business - {child_business}")

        system_api = FacebookAdsApi.init(access_token=self.system_account_token)
        if (
            hasattr(create_account_input, "credit_allocation")
            and create_account_input.credit_allocation is not None
        ):
            extended_credit = ExtendedCredit(
                create_account_input.credit_allocation.credit_line_id, api=system_api
            )
            credit_allocation = extended_credit.create_owning_credit_allocation_config(
                params={
                    "receiving_business_id": child_business["id"],
                    "amount": create_account_input.credit_allocation.currency_amount,
                }
            )
            print(f"Successfully created credit allocation - {credit_allocation}")

        child_business = Business(child_business["id"], api=system_api)

        try:
            response = child_business.create_access_token(
                params={
                    "app_id": self.app_id,
                    "scope": "ads_management,business_management",
                }
            )
        except Exception as e:
            raise e
        print("Successfully created access token")

        account_token = response["access_token"]
        api = FacebookAdsApi.init(access_token=account_token)

        child_business = Business(child_business["id"], api=api)
        extended_credit: Cursor = child_business.get_extended_credits(
            fields=[ExtendedCredit.Field.id]
        )
        funding_source_id = None
        if extended_credit:
            funding_source = extended_credit.next()
            funding_source_id = funding_source.id if funding_source else None

        currency = "USD"
        if (
            hasattr(create_account_input, "credit_allocation")
            and create_account_input.credit_allocation is not None
        ):
            currency = create_account_input.credit_allocation.currency
        try:
            ad_account = child_business.create_ad_account(
                params={
                    AdAccount.Field.name: create_account_input.name,
                    AdAccount.Field.currency: currency,
                    AdAccount.Field.end_advertiser: shared_page_id,
                    AdAccount.Field.timezone_id: Business.TimezoneId.value_1,
                    AdAccount.Field.partner: "NONE",
                    AdAccount.Field.media_agency: "NONE",
                    AdAccount.Field.funding_source: funding_source_id,
                }
            )
        except Exception as e:
            raise e
        print(f"Successfully created Ad Account - {ad_account}")

        system_users = child_business.get_system_users()
        system_user_id = system_users[0]["id"]

        try:
            ad_account.create_assigned_user(
                params={
                    "user": system_user_id,
                    "tasks": [
                        AdAccount.Tasks.advertise,
                        AdAccount.Tasks.analyze,
                        AdAccount.Tasks.manage,
                    ],
                    AdAccount.Field.business: child_business["id"],
                }
            )
        except Exception as e:
            raise e
        print(f"Successfully assigned system user - {system_user_id}")

        return ThirdPartyAccount(self, child_business["id"], account_token)

    def get_account(
        self, account_id: str, user_access_token: Optional[str] = None
    ) -> ThirdPartyAccount:
        if user_access_token is None:
            user_access_token = self.regenerate_token(account_id)
        return ThirdPartyAccount(self, account_id, user_access_token)

    def regenerate_token(self, account_id: str) -> str:
        api = FacebookAdsApi.init(access_token=self.system_account_token)
        child_business = Business(account_id, api=api)

        try:
            response = child_business.create_access_token(
                params={
                    "id": child_business["id"],
                    "app_id": self.app_id,
                    "scope": "ads_management,business_management",
                }
            )
        except Exception as e:
            raise e
        return response["access_token"]

    def delete_account(self, account_id: str) -> None:
        api = FacebookAdsApi.init(access_token=self.system_account_token)
        tech_provider_business = Business(self.tech_provider_business_id, api=api)
        try:
            tech_provider_business.delete_owned_businesses(
                params={
                    "client_id": account_id,
                }
            )
        except Exception as e:
            raise e
        print(f"Successfully deleted account - {account_id}")

    def list_accounts(self, max: int = 10) -> List[ThirdPartyAccountInfo]:
        api = FacebookAdsApi.init(access_token=self.system_account_token)
        business = Business(self.tech_provider_business_id, api=api)
        accounts = []
        owned_businesses: Cursor = business.get_owned_businesses(
            fields=[Business.Field.id, Business.Field.name], params={"limit": max}
        )
        while owned_businesses:
            accounts.extend(
                ThirdPartyAccountInfo(ob["id"], ob["name"]) for ob in owned_businesses
            )
            if not owned_businesses.load_next_page():
                break
        return accounts
