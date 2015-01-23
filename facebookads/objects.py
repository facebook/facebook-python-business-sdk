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

"""
objects module contains classes that represent and help traverse nodes on the
Ads API.
"""

from facebookads.exceptions import FacebookBadObjectError
from facebookads.api import FacebookAdsApi
from facebookads.mixins import (
    CanArchive,
    CanValidate,
    CannotCreate,
    CannotDelete,
    CannotUpdate,
    HasObjective,
    HasStatus,
    HasBidInfo,
)

import hashlib
import collections
import json
import six


class EdgeIterator(object):

    """EdgeIterator is an iterator over an object's connections.

    Examples:
        >>> me = AdUser('me')
        >>> my_accounts = [act for act in EdgeIterator(me, AdAccount)]
        >>> my_accounts
        [<AdAccount act_abc>, <AdAccount act_xyz>]
    """

    def __init__(
        self,
        source_object,
        target_objects_class,
        fields=None,
        params=None,
    ):
        """
        Initializes an iterator over the objects to which there is an edge from
        source_object.

        Args:
            source_object: An AbstractObject instance from which to inspect an
                edge. This object should have an id.
            target_objects_class: Objects traverersed over will be initialized
                with this AbstractObject class.
            fields (optional): A list of fields of target_objects_class to
                automatically read in.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
        """
        self._params = dict(params or {})
        target_objects_class._assign_fields_to_params(fields, self._params)
        self._source_object = source_object
        self._target_objects_class = target_objects_class
        self._path = (
            source_object.get_id_assured(),
            target_objects_class.get_endpoint(),
        )
        self._queue = []
        self._finished_iteration = False
        self._total_count = None

        if self._source_object.get_api():
            self.load_next_page()

    def __repr__(self):
        return str(self._queue)

    def __len__(self):
        return len(self._queue)

    def __iter__(self):
        return self

    def __next__(self):
        # Load next page at end.
        # If load_next_page returns False, raise StopIteration exception
        if not self._queue and not self.load_next_page():
            raise StopIteration()

        return self._queue.pop(0)

    # Python 2 compatibility.
    next = __next__

    def __getitem__(self, index):
        return self._queue[index]

    def total(self):
        return self._total_count

    def load_next_page(self):
        """Queries server for more nodes and loads them into the internal queue.

        Returns:
            True if successful, else False.
        """
        if self._finished_iteration:
            return False

        self._params['summary'] = True

        response = self._source_object.get_api_assured().call(
            FacebookAdsApi.HTTP_METHOD_GET,
            self._path,
            params=self._params,
        ).json()

        if 'paging' in response and 'next' in response['paging']:
            self._path = response['paging']['next']
        else:
            # Indicate if this was the last page
            self._finished_iteration = True

        if 'summary' in response and 'total_count' in response['summary']:
            self._total_count = response['summary']['total_count']

        self._queue = self.build_objects_from_response(response)
        return len(self._queue) > 0

    def build_objects_from_response(self, response):
        if 'data' in response:
            ret = []
            for json_obj in response['data']:
                obj = self._target_objects_class()
                obj._set_data(json_obj)
                ret.append(obj)
        else:
            obj = self._target_objects_class()
            obj._set_data(response)
            ret = [obj]

        return ret


class AbstractObject(collections.MutableMapping):

    """
    Represents an abstract object (may or may not have explicitly be a node of
    the Graph) as a MutableMapping of its data.
    """

    _default_read_fields = []

    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[str(key)]

    def __setitem__(self, key, value):
        self._data[str(key)] = value

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        return key in self._data

    def __unicode__(self):
        return unicode(self._data)

    def __repr__(self):
        return "<%s> %s" % (
            self.__class__.__name__,
            json.dumps(
                self.export_value(self._data),
                sort_keys=True,
                indent=4,
                separators=(',', ': ')
            ),
        )

    @classmethod
    def get_endpoint(cls):
        """Returns the endpoint name.

        Raises:
            NotImplementedError if the method is not implemented in a class
                that derives from this abstract class.
        """
        raise NotImplementedError(
            "%s must have implemented get_endpoint." % cls.__name__
        )

    @classmethod
    def get_default_read_fields(cls):
        """Returns the class's list of default fields to read."""
        return cls._default_read_fields

    @classmethod
    def set_default_read_fields(cls, fields):
        """Sets the class's list of default fields to read.

        Args:
            fields: list of field names to read by default without specifying
                them explicitly during a read operation either via EdgeIterator
                or via AbstractCrudObject.read.
        """
        cls._default_read_fields = fields

    def _set_data(self, data):
        """
        An AbstractObject does not keep history so _set_data is an alias for
        a MutableMapping's update() method. _set_data elsewhere may have a
        different behavior depending on the type of the object and how the data
        should be processed.
        """
        self.update(data)

    def export_value(self, data):
        if isinstance(data, AbstractObject):
            data = data.export_data()
        elif isinstance(data, dict):
            data = dict((k, self.export_value(v))
                        for k, v in data.items()
                        if v is not None)
        elif isinstance(data, list):
            data = [self.export_value(v) for v in data]
        return data

    def export_data(self):
        return self.export_value(self._data)

    @classmethod
    def _assign_fields_to_params(cls, fields, params):
        """Applies fields to params in a consistent manner."""
        if fields is None:
            fields = cls.get_default_read_fields()
        if fields:
            params['fields'] = ','.join(fields)

