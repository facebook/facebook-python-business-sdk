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

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adaccountgroup import AdAccountGroup
from facebookads.adobjects.page import Page
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker

class AdAccountUserMixin:

    class Field(object):
        id = 'id'
        name = 'name'
        permissions = 'permissions'
        role = 'role'

    class Permission(object):
        account_admin = 1
        admanager_read = 2
        admanager_write = 3
        billing_read = 4
        billing_write = 5
        reports = 7

    class Role(object):
        administrator = 1001
        analyst = 1003
        manager = 1002

    @classmethod
    def get_endpoint(cls):
        return 'users'

    def get_ad_accounts(self, fields=None, params=None):
        """Returns iterator over AdAccounts associated with this user."""
        return self.iterate_edge(AdAccount, fields, params, endpoint='adaccounts')

    def get_ad_account(self, fields=None, params=None):
        """Returns first AdAccount associated with this user."""
        return self.edge_object(AdAccount, fields, params)

    def get_pages(self, fields=None, params=None):
        """Returns iterator over Pages's associated with this user."""
        return self.iterate_edge(Page, fields, params)

    def get_ad_account_groups(self, fields=None, params=None):
        """Returns iterator over AdAccount Groups associated with this user."""
        return self.iterate_edge(AdAccountGroup, fields, params)

    def create_ad_account_group(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        param_checker = TypeChecker(param_types, enums)
        request = FacebookRequest(
            api=self._api,
            node_id=self['id'],
            method='POST',
            endpoint='/adaccountgroups',
            param_checker=param_checker,
            target_class=AdAccountGroup,
            api_type='EDGE',
            allow_file_upload=False,
            response_parser=ObjectParser(
                target_class=AdAccountGroup,
            ),
        )
        if params is not None:
            request.add_params(params)
        if fields is not None:
            request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            return request.execute()
