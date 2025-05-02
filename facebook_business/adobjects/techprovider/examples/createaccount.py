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

from facebook_business.adobjects.techprovider.thirdpartyaccountmanager import (
    CreateAccountInput,
    CreditAllocationProps,
    PageProps,
    ThirdPartyAccountManager,
)

tech_provider_business_id = "<tech_provider_business_id>"
app_id = "<app_id>"
page_id = "<page_id>"
credit_line_id = "<credit_line_id>"
system_account_token = "<system_account_token>"
user_access_token = "<user_access_token>"

create_account_input = CreateAccountInput(
    name="<account_name>",
    page=PageProps(
        id=page_id,
    ),
    credit_allocation=CreditAllocationProps(
        credit_line_id=credit_line_id,
        currency_amount="<currency_amount>",
        currency="USD",
    ),
    user_access_token=user_access_token,
)

third_party_account_manager = ThirdPartyAccountManager(
    app_id, tech_provider_business_id, system_account_token
)
third_party_account = third_party_account_manager.create_account(create_account_input)
print(third_party_account)
