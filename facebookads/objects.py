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

import collections
import pprint
pp = pprint.PrettyPrinter(indent=4)


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
        if fields is None:
            fields = []

        fields = ','.join([
            field for field in (
                fields if fields
                else target_objects_class.get_default_read_fields()
            )
        ])

        self._params = {} if params is None else params.copy()

        if fields:
            self._params['fields'] = fields

        self._source_object = source_object
        self._target_objects_class = target_objects_class
        self._path = (
            source_object.get_id_assured(),
            target_objects_class.get_endpoint(),
        )
        self._queue = []
        self._finished_iteration = False

    def __iter__(self):
        return self

    def __next__(self):
        # Load next page at end.
        # If load_next_page returns False, raise StopIteration exception
        if not self._queue and not self.load_next_page():
            raise StopIteration()

        return self._queue.pop(0)

    next = __next__

    def load_next_page(self):
        """Queries server for more nodes and loads them into the internal queue.

        Returns:
            True if successful, else False.
        """
        if self._finished_iteration:
            return False

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

        num_added = 0
        for json_obj in response['data']:
            obj = self._target_objects_class()
            obj._read_update(json_obj)
            self._queue.append(obj)
            num_added += 1

        return num_added > 0


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

    def __str__(self):
        return str(self._data)

    def __unicode__(self):
        return unicode(self._data)

    def __repr__(self):
        return pp.pformat(self._data)

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

    def _read_update(self, data):
        """
        An AbstractObject does not keep history so _read_update is an alias for
        a MutableMapping's update() method. _read_update elsewhere may have a
        different behavior depending on the type of the object and how the data
        should be processed.
        """
        self.update(data)

    def export_data(self):
        """Returns a dictionary of property names mapped to their values."""
        data = {}

        for key in self:
            if self[key] is not None:
                data[key] = self[key]

        return data


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

        if fbid is not None:
            self[self.__class__.Field.id] = fbid

        self.parent_id = parent_id
        self.api = api

    def __setitem__(self, key, value):
        """Sets an item in this CRUD object while maintaining a changelog."""
        key = str(key)

        key_already_set = key in self._data
        if key_already_set:
            old_data_value = self._data[key]

        self._data[key] = value

        if key_already_set:
            if key in self._changes:
                # key already set and has been a result of user change
                if (
                    'original' in self._changes[key] and
                    value == self._changes['key']['original']
                ):
                    # value is being set back to original
                    del self._changes['key']
                else:
                    # There's a new value
                    self._changes[key]['new'] = value
            elif value != old_data_value:
                # key already set and not in changes (has original value)
                self._changes[key] = {
                    'original': old_data_value,
                    'new': value,
                }
        else:
            # There's a new value
            self._changes[key] = {
                'new': value,
            }

        return self

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

    # Getters

    def get_id(self):
        """Returns the object's fbid if set. Else, it returns None."""
        if self.__class__.Field.id in self:
            return self[self.__class__.Field.id]
        else:
            return None

    def get_parent_id(self):
        """Returns the object's parent's id."""
        return self.parent_id

    def get_api(self):
        """
        Returns the api associated with the object. If None, returns the default
        api.
        """
        if self.api is not None:
            return self.api
        else:
            return FacebookAdsApi.get_default_api()

    def get_id_assured(self):
        """Returns the fbid of the object.

        Raises:
            FacebookBadObjectError if the object does not have an id.
        """
        if (
            self.__class__.Field.id not in self or
            self[self.__class__.Field.id] is None
        ):
            raise FacebookBadObjectError(
                "%s object needs an id for this operation."
                % self.__class__.__name__
            )

        return self[self.__class__.Field.id]

    def get_parent_id_assured(self):
        """Returns the object's parent's fbid.

        Raises:
            FacebookBadObjectError if the object does not have a parent id.
        """
        if self.parent_id is None:
            raise FacebookBadObjectError(
                "%s object needs a parent_id for this operation."
                % self.__class__.__name__
            )

        return self.parent_id

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

    def _read_update(self, data):
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

        for key in self._changes:
            value = self._changes[key]['new']
            if isinstance(value, AbstractObject):
                data[key] = value.export_data()
            else:
                data[key] = value

        return data

    # CRUD Helpers

    def clear_id(self):
        """Clears the object's fbid."""
        del self[self.__class__.Field.id]
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
        if self.__class__.Field.id in self:
            raise FacebookBadObjectError(
                "This %s object was alread created." % self.__class__.__name__
            )

        params = {} if params is None else params.copy()
        params.update(self.export_data())

        if batch is not None:
            def callback_success(response):
                self._read_update(response.json())
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
            self._read_update(response.json())

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
        if not fields:
            fields = self.get_default_read_fields()

        if fields:
            params = {} if params is None else params.copy()

            fields = ','.join(
                fields if fields
                else self.get_default_read_fields()
            )

            params['fields'] = fields

        if batch is not None:
            def callback_success(response):
                self._read_update(response.json())

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
            self._read_update(response.json())

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
        if self.__class__.Field.id in self:
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

    def child(self, target_object_class):
        """
        Returns an instance of target_object_class with self's id as parent_id.
        """
        return target_object_class(parent_id=self.get_id_assured())