class AbstractCrudObject(AbstractObject):
    """
    Extends AbstractObject and implements methods to create, read, update,
    and delete.

    Attributes:
        parent_id: The object's parent's id. (default None)
        api: The api instance associated with this object. (default None)
    """

    class Field(object):
        pass

    def __init__(self, fbid=None, parent_id=None, api=None):
        """Initializes a CRUD object.

        Args:
            fbid (optional): The id of the object ont the Graph.
            parent_id (optional): The id of the object's parent.
            api (optional): An api object which all calls will go through. If
                an api object is not specified, api calls will revert to going
                through the default api.
        """
        super(AbstractCrudObject, self).__init__()

        self._changes = {}
        self._data[self.Field.id] = fbid
        self._parent_id = parent_id
        self._api = api

    def __setitem__(self, key, value):
        """Sets an item in this CRUD object while maintaining a changelog."""

        if key not in self._data or self._data[key] != value:
            self._changes[key] = value

        super(AbstractCrudObject, self).__setitem__(key, value)

        return self

    def __delitem__(self, key):
        del self._data[key]
        if key in self._changes:
            del self._changes[key]

    def __eq__(self, other):
        """Two objects are the same if they have the same fbid."""
        return (
            # Same class
            isinstance(other, self.__class__) and

            # Both have id's
            self.get_id() is not None and other.get_id() is not None and

            # Both have same id
            self.get_id() == other.get_id()
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def get_by_ids(cls, ids, params=None, fields=None):
        params = dict(params or {})
        cls._assign_fields_to_params(fields, params)
        params['ids'] = ','.join(map(str, ids))
        response = FacebookAdsApi.get_default_api().call(
            FacebookAdsApi.HTTP_METHOD_GET,
            ['/'],
            params=params,
        )
        result = []
        for fbid, data in response.json().items():
            obj = cls(fbid, api=FacebookAdsApi.get_default_api())
            obj._set_data(data)
            result.append(obj)
        return result

    # Getters

    def get_id(self):
        """Returns the object's fbid if set. Else, it returns None."""
        if self[self.Field.id] is not None:
            return self[self.Field.id]
        else:
            return None

    def get_parent_id(self):
        """Returns the object's parent's id."""
        return self._parent_id or FacebookAdsApi.get_default_account_id()

    def get_api(self):
        """
        Returns the api associated with the object. If None, returns the default
        api.
        """
        if self._api is not None:
            return self._api
        else:
            return FacebookAdsApi.get_default_api()

    def get_id_assured(self):
        """Returns the fbid of the object.

        Raises:
            FacebookBadObjectError if the object does not have an id.
        """
        if (
            self.Field.id not in self or
            self[self.Field.id] is None
        ):
            raise FacebookBadObjectError(
                "%s object needs an id for this operation."
                % self.__class__.__name__
            )

        return self.get_id()

    def get_parent_id_assured(self):
        """Returns the object's parent's fbid.

        Raises:
            FacebookBadObjectError if the object does not have a parent id.
        """
        if self.get_parent_id() is None:
            raise FacebookBadObjectError(
                "%s object needs a parent_id for this operation."
                % self.__class__.__name__
            )

        return self.get_parent_id()

    def get_api_assured(self):
        """Returns the fbid of the object.

        Raises:
            FacebookBadObjectError if get_api returns None.
        """
        api = self.get_api()
        if api is None:
            raise FacebookBadObjectError(
                "%s does not yet have an associated api object."
                % self.__class__.__name__
            )

        return api

    # Data management

    def _clear_history(self):
        self._changes = {}
        return self

    def _set_data(self, data):
        """
        Sets object's data as if it were read from the server.
        Warning: Does not log changes.
        """
        for key in data:
            key = str(key)
            value = data[key]

            self._data[key] = value

            # clear history due to the update
            if key in self._changes:
                del self._changes[key]

        return self

    def export_data(self):
        """
        Returns a dictionary of property names mapped to their values for
        properties modified from their original values.
        """
        data = {}

        for key, value in self._changes.items():
            if isinstance(value, AbstractObject):
                data[key] = value.export_data()
            else:
                data[key] = value

        return data

    # CRUD Helpers

    def clear_id(self):
        """Clears the object's fbid."""
        del self[self.Field.id]
        return self

    def get_node_path(self):
        """Returns the node's relative path as a tuple of tokens."""
        return (self.get_id_assured(),)

    def get_node_path_string(self):
        """Returns the node's path as a tuple."""
        return '/'.join(self.get_node_path())

    # CRUD

    def remote_create(
        self,
        batch=None,
        failure=None,
        files=None,
        params=None,
        success=None,
    ):
        """Creates the object by calling the API.

        Args:
            batch (optional): A FacebookAdsApiBatch object. If specified,
                the call will be added to the batch.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
            files (optional): An optional mapping of file names to binary open
                file objects. These files will be attached to the request.
            success (optional): A callback function which will be called with
                the FacebookResponse of this call if the call succeeded.
            failure (optional): A callback function which will be called with
                the FacebookResponse of this call if the call failed.

        Returns:
            self if not a batch call.
            the return value of batch.add if a batch call.
        """
        if self.get_id() is not None:
            raise FacebookBadObjectError(
                "This %s object was already created." % self.__class__.__name__
            )

        params = {} if params is None else params.copy()
        params.update(self.export_data())

        if batch is not None:
            def callback_success(response):
                self._set_data(response.json())
                self._clear_history()

                if success is not None:
                    success(response)

            def callback_failure(response):
                if failure is not None:
                    failure(response)

            batch_call = batch.add(
                FacebookAdsApi.HTTP_METHOD_POST,
                (self.get_parent_id_assured(), self.get_endpoint()),
                params=params,
                files=files,
                success=callback_success,
                failure=callback_failure,
            )
            return batch_call
        else:
            response = self.get_api_assured().call(
                FacebookAdsApi.HTTP_METHOD_POST,
                (self.get_parent_id_assured(), self.get_endpoint()),
                params=params,
                files=files,
            )
            self._set_data(response.json())
            self._clear_history()

            return self

    def remote_read(
        self,
        batch=None,
        failure=None,
        fields=None,
        params=None,
        success=None,
    ):
        """Reads the object by calling the API.

        Args:
            batch (optional): A FacebookAdsApiBatch object. If specified,
                the call will be added to the batch.
            fields (optional): A list of fields to read.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
            files (optional): An optional mapping of file names to binary open
                file objects. These files will be attached to the request.
            success (optional): A callback function which will be called with
                the FacebookResponse of this call if the call succeeded.
            failure (optional): A callback function which will be called with
                the FacebookResponse of this call if the call failed.

        Returns:
            self if not a batch call.
            the return value of batch.add if a batch call.
        """
        params = dict(params or {})
        self._assign_fields_to_params(fields, params)

        if batch is not None:
            def callback_success(response):
                self._set_data(response.json())

                if success is not None:
                    success(response)

            def callback_failure(response):
                if failure is not None:
                    failure(response)

            batch_call = batch.add(
                FacebookAdsApi.HTTP_METHOD_GET,
                self.get_node_path(),
                params=params,
                success=callback_success,
                failure=callback_failure,
            )
            return batch_call
        else:
            response = self.get_api_assured().call(
                FacebookAdsApi.HTTP_METHOD_GET,
                self.get_node_path(),
                params=params,
            )
            self._set_data(response.json())

            return self

    def remote_update(
        self,
        batch=None,
        failure=None,
        files=None,
        params=None,
        success=None,
    ):
        """Updates the object by calling the API with only the changes recorded.

        Args:
            batch (optional): A FacebookAdsApiBatch object. If specified,
                the call will be added to the batch.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
            files (optional): An optional mapping of file names to binary open
                file objects. These files will be attached to the request.
            success (optional): A callback function which will be called with
                the FacebookResponse of this call if the call succeeded.
            failure (optional): A callback function which will be called with
                the FacebookResponse of this call if the call failed.

        Returns:
            self if not a batch call.
            the return value of batch.add if a batch call.
        """
        params = {} if params is None else params.copy()
        params.update(self.export_data())
        self._set_data(params)

        if batch is not None:
            def callback_success(response):
                self._clear_history()

                if success is not None:
                    success(response)

            def callback_failure(response):
                if failure is not None:
                    failure(response)

            batch_call = batch.add(
                FacebookAdsApi.HTTP_METHOD_POST,
                self.get_node_path(),
                failure=callback_failure,
                files=files,
                params=params,
                success=callback_success,
            )
            return batch_call
        else:
            self.get_api_assured().call(
                FacebookAdsApi.HTTP_METHOD_POST,
                self.get_node_path(),
                files=files,
                params=params,
            )
            self._clear_history()

            return self

    def remote_delete(
        self,
        batch=None,
        failure=None,
        params=None,
        success=None,
    ):
        """Deletes the object by calling the API with the DELETE http method.

        Args:
            batch (optional): A FacebookAdsApiBatch object. If specified,
                the call will be added to the batch.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
            success (optional): A callback function which will be called with
                the FacebookResponse of this call if the call succeeded.
            failure (optional): A callback function which will be called with
                the FacebookResponse of this call if the call failed.

        Returns:
            self if not a batch call.
            the return value of batch.add if a batch call.
        """
        if batch is not None:
            def callback_success(response):
                self.clear_id()

                if success is not None:
                    success(response)

            def callback_failure(response):
                if failure is not None:
                    failure(response)

            batch_call = batch.add(
                FacebookAdsApi.HTTP_METHOD_DELETE,
                self.get_node_path(),
                params=params,
                success=callback_success,
                failure=callback_failure,
            )
            return batch_call
        else:
            self.get_api_assured().call(
                FacebookAdsApi.HTTP_METHOD_DELETE,
                self.get_node_path(),
                params=params,
            )
            self.clear_id()

            return self

    # Helpers

    def save(self, *args, **kwargs):
        """
        Calls remote_create method if object has not been created. Else, calls
        the remote_update method.
        """
        if self.get_id() is not None:
            return self.remote_update(*args, **kwargs)
        else:
            return self.remote_create(*args, **kwargs)

    def iterate_edge(self, target_objects_class, fields=None, params=None):
        """
        Returns EdgeIterator with argument self as source_object and
        the rest as given __init__ arguments.

        Note: list(iterate_edge(...)) can prefetch all the objects.
        """
        source_object = self
        return EdgeIterator(
            source_object,
            target_objects_class,
            fields=fields,
            params=params
        )

    def edge_object(self, target_objects_class, fields=None, params=None):
        """
        Returns first object when iterating over EdgeIterator with argument
        self as source_object and the rest as given __init__ arguments.
        """
        params = {} if params is None else params.copy()
        params['limit'] = '1'
        for obj in self.iterate_edge(
            target_objects_class,
            fields=fields,
            params=params
        ):
            return obj

        # if nothing found, return None
        return None


class AdUser(CannotCreate, CannotDelete, CannotUpdate, AbstractCrudObject):

    """
    Represents an ad user.
    """

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
        """Returns iterator over AdAccount's associated with this user."""
        return self.iterate_edge(AdAccount, fields, params)

    def get_ad_account(self, fields=None, params=None):
        """Returns first AdAccount associated with this user."""
        return self.edge_object(AdAccount, fields, params)


class Activity(AbstractObject):

    class Field(object):
        event_time = 'event_time'
        event_type = 'event_type'

    @classmethod
    def get_endpoint(cls):
        return 'activities'


class AdAccount(CannotCreate, CannotDelete, AbstractCrudObject):

    class Field(object):
        account_groups = 'account_groups'
        account_id = 'account_id'
        account_status = 'account_status'
        age = 'age'
        agency_client_declaration = 'agency_client_declaration'
        amount_spent = 'amount_spent'
        balance = 'balance'
        business_city = 'business_city'
        business_country_code = 'business_country_code'
        business_name = 'business_name'
        business_state = 'business_state'
        business_street = 'business_street'
        business_street2 = 'business_street2'
        business_zip = 'business_zip'
        capabilities = 'capabilities'
        currency = 'currency'
        daily_spend_limit = 'daily_spend_limit'
        end_advertiser = 'end_advertiser'
        funding_source = 'funding_source'
        funding_source_details = 'funding_source_details'
        id = 'id'
        is_personal = 'is_personal'
        media_agency = 'media_agency'
        name = 'name'
        offsite_pixels_tos_accepted = 'offsite_pixels_tos_accepted'
        partner = 'partner'
        spend_cap = 'spend_cap'
        tax_id_status = 'tax_id_status'
        timezone_id = 'timezone_id'
        timezone_name = 'timezone_name'
        timezone_offset_hours_utc = 'timezone_offset_hours_utc'
        tos_accepted = 'tos_accepted'
        users = 'users'

    class AccountStatus(object):
        active = 1
        disabled = 2
        in_grace_period = 9
        pending_closure = 100
        pending_review = 7
        temporarily_unavailable = 101
        unsettled = 3

    class AgencyClientDeclaration(object):
        agency_representing_client = 'agency_representing_client'
        client_based_in_france = 'client_based_in_france'
        client_city = 'client_city'
        client_country_code = 'client_country_code'
        client_email_address = 'client_email_address'
        client_name = 'client_name'
        client_province = 'client_province'
        client_street = 'client_street'
        client_street2 = 'client_street2'
        has_written_mandate_from_advertiser = \
            'has_written_mandate_from_advertiser'
        is_client_paying_invoices = 'is_client_paying_invoices'

    class Capabilities(object):
        custom_audiences_folders = 'CUSTOM_AUDIENCES_FOLDERS'
        custom_audiences_opt_out_link = 'CUSTOM_AUDENCES_OPT_OUT_LINK'
        custom_cluster_sharing = 'CUSTOM_CLUSTER_SHARING'
        direct_sales = 'DIRECT_SALES'
        lookalike_audience = 'LOOKALIKE_AUDIENCE'
        new_campaign_structure = 'NEW_CAMPAIGN_STRUCTURE'
        premium = 'PREMIUM'
        view_tags = 'VIEW_TAGS'

    class TaxIdStatus(object):
        account_is_personal = 5
        offline_vat_validation_failed = 4
        unknown = 0
        vat_information_required = 3
        vat_not_required = 1

    @classmethod
    def get_endpoint(cls):
        return 'adaccounts'

    @classmethod
    def get_my_account(cls, api=None):
        """Returns first AdAccount associated with 'me' given api instance."""
        # Setup user and read the object from the server
        me = AdUser(fbid='me', api=api)

        # Get first account connected to the user
        my_account = me.edge_object(cls)

        return my_account

    def opt_out_user_from_targeting(self, schema, users, app_ids=[]):
        """Opts out users from being targeted by this ad account.

        Args:
            schema: A CustomAudience.Schema value
            users: a list of identites that follow the schema given

        Returns:
            Return FacebookResponse object
        """
        return self.get_api_assured().call(
            FacebookAdsApi.HTTP_METHOD_DELETE,
            (self.get_id_assured(), 'usersofanyaudience'),
            params=CustomAudience.format_params(schema, users, app_ids),
        )

    def get_activities(self, fields=None, params=None):
        """Returns iterator over Activity's associated with this account."""
        return self.iterate_edge(Activity, fields, params)

    def get_ad_users(self, fields=None, params=None):
        """Returns iterator over AdUser's associated with this account."""
        return self.iterate_edge(AdUser, fields, params)

    def get_ad_campaigns(self, fields=None, params=None):
        """Returns iterator over AdCampaign's associated with this account."""
        return self.iterate_edge(AdCampaign, fields, params)

    def get_ad_sets(self, fields=None, params=None):
        """Returns iterator over AdSet's associated with this account."""
        return self.iterate_edge(AdSet, fields, params)

    def get_ad_campaign_stats(self, fields=None, params=None):
        """
        Returns iterator over AdCampaignStats's associated with this account.
        """
        return self.iterate_edge(AdCampaignStats, fields, params)

    def get_ad_groups(self, fields=None, params=None):
        """Returns iterator over AdGroup's associated with this account."""
        return self.iterate_edge(AdGroup, fields, params)

    def get_ad_group_stats(self, fields=None, params=None):
        """Returns iterator over Activity's associated with this account."""
        return self.iterate_edge(AdGroupStats, fields, params)

    def get_ad_creatives(self, fields=None, params=None):
        """Returns iterator over AdCreative's associated with this account."""
        return self.iterate_edge(AdCreative, fields, params)

    def get_ad_images(self, fields=None, params=None):
        """Returns iterator over AdImage's associated with this account."""
        return self.iterate_edge(AdImage, fields, params)

    def get_broad_category_targeting(self, fields=None, params=None):
        """
        Returns iterator over BroadCategoryTargeting's associated with this
        account.
        """
        return self.iterate_edge(BroadCategoryTargeting, fields, params)

    def get_connection_objects(self, fields=None, params=None):
        """
        Returns iterator over ConnectionObject's associated with this account.
        """
        return self.iterate_edge(ConnectionObject, fields, params)

    def get_custom_audiences(self, fields=None, params=None):
        """
        Returns iterator over CustomAudience's associated with this account.
        """
        return self.iterate_edge(CustomAudience, fields, params)

    def get_partner_categories(self, fields=None, params=None):
        """
        Returns iterator over PartnerCategory's associated with this account.
        """
        return self.iterate_edge(PartnerCategory, fields, params)

    def get_rate_cards(self, fields=None, params=None):
        """Returns iterator over RateCard's associated with this account."""
        return self.iterate_edge(RateCard, fields, params)

    def get_reach_estimate(self, fields=None, params=None):
        """
        Returns iterator over ReachEstimate's associated with this account.
        """
        return self.iterate_edge(ReachEstimate, fields, params)

    def get_report_stats(self, fields=None, params=None):
        """Returns iterator over ReportStats's associated with this account."""
        return self.iterate_edge(ReportStats, fields, params)

    def get_stats(self, fields=None, params=None):
        """Returns iterator over AdStats's associated with this account."""
        return self.edge_object(AdStats, fields, params)

    def get_transactions(self, fields=None, params=None):
        """Returns iterator over Transaction's associated with this account."""
        return self.iterate_edge(Transaction, fields, params)

    def get_conversion_stats(self, fields=None, params=None):
        """
        Returns iterator over ConversionStats's associated with this account.
        """
        return self.edge_object(ConversionStats, fields, params)

    def get_ad_campaign_conversion_stats(self, fields=None, params=None):
        """Returns an AdCampaignConversionStats object for this account."""
        return self.edge_object(
            AdCampaignConversionStats,
            fields,
            params,
        )

    def get_ad_group_conversion_stats(self, fields=None, params=None):
        """Returns an AdGroupConversionStats object for this account."""
        return self.edge_object(AdGroupConversionStats, fields, params)

    def get_ad_preview(self, fields=None, params=None):
        """Returns iterator over AdPreview's associated with this account."""
        return self.iterate_edge(AdPreview, fields, params)


class AdAccountGroup(AbstractCrudObject):

    class Field(object):
        account_group_id = 'account_group_id'
        accounts = 'accounts'
        currency = 'currency'
        id = 'id'
        name = 'name'
        status = 'status'
        users = 'users'

    @classmethod
    def get_endpoint(cls):
        return 'adaccountgroups'

    def get_users(self, fields=None, params=None):
        """
        Returns iterator over AdAccountGroupUser's associated with this account
        group.
        """
        return self.iterate_edge(AdAccountGroupUser, fields, params)

    def get_accounts(self, fields=None, params=None):
        """
        Returns iterator over AdAccountGroupAccount's associated with this
        account group.
        """
        return self.iterate_edge(AdAccountGroupAccount, fields, params)


class AdAccountGroupAccount(AbstractCrudObject):

    class Field(object):
        account_id = 'account_id'
        status = 'status'

    @classmethod
    def get_endpoint(cls):
        return 'adaccounts'

    def get_node_path(self):
        return (
            self.get_parent_id_assured(),
            self.get_endpoint(),
            self.get_id_assured()
        )

    def get_ad_account(self):
        """Returns an AdAccount object with the same account id."""
        return AdAccount(fbid='act_' + self[self.Field.account_id])


class AdAccountGroupUser(AbstractCrudObject):

    class Field(object):
        id = 'uid'
        role = 'role'
        uid = 'uid'

    class Role(object):
        administrator = 1001
        general_user = 1002
        reports_only = 1003

    @classmethod
    def get_endpoint(cls):
        return 'users'

    def get_node_path(self):
        return (
            self.get_parent_id_assured(),
            self.get_endpoint(),
            self.get_id_assured()
        )

    def get_ad_user(self):
        """Returns an AdUser object with the same account id."""
        return AdUser(fbid=self[self.Field.uid])


class AdCampaign(CanValidate, HasStatus, HasObjective, CanArchive,
                 AbstractCrudObject):

    class Field(object):
        account_id = 'account_id'
        buying_type = 'buying_type'
        id = 'id'
        is_completed = 'is_completed'
        name = 'name'
        objective = 'objective'
        status = 'campaign_group_status'

    class BuyingType(object):
        auction = 'AUCTION'
        fixed_cpm = 'FIXED_CPM'
        mixed = 'MIXED'

    @classmethod
    def get_endpoint(cls):
        return 'adcampaign_groups'

    def get_ad_sets(self, fields=None, params=None):
        """Returns iterator over AdSet's associated with this campaign."""
        return self.iterate_edge(AdSet, fields, params)

    def get_ad_groups(self, fields=None, params=None):
        """Returns iterator over AdGroup's associated with this campaign."""
        return self.iterate_edge(AdGroup, fields, params)

    def get_stats(self, fields=None, params=None):
        """Returns iterator over AdStat's associated with this campaign."""
        return self.iterate_edge(AdStats, fields, params)


class AdSet(CanValidate, HasStatus, CanArchive, AbstractCrudObject):

    class Field(HasBidInfo, object):
        account_id = 'account_id'
        bid_info = 'bid_info'
        bid_type = 'bid_type'
        budget_remaining = 'budget_remaining'
        campaign_group_id = 'campaign_group_id'
        campaign_schedule = 'campaign_schedule'
        created_time = 'created_time'
        daily_budget = 'daily_budget'
        end_time = 'end_time'
        id = 'id'
        lifetime_budget = 'lifetime_budget'
        name = 'name'
        pacing_type = 'pacing_type'
        promoted_object = 'promoted_object'
        start_time = 'start_time'
        status = 'campaign_status'
        targeting = 'targeting'
        updated_time = 'updated_time'

    class BidType(object):
        absolute_ocpm = 'ABSOLUTE_OCPM'
        cpc = 'CPC'
        cpm = 'CPM'
        multi_premium = 'MULTI_PREMIUM'

    class PacingType(object):
        day_parting = 'day_parting'
        standard = 'standard'

    @classmethod
    def get_endpoint(cls):
        return 'adcampaigns'

    def get_ad_groups(self, fields=None, params=None):
        """Returns iterator over AdGroup's associated with this set."""
        return self.iterate_edge(AdGroup, fields, params)

    def get_ad_creatives(self, fields=None, params=None):
        """Returns iterator over AdCreative's associated with this set."""
        return self.iterate_edge(AdCreative, fields, params)

    def get_stats(self, fields=None, params=None):
        """Returns iterator over AdStat's associated with this set."""
        return self.iterate_edge(AdStats, fields, params)


class AdGroup(HasStatus, HasObjective, CanArchive, AbstractCrudObject):

    class Field(HasBidInfo, object):
        account_id = 'account_id'
        adgroup_review_feedback = 'adgroup_review_feedback'
        bid_info = 'bid_info'
        campaign_group_id = 'campaign_group_id'
        campaign_id = 'campaign_id'
        conversion_specs = 'conversion_specs'
        created_time = 'created_time'
        creative = 'creative'
        creative_ids = 'creative_ids'
        failed_delivery_checks = 'failed_delivery_checks'
        id = 'id'
        name = 'name'
        objective = 'objective'
        redownload = 'redownload'
        social_prefs = 'social_prefs'
        status = 'adgroup_status'
        tracking_specs = 'tracking_specs'
        updated_time = 'updated_time'
        view_tags = 'view_tags'

        class Creative(object):
            creative_id = 'creative_id'

    @classmethod
    def get_endpoint(cls):
        return 'adgroups'

    def get_ad_creatives(self, fields=None, params=None):
        """Returns iterator over AdCreative's associated with this ad."""
        return self.iterate_edge(AdCreative, fields, params)

    def get_targeting_description(self, fields=None, params=None):
        """
        Returns TargetingDescription object associated with this ad.
        """
        return self.edge_object(TargetingDescription, fields, params)

    def get_keyword_stats(self, fields=None, params=None):
        """Returns iterator over KeywordStats's associated with this ad."""
        return self.iterate_edge(KeywordStats, fields, params)

    def get_ad_preview(self, fields=None, params=None):
        """Returns AdGroupPreview object associated with this ad."""
        return self.edge_object(AdGroupPreview, fields, params)

    def get_reach_estimate(self, fields=None, params=None):
        """Returns iterator over ReachEstimate's associated with this ad."""
        return self.iterate_edge(ReachEstimate, fields, params)

    def get_stats(self, fields=None, params=None):
        """Returns AdStats object associated with this ad."""
        return self.edge_object(AdStats, fields, params)

    def get_click_tracking_tag(self, fields=None, params=None):
        """Returns iterator over ClickTrackingTag's associated with this ad."""
        return self.iterate_edge(ClickTrackingTag, fields, params)

    def get_conversion_stats(self, fields=None, params=None):
        """Returns ConversionStats object associated with this ad."""
        return self.edge_object(ConversionStats, fields, params)


class AdConversionPixel(AbstractCrudObject):

    class Field(object):
        creator = 'creator'
        id = 'id'
        js_pixel = 'js_pixel'
        name = 'name'
        status = 'status'
        tag = 'tag'
        value = 'value'

    @classmethod
    def get_endpoint(cls):
        return 'offsitepixels'


class AdCreative(AbstractCrudObject):

    class Field(object):
        actor_id = 'actor_id'
        actor_image_hash = 'actor_image_hash'
        actor_name = 'actor_name'
        body = 'body'
        call_to_action_type = 'call_to_action_type'
        follow_redirect = 'follow_redirect'
        id = 'id'
        image_crops = 'image_crops'
        image_file = 'image_file'
        image_hash = 'image_hash'
        image_url = 'image_url'
        link_deep_link_url = 'link_deep_link_url'
        link_url = 'link_url'
        name = 'name'
        object_id = 'object_id'
        object_store_url = 'object_store_url'
        object_story_id = 'object_story_id'
        object_story_spec = 'object_story_spec'
        object_type = 'object_type'
        object_url = 'object_url'
        preview_url = 'preview_url'
        thumbnail_url = 'thumbnail_url'
        title = 'title'
        url_tags = 'url_tags'
        video_id = 'video_id'

    @classmethod
    def get_endpoint(cls):
        return 'adcreatives'

    def get_ad_preview(self, fields=None, params=None):
        """Returns iterator over AdPreview's associated with this creative."""
        return self.iterate_edge(AdPreview, fields, params)


class AdImage(CannotUpdate, AbstractCrudObject):

    class Field(object):
        creatives = 'creatives'
        filename = 'filename'
        hash = 'hash'
        id = 'id'
        url = 'url'

    @classmethod
    def get_endpoint(cls):
        return 'adimages'

    def get_node_path(self):
        return (self.get_parent_id_assured(), self.get_endpoint())

    def _set_data(self, data):
        """
            `data` may have a different structure depending if you're creating
            new AdImages or iterating over existing ones using something like
            AdAccount.get_ad_images().

            While reading existing images, _set_data from AbstractCrudObject
            handles everything correctly, but we need to treat the remote_create
            case.

            remote_create sample response:
            {
              "images": {
                "8cf726a44ab7008c5cc6b4ebd2491234": {
                  "hash":"8cf726a44ab7008c5cc6b4ebd2491234",
                  "url":"https://fbcdn-photos-a.akamaihd.net/..."
                }
              }
            }

            Sample response when calling act_<ACT_ID>/adimages, used internally
            by AdAccount.get_ad_images():
            {
              "data": [
                {
                  "hash": "181b88e3cdf6464af7ed52fe488fe559",
                  "id": "1739564149602806:181b88e3cdf6464af7ed52fe488fe559"
                }
              ],
              "paging": {
                "cursors": {
                  "before": "MTczOTU2NDE0OTYwMjgwNjoxODFiODh==",
                  "after": "MTczOTU2NDE0OTYwMjgwNjoxODFiODhl=="
                }
              }
            }
        """

        if 'images' in data.keys():
            data = list(data['images'].values())[0]

            for key in data:
                key = str(key)
                value = data[key]

                self._data[key] = value

                # clear history due to the update
                if key in self._changes:
                    del self._changes[key]

            self._data[self.Field.id] = '%s:%s' % (
                self.get_parent_id_assured()[4:],
                self[self.Field.hash],
            )

            return self
        else:
            return super(AdImage, self)._set_data(data)

    def remote_create(
        self,
        batch=None,
        failure=None,
        files=None,
        params=None,
        success=None,
    ):
        """Uploads filename and creates the AdImage object from it.

        It has same arguments as AbstractCrudObject.remote_create except it does
        not have the files argument but requires the 'filename' property to be
        defined.
        """
        if self[self.Field.filename] is None:
            raise FacebookBadObjectError(
                "AdImage required a filename to be defined."
            )
        filename = self[self.Field.filename]
        open_file = open(filename, 'rb')
        return_val = super(AdImage, self).remote_create(
            files={filename: open_file},
            batch=batch,
            failure=failure,
            params=params,
            success=success,
        )
        open_file.close()
        return return_val

    def get_hash(self):
        """Returns the image hash to which AdCreative's can refer."""
        return self[self.Field.hash]

    def remote_read(
        self,
        batch=None,
        failure=None,
        fields=None,
        params=None,
        success=None,
    ):
        if self[AdImage.Field.id]:
            _, image_hash = self[AdImage.Field.id].split(':')
            account = AdAccount(fbid=self.get_parent_id_assured())
            params = {
                'hashes': [
                    image_hash,
                ],
            }
            images = account.get_ad_images(fields=fields, params=params)
            if images:
                self._set_data(images[0]._data)



class AdPreview(AbstractObject):

    class Field(object):
        ad_format = 'ad_format'
        body = 'body'
        creative = 'creative'
        post = 'post'

    class AdFormat(object):
        desktop_feed_standard = 'DESKTOP_FEED_STANDARD'
        mobile_banner = 'MOBILE_BANNER'
        mobile_feed_standard = 'MOBILE_FEED_STANDARD'
        mobile_interstitial = 'MOBILE_INTERSTITIAL'
        right_column_standard = 'RIGHT_COLUMN_STANDARD'

    @classmethod
    def get_endpoint(cls):
        return 'generatepreviews'

    def get_html(self):
        """Returns the preview html."""
        return self[self.Field.body]


class AdCreativePreview(AdPreview):

    @classmethod
    def get_endpoint(cls):
        return 'previews'


class AdGroupPreview(AdCreativePreview):

    pass


# Stats for an object - e.g. {adgroup id}/stats
class AdStats(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'stats'


class AdCampaignStats(AdStats):

    @classmethod
    def get_endpoint(cls):
        return 'adcampaignstats'


class AdGroupStats(AdStats):

    @classmethod
    def get_endpoint(cls):
        return 'adgroupstats'


class ReportStats(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'reportstats'


class ConversionStats(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'conversions'


class AdCampaignConversionStats(AdStats):

    @classmethod
    def get_endpoint(cls):
        return 'adcampaignconversions'


class AdGroupConversionStats(AdStats):

    @classmethod
    def get_endpoint(cls):
        return 'adgroupconversions'


class KeywordStats(AdStats):

    @classmethod
    def get_endpoint(cls):
        return 'keywordstats'


class BroadCategoryTargeting(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'broadtargetingcategories'


class ClickTrackingTag(AbstractCrudObject):

    class Field(object):
        add_template_param = 'add_template_param'
        adgroup_id = 'adgroup_id'
        id = 'id'
        url = 'url'

    @classmethod
    def get_endpoint(cls):
        return 'trackingtag'


class CustomAudience(AbstractCrudObject):

    class Field(object):
        account_id = 'account_id'
        approximate_count = 'approximate_count'
        data_source = 'data_source'
        delivery_status = 'delivery_status'
        description = 'description'
        force_delete_lookalikes = 'force_delete_lookalikes'
        id = 'id'
        lookalike_audience_ids = 'lookalike_audience_ids'
        lookalike_spec = 'lookalike_spec'
        name = 'name'
        operation_status = 'operation_status'
        opt_out_link = 'opt_out_link'
        permission_for_actions = 'permission_for_actions'
        prefill = 'prefill'
        retention_days = 'retention_days'
        rule = 'rule'
        subtype = 'subtype'
        time_updated = 'time_updated'

    class Schema(object):
        uid = 'UID'
        email_hash = 'EMAIL_SHA256'
        phone_hash = 'PHONE_SHA256'
        mobile_advertiser_id = 'MOBILE_ADVERTISER_ID'

    @classmethod
    def get_endpoint(cls):
        return 'customaudiences'

    @classmethod
    def format_params(cls, schema, users, app_ids=[]):
        hashed_users = []
        if schema == cls.Schema.phone_hash or schema == cls.Schema.email_hash:
            for user in users:
                if schema == cls.Schema.email_hash:
                    user = user.strip(" \t\r\n\0\x0B.").lower()
                if isinstance(user, six.text_type):
                    user = user.encode('utf8')  # required for hashlib
                hashed_users.append(hashlib.sha256(user).hexdigest())

        payload = {
            'schema': schema,
            'data': hashed_users or users,
        }

        if schema == cls.Schema.uid:
            if not app_ids:
                raise FacebookBadObjectError(
                    "Custom Audiences with type " + cls.Schema.uid +
                    "require at least one app_id"
                )
            payload['app_ids'] = app_ids

        return {
            'payload': payload,
        }

    def add_users(self, schema, users, app_ids=[]):
        """Adds users to this CustomAudience.

        Args:
            schema: A CustomAudience.Schema value specifying the type of values
                in the users list.
            users: A list of identities respecting the schema specified.

        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            FacebookAdsApi.HTTP_METHOD_POST,
            (self.get_id_assured(), 'users'),
            params=CustomAudience.format_params(schema, users, app_ids),
        )

    def remove_users(self, schema, users, app_ids=[]):
        """Deletes users from this CustomAudience.

        Args:
            schema: A CustomAudience.Schema value specifying the type of values
                in the users list.
            users: A list of identities respecting the schema specified.

        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            FacebookAdsApi.HTTP_METHOD_DELETE,
            (self.get_id_assured(), 'users'),
            params=CustomAudience.format_params(schema, users, app_ids),
        )

    def share_audience(self, account_ids):
        """Shares this CustomAudience with the specified account_ids.

        Args:
            account_ids: A list of account ids.

        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            FacebookAdsApi.HTTP_METHOD_POST,
            (self.get_id_assured(), 'adaccounts'),
            params={'adaccounts': account_ids},
        )

    def unshare_audience(self, account_ids):
        """Unshares this CustomAudience with the specified account_ids.

        Args:
            account_ids: A list of account ids.

        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            FacebookAdsApi.HTTP_METHOD_DELETE,
            (self.get_id_assured(), 'users'),
            params={'adaccounts': account_ids},
        )


class ConnectionObject(AbstractObject):

    class Field(object):
        app_installs_tracked = 'app_installs_tracked'
        id = 'id'
        is_game = 'is_game'
        name = 'name'
        native_app_store_ids = 'native_app_store_ids'
        native_app_targeting_ids = 'native_app_targeting_ids'
        og_actions = 'og_actions'
        og_namespace = 'og_namespace'
        og_object = 'og_object'
        picture = 'picture'
        supported_platforms = 'supported_platforms'
        tabs = 'tabs'
        type = 'type'
        url = 'url'

    class Type(object):
        application = 2
        domain = 7
        event = 3
        page = 1
        place = 6

    @classmethod
    def get_endpoint(cls):
        return 'connectionobjects'


class LookalikeAudience(AbstractCrudObject):

    class Field(object):
        name = 'name'
        lookalike_spec = 'lookalike_spec'
        origin_audience_id = 'origin_audience_id'

        page_id = 'page_id'
        conversion_type = 'conversion_type'
        country = 'country'
        ratio = 'ratio'

        class LookalikeSpec(object):
            type = 'type'
            ratio = 'raito'
            country = 'country'
            pixel_ids = 'pixel_ids'
            conversion_type = 'conversion_type'

    class LookalikeType(object):
        reach = 'reach'
        similarity = 'similarity'

    class ConversionType(object):
        page_likes = 'page_likes'

    @classmethod
    def get_endpoint(cls):
        return 'customaudiences'


class PartnerCategory(
    CannotCreate,
    CannotUpdate,
    CannotDelete,
    AbstractCrudObject,
):

    class Field(object):
        description = 'description'
        details = 'details'
        id = 'id'
        name = 'name'
        parent_category = 'parent_category'
        source = 'source'
        status = 'status'

    @classmethod
    def get_endpoint(cls):
        return 'partnercategories'


class RateCard(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'ratecard'


class ReachEstimate(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'reachestimate'


class ReachFrequencyPrediction(AbstractCrudObject):

    class Field(object):
        account_id = 'account_id'
        action = 'action'
        budget = 'budget'
        buying_type = 'buying_type'
        campaign_id = 'campaign_id'
        campaign_time_start = 'campaign_time_start'
        campaign_time_stop = 'campaign_time_stop'
        curve_budget_reach = 'curve_budget_reach'
        destination_id = 'destination_id'
        end_time = 'end_time'
        external_budget = 'external_budget'
        external_impression = 'external_impression'
        external_maximum_budget = 'external_maximum_budget'
        external_maximum_impression = 'external_maximum_impression'
        external_maximum_reach = 'external_maximum_reach'
        external_minimum_budget = 'external_maximum_budget'
        external_minimum_impression = 'external_maximum_impression'
        external_minimum_reach = 'external_maximum_reach'
        external_reach = 'external_reach'
        frequency_cap = 'frequency_cap'
        id = 'id'
        impression = 'impression'
        objective = 'objective'
        prediction_id = 'rf_prediction_id'
        prediction_id_to_release = 'rf_prediction_id_to_release'
        prediction_id_to_share = 'prediction_id_to_share'
        prediction_mode = 'prediction_mode'
        prediction_progress = 'prediction_progress'
        reach = 'reach'
        start_time = 'start_time'
        status = 'status'
        story_event_type = 'story_event_type'
        target_audience_size = 'target_audience_size'
        target_spec = 'target_spec'
        time_created = 'time_created'

    class Action(object):
        reserve = 'reserve'
        cancel = 'cancel'

    @classmethod
    def get_endpoint(cls):
        return 'reachfrequencypredictions'

    def reserve(
        self,
        prediction_to_release=None,
        reach=None,
        budget=None,
        impression=None,
    ):
        params = {
            self.Field.prediction_id: self.get_id_assured(),
            self.Field.prediction_id_to_release: prediction_to_release,
            self.Field.budget: budget,
            self.Field.reach: reach,
            self.Field.impression: impression,
            self.Field.action: self.Action.reserve,
        }
        # Filter out None values.
        params = dict((k, v) for k, v in params.items() if v is not None)

        response = self.get_api_assured().call(
            FacebookAdsApi.HTTP_METHOD_POST,
            (self.get_parent_id_assured(), self.get_endpoint()),
            params=params,
        )

        return self.__class__(response.body(), self.get_parent_id_assured())

    def cancel(self):
        params = {
            self.Field.prediction_id: self.get_id_assured(),
            self.Field.action: self.Action.cancel,
        }
        self.get_api_assured().call(
            FacebookAdsApi.HTTP_METHOD_POST,
            (self.get_parent_id_assured(), self.get_endpoint()),
            params=params,
        )
        return self


class TargetingDescription(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'targetingsentencelines'


class TargetingSearch(AbstractObject):

    class DemographicSearchClasses(object):
        demographics = 'demographics'
        ethnic_affinity = 'ethnic_affinity'
        family_statuses = 'family_statuses'
        generation = 'generation'
        home_ownership = 'home_ownership'
        home_type = 'home_type'
        home_value = 'home_value'
        household_composition = 'household_composition'
        income = 'income'
        industries = 'industries'
        life_events = 'life_events'
        markets = 'markets'
        moms = 'moms'
        net_worth = 'net_worth'
        office_type = 'office_type'
        politics = 'politics'

    class TargetingSearchTypes(object):
        city = 'adcity'
        country = 'adcountry'
        education = 'adeducationschool'
        employer = 'adworkemployer'
        geolocation = 'adgeolocation'
        interest = 'adinterest'
        interest_suggestion = 'adinterestsuggestion'
        interest_validate = 'adinterestvalid'
        keyword = 'adkeyword'
        locale = 'adlocale'
        major = 'adeducationmajor'
        position = 'adworkposition'
        radius_suggestion = 'adradiussuggestion'
        region = 'adregion'
        targeting_category = 'adtargetingcategory'
        zipcode = 'adzipcode'

    @classmethod
    def search(cls, type, target_class=None, query=None, params=None, api=None):
        # TODO
        return None


class TargetingSpecsField(object):

    age_max = 'age_max'
    age_min = 'age_min'
    behaviors = 'behaviors'
    college_years = 'college_years'
    conjunctive_user_adclusters = 'conjunctive_user_adclusters'
    connections = 'connections'
    custom_audiences = 'custom_audiences'
    education_majors = 'education_majors'
    education_schools = 'education_schools'
    education_statuses = 'education_statuses'
    ethnic_affinity = 'ethnic_affinity'
    excluded_connections = 'excluded_connections'
    excluded_custom_audiences = 'excluded_custom_audiences'
    excluded_geo_locations = 'excluded_geo_locations'
    excluded_user_adclusters = 'excluded_user_adclusters'
    friends_of_connections = 'friends_of_connections'
    genders = 'genders'
    generation = 'generation'
    geo_locations = 'geo_locations'
    home_ownership = 'home_ownership'
    home_type = 'home_type'
    home_value = 'home_value'
    household_composition = 'household_composition'
    income = 'income'
    industries = 'industries'
    interested_in = 'interested_in'
    interests = 'interests'
    life_events = 'life_events'
    locales = 'locales'
    markets = 'markets'
    moms = 'moms'
    net_worth = 'net_worth'
    office_type = 'office_type'
    page_types = 'page_types'
    politics = 'politics'
    relationship_statuses = 'relationship_statuses'
    user_adclusters = 'user_adclusters'
    user_device = 'user_device'
    user_os = 'user_os'
    wireless_carrier = 'wireless_carrier'
    work_employers = 'work_employers'
    work_positions = 'work_positions'
    zips = 'zips'


class Transaction(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'transactions'


class AutoComplete(AbstractCrudObject):

    class Type(object):
        adcountry = 'adcountry'
        adregion = 'adregion'
        adcity = 'adcity'
        adeducationschool = 'adeducationschool'
        adeducationmajor = 'adeducationmajor'
        adlocale = 'adlocale'
        adworkemployer = 'adworkemployer'
        adworkposition = 'adworkposition'
        adkeyword = 'adkeyword'
        adzipcode = 'adzipcode'
        adgeolocation = 'adgeolocation'

    @classmethod
    def get_endpoint(cls):
        return 'search'

    def get_node_path(self):
        return (
            self.get_endpoint(),
        )
