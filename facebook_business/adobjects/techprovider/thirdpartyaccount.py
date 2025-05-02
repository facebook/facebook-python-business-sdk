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
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from facebook_business.adobjects.techprovider.thirdpartyaccountmanager import (
        ThirdPartyAccountManager,
    )

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.business import Business
from facebook_business.api import FacebookAdsApi


@dataclass
class ThirdPartyAccountInfo:
    account_id: str
    name: str


""" ThirdPartyAccount

These are accounts owned by a tech provider's business, representing
a user of the tech provider's application.

This class allows the tech provider to decide which assets are shared from an existing
facebook user's account/business portfolio (which the user has granted the tech provider access to),
and which assets are created and owned by the tech provider. This class allows the Tech Provider
to provide monetization experiences for the third party user using a higher level interface
than the underlying facebook graph apis.

This class simplifies:
1. Creating Assets that are owned by the tech provider (Ad Accounts, Pages, Pixels, etc) .
2. Accessing Assets from a users facebook account or business account (Pages, Pixels, etc).
3. Combining tech provider owned and user owned assets. (ex: a Product Catalog owned by the tech provider using CAPI events from a user owned dataset)
3. Allocating a portion of the tech provider's Credit Line to the account.
4. Access Token Usage and Management
5. Providing Monetization Services to the third party user

All management operations are performed using the ThirdPartyAccountManager (e.g. CRUD operations)
Creation:
- ThirdPartyAccountManager.create_account() must be used to create a new ThirdPartyAccount
Reading:
- ThirdPartyAccountManager.get_account() must be used to load a single ThirdPartyAccount
- ThirdPartyAccountManager.list_accounts() must be used to load a list of ThirdPartyAccountInfo
Deletion:
- ThirdPartyAccountManager.delete_account() must be used to delete an existing ThirdPartyAccount
"""


class ThirdPartyAccount:

    def __init__(
        self,
        account_manager: ThirdPartyAccountManager,
        account_id: str,
        account_token: Optional[str] = None,
    ):
        # The manager for this account
        self.account_manager = account_manager

        # The ID of the account
        self.account_id = account_id

        # The access token for the account
        self.account_token = account_token

    """ get_facebook_page_id

    Return the Facebook Page associated with the account.

    This is the Facebook Page that was shared with the account
    during creation. If the page was updated, this will return
    the updated page.

    Returns: Optional[str] - The Facebook Page ID or None if not found
    """

    def get_facebook_page_id(self) -> Optional[str]:
        api = self.get_api()
        try:
            business = Business(self.account_id, api=api)
            ad_accounts = business.get_owned_ad_accounts(
                fields=[AdAccount.Field.end_advertiser]
            )
            if ad_accounts:
                return ad_accounts[0].end_advertiser
        except Exception as e:
            raise e
        print(f"No Facebook page ID found for account - {self.account_id}")
        return None

    def get_api(self) -> FacebookAdsApi:
        return FacebookAdsApi.init(access_token=self.account_token)

    def refresh_access_token(self) -> None:
        self.account_token = self.account_manager.regenerate_token(self.account_id)