class CannotCreate(object):

    """
    An instance of CannotCreate will raise a TypeError when calling
    remote_create().
    """

    @classmethod
    def remote_create(cls, *args, **kwargs):
        raise TypeError('Cannot create object of type %s.' % cls.__name__)


class CannotDelete(object):

    """
    An instance of CannotDelete will raise a TypeError when calling
    remote_delete().
    """

    @classmethod
    def remote_delete(cls, *args, **kwargs):
        raise TypeError('Cannot delete object of type %s.' % cls.__name__)


class CannotUpdate(object):

    """
    An instance of CannotUpdate will raise a TypeError when calling
    remote_update().
    """

    @classmethod
    def remote_update(cls, *args, **kwargs):
        raise TypeError('Cannot update object of type %s.' % cls.__name__)


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

    pass


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
        timezon_id = 'timezone_id'
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

    def opt_out_user_from_targeting(self, schema, users):
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
            params={'payload': {'schema': schema, 'data': users}},
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
        return AdAccount(fbid='act_' + self[self.__class__.Field.account_id])


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
        return AdUser(fbid=self[self.__class__.Field.uid])


class HasObjective(object):

    """
    An instance or HasObjective will have an enum attribute Objective.
    """

    class Objective(object):
        canvas_app_engagement = 'CANVAS_APP_ENGAGEMENT'
        canvas_app_installs = 'CANVAS_APP_INSTALLS'
        event_responses = 'EVENT_RESPONSES'
        mobile_app_engagement = 'MOBILE_APP_ENGAGEMENT'
        mobile_app_installs = 'MOBILE_APP_INSTALLS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        website_clicks = 'WEBSITE_CLICKS'
        website_conversions = 'WEBSITE_CONVERSIONS'


class HasStatus(object):

    """
    An instance or HasObjective will have an enum attribute Status.
    """

    class Status(object):
        active = 'ACTIVE'
        archived = 'ARCHIVED'
        deleted = 'DELETED'
        paused = 'PAUSED'


class AdCampaign(HasStatus, HasObjective, AbstractCrudObject):

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


class HasBidInfo(object):

    """
    An instance or HasObjective will have an enum attribute BidInfo.
    """

    class BidInfo(object):
        actions = 'ACTIONS'
        clicks = 'CLICKS'
        impressions = 'IMPRESSIONS'
        reach = 'REACH'
        social = 'SOCIAL'


class AdSet(HasStatus, AbstractCrudObject):

    class Field(HasBidInfo, object):
        account_id = 'account_id'
        bid_info = 'bid_info'
        bid_type = 'bid_type'
        budget_remaining = 'budget_remaining'
        campaign_group_id = 'campaign_group_id'
        created_time = 'created_time'
        daily_budget = 'daily_budget'
        end_time = 'end_time'
        id = 'id'
        lifetime_budget = 'lifetime_budget'
        name = 'name'
        start_time = 'start_time'
        status = 'campaign_status'
        targeting = 'targeting'
        updated_time = 'updated_time'

    class BidType(object):
        absolute_ocpm = 'absolute_ocpm'
        cpc = 'CPC'
        cpm = 'CPM'
        multi_premium = 'multi_premium'

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


class AdGroup(HasStatus, HasObjective, AbstractCrudObject):

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
        object_type = 'object_type'
        object_url = 'object_url'
        preview_url = 'preview_url'
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

    def _read_update(self, data):
        data = list(data['images'].values())[0]

        for key in data:
            key = str(key)
            value = data[key]

            self._data[key] = value

            # clear history due to the update
            if key in self._changes:
                del self._changes[key]

        self._data[self.__class__.Field.id] = '%s:%s' % (
            self.get_parent_id_assured()[4:],
            self[self.__class__.Field.hash],
        )

        return self

    def remote_create_from_filename(
        self,
        filename,
        batch=None,
        failure=None,
        params=None,
        success=None,
    ):
        """Uploads filename and creates the AdImage object from it.

        It has same arguments as AbstractCrudObject.remote_create except it does
        not have a 'files' keyword argument. Instead, it has a required
        'filename' argument.
        """
        open_file = open(filename, 'rb')
        return_val = self.remote_create(
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
        return self[self.__class__.Field.hash]


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
        return self[self.__class__.Field.body]


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
        description = 'description'
        id = 'id'
        name = 'name'
        opt_out_link = 'opt_out_link'

        account_id = 'account_id'
        approximate_count = 'approximate_count'
        data_source = 'data_source'
        delivery_status = 'delivery_status'
        lookalike_audience_ids = 'lookalike_audience_ids'
        permission_for_actions = 'permission_for_actions'
        operation_status = 'operation_status'
        subtype = 'subtype'
        time_updated = 'time_updated'

        force_delete_lookalikes = 'force_delete_lookalikes'

    class Schema(object):
        uid = 'UID'
        email_hash = 'EMAIL_SHA256'
        phone_hash = 'PHONE_SHA256'
        mobile_advertiser_id = 'MOBILE_ADVERTISER_ID'

    @classmethod
    def get_endpoint(cls):
        return 'customaudiences'

    def add_users(self, schema, users):
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
            params={'payload': {'schema': schema, 'data': users}},
        )

    def remove_users(self, schema, users):
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
            params={'payload': {'schema': schema, 'data': users}},
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
