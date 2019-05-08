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

from facebook_business.adobjects import agencyclientdeclaration

class AdAccountMixin:
    class AccountStatus(object):
        active = 1
        disabled = 2
        in_grace_period = 9
        pending_closure = 100
        pending_review = 7
        temporarily_unavailable = 101
        unsettled = 3

    class AgencyClientDeclaration(agencyclientdeclaration.AgencyClientDeclaration.Field):
        pass

    class Capabilities(object):
        bulk_account = 'BULK_ACCOUNT'
        can_use_reach_and_frequency = 'CAN_USE_REACH_AND_FREQUENCY'
        direct_sales = 'DIRECT_SALES'
        view_tags = 'VIEW_TAGS'

    class TaxIdStatus(object):
        account_is_personal = 5
        offline_vat_validation_failed = 4
        unknown = 0
        vat_information_required = 3
        vat_not_required = 1

    @classmethod
    def get_my_account(cls, api=None):
        from facebook_business.adobjects.adaccountuser import AdAccountUser
        """Returns first AdAccount associated with 'me' given api instance."""
        # Setup user and read the object from the server
        me = AdAccountUser(fbid='me', api=api)

        # Get first account connected to the user
        my_account = me.edge_object(cls)

        return my_account

    def opt_out_user_from_targeting(self,
                                    schema,
                                    users,
                                    is_raw=False,
                                    app_ids=None,
                                    pre_hashed=None):
        from facebook_business.adobjects.customaudience import CustomAudience
        """Opts out users from being targeted by this ad account.

        Args:
            schema: A CustomAudience.Schema value
            users: a list of identites that follow the schema given

        Returns:
            Return FacebookResponse object
        """
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'usersofanyaudience'),
            params=CustomAudience.format_params(schema,
                                                users,
                                                is_raw,
                                                app_ids,
                                                pre_hashed),
        )
