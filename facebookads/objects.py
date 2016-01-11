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

from facebookads.exceptions import (
    FacebookBadObjectError,
    FacebookError,
    FacebookUnavailablePropertyException,
)
from facebookads.api import FacebookAdsApi
from facebookads.session import FacebookSession
from facebookads.mixins import (
    CanArchive,
    CanValidate,
    CannotCreate,
    CannotDelete,
    CannotUpdate,
    HasObjective,
    HasStatus,
    HasBidInfo,
    HasAdLabels,
)
from facebookads.video_uploader import (
    VideoUploader,
    VideoUploadRequest,
    VideoEncodingStatusChecker,
)

import hashlib
import collections
import json
import six
import base64
import warnings
import functools
import re


def deprecated(fun=None, replacement=None):
    if fun is None:
        return functools.partial(deprecated, replacement=replacement)

    @functools.wraps(fun)
    def inner(*args, **kwargs):
        msg = "%s is deprecated" % fun.__name__
        if replacement:
            msg += "; use %s instead" % replacement
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
        doc = msg + '\n'
        if fun.__doc__:
            doc += fun.__doc__
        fun.__doc__ = doc
        return fun(*args, **kwargs)
    return inner


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
        include_summary=True,
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
        self.params = dict(params or {})
        target_objects_class._assign_fields_to_params(fields, self.params)
        self._source_object = source_object
        self._target_objects_class = target_objects_class
        self._path = (
            source_object.get_id_assured(),
            target_objects_class.get_endpoint(),
        )
        self._queue = []
        self._finished_iteration = False
        self._total_count = None
        self._include_summary = include_summary

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
        if self._total_count is None:
            raise FacebookUnavailablePropertyException(
                "Couldn't retrieve the object total count for that type "
                "of request.",
            )
        return self._total_count

    def load_next_page(self):
        """Queries server for more nodes and loads them into the internal queue.

        Returns:
            True if successful, else False.
        """
        if self._finished_iteration:
            return False

        if self._include_summary:
            if 'summary' not in self.params:
                self.params['summary'] = True

        response = self._source_object.get_api_assured().call(
            'GET',
            self._path,
            params=self.params,
        ).json()

        if 'paging' in response and 'next' in response['paging']:
            self._path = response['paging']['next']
        else:
            # Indicate if this was the last page
            self._finished_iteration = True

        if (
            self._include_summary and
            'summary' in response and
            'total_count' in response['summary']
        ):
            self._total_count = response['summary']['total_count']

        self._queue = self.build_objects_from_response(response)
        return len(self._queue) > 0

    def build_objects_from_response(self, response):
        if 'data' in response and isinstance(response['data'], list):
            ret = []
            if isinstance(response['data'], list):
                for json_obj in response['data']:
                    obj = self._target_objects_class()
                    obj._set_data(json_obj)
                    ret.append(obj)
            else:
                obj = self._target_objects_class()
                obj._set_data(response['data'])
                ret.append(obj)
        else:
            data = response['data'] if 'data' in response else response
            obj = self._target_objects_class()
            obj._set_data(data)
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
                separators=(',', ': '),
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
            "%s must have implemented get_endpoint." % cls.__name__,
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

    @classmethod
    def _assign_fields_to_params(cls, fields, params):
        """Applies fields to params in a consistent manner."""
        if fields is None:
            fields = cls.get_default_read_fields()
        if fields:
            params['fields'] = ','.join(fields)

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
        self._parent_id = parent_id
        self._api = api
        self._data[self.Field.id] = fbid
        self._include_summary = True

    def __setitem__(self, key, value):
        """Sets an item in this CRUD object while maintaining a changelog."""

        if key not in self._data or self._data[key] != value:
            self._changes[key] = value

        super(AbstractCrudObject, self).__setitem__(key, value)

        return self

    def __delitem__(self, key):
        del self._data[key]
        self._changes.pop(key, None)

    def __eq__(self, other):
        """Two objects are the same if they have the same fbid."""
        return (
            # Same class
            isinstance(other, self.__class__) and

            # Both have id's
            self.get_id() and other.get_id() and

            # Both have same id
            self.get_id() == other.get_id()
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def get_by_ids(cls, ids, params=None, fields=None, api=None):
        api = api or FacebookAdsApi.get_default_api()
        params = dict(params or {})
        cls._assign_fields_to_params(fields, params)
        params['ids'] = ','.join(map(str, ids))
        response = api.call(
            'GET',
            ['/'],
            params=params,
        )
        result = []
        for fbid, data in response.json().items():
            obj = cls(fbid, api=api)
            obj._set_data(data)
            result.append(obj)
        return result

    # Getters

    def get_id(self):
        """Returns the object's fbid if set. Else, it returns None."""
        return self.get(self.Field.id)

    def get_parent_id(self):
        """Returns the object's parent's id."""
        return self._parent_id or FacebookAdsApi.get_default_account_id()

    def get_api(self):
        """
        Returns the api associated with the object. If None, returns the
        default api.
        """
        return self._api or FacebookAdsApi.get_default_api()

    def get_id_assured(self):
        """Returns the fbid of the object.

        Raises:
            FacebookBadObjectError if the object does not have an id.
        """
        if not self.get(self.Field.id):
            raise FacebookBadObjectError(
                "%s object needs an id for this operation."
                % self.__class__.__name__,
            )

        return self.get_id()

    def get_parent_id_assured(self):
        """Returns the object's parent's fbid.

        Raises:
            FacebookBadObjectError if the object does not have a parent id.
        """
        if not self.get_parent_id():
            raise FacebookBadObjectError(
                "%s object needs a parent_id for this operation."
                % self.__class__.__name__,
            )

        return self.get_parent_id()

    def get_api_assured(self):
        """Returns the fbid of the object.

        Raises:
            FacebookBadObjectError if get_api returns None.
        """
        api = self.get_api()
        if not api:
            raise FacebookBadObjectError(
                "%s does not yet have an associated api object.\n"
                "Did you forget to instantiate an API session with: "
                "FacebookAdsApi.init(app_id, app_secret, access_token)"
                % self.__class__.__name__,
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
        for key in map(str, data):
            self._data[key] = data[key]

            # clear history due to the update
            self._changes.pop(key, None)

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
        api_version=None,
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
        if self.get_id():
            raise FacebookBadObjectError(
                "This %s object was already created."
                % self.__class__.__name__,
            )

        params = {} if not params else params.copy()
        params.update(self.export_data())

        if batch is not None:
            def callback_success(response):
                self._set_data(response.json())
                self._clear_history()

                if success:
                    success(response)

            def callback_failure(response):
                if failure:
                    failure(response)

            batch_call = batch.add(
                'POST',
                (self.get_parent_id_assured(), self.get_endpoint()),
                params=params,
                files=files,
                success=callback_success,
                failure=callback_failure,
            )
            return batch_call
        else:
            response = self.get_api_assured().call(
                'POST',
                (self.get_parent_id_assured(), self.get_endpoint()),
                params=params,
                files=files,
                api_version=api_version,
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
        api_version=None,
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

                if success:
                    success(response)

            def callback_failure(response):
                if failure:
                    failure(response)

            batch_call = batch.add(
                'GET',
                self.get_node_path(),
                params=params,
                success=callback_success,
                failure=callback_failure,
            )
            return batch_call
        else:
            response = self.get_api_assured().call(
                'GET',
                self.get_node_path(),
                params=params,
                api_version=api_version,
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
        api_version=None,
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
        params = {} if not params else params.copy()
        params.update(self.export_data())
        self._set_data(params)

        if batch is not None:
            def callback_success(response):
                self._clear_history()

                if success:
                    success(response)

            def callback_failure(response):
                if failure:
                    failure(response)

            batch_call = batch.add(
                'POST',
                self.get_node_path(),
                failure=callback_failure,
                files=files,
                params=params,
                success=callback_success,
            )
            return batch_call
        else:
            self.get_api_assured().call(
                'POST',
                self.get_node_path(),
                files=files,
                params=params,
                api_version=api_version,
            )
            self._clear_history()

            return self

    def remote_delete(
        self,
        batch=None,
        failure=None,
        params=None,
        success=None,
        api_version=None,
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

                if success:
                    success(response)

            def callback_failure(response):
                if failure:
                    failure(response)

            batch_call = batch.add(
                'DELETE',
                self.get_node_path(),
                params=params,
                success=callback_success,
                failure=callback_failure,
            )
            return batch_call
        else:
            self.get_api_assured().call(
                'DELETE',
                self.get_node_path(),
                params=params,
                api_version=api_version,
            )
            self.clear_id()

            return self

    # Helpers

    def remote_save(self, *args, **kwargs):
        """
        Calls remote_create method if object has not been created. Else, calls
        the remote_update method.
        """
        if self.get_id():
            return self.remote_update(*args, **kwargs)
        else:
            return self.remote_create(*args, **kwargs)

    # To avoid breaking change. Will be deprecated
    save = remote_save

    def iterate_edge(self, target_objects_class, fields=None, params=None,
                     fetch_first_page=True, include_summary=True):
        """
        Returns EdgeIterator with argument self as source_object and
        the rest as given __init__ arguments.

        Note: list(iterate_edge(...)) can prefetch all the objects.
        """
        source_object = self
        iterator = EdgeIterator(
            source_object,
            target_objects_class,
            fields=fields,
            params=params,
            include_summary=include_summary,
        )
        if fetch_first_page:
            iterator.load_next_page()
        return iterator

    def iterate_edge_async(self, target_objects_class, fields=None,
                           params=None, async=False, include_summary=True):
        """
        Behaves as iterate_edge(...) if parameter async if False
        (Default value)

        If async is True:
        Returns an AsyncJob which can be checked using remote_read()
        to verify when the job is completed and the result ready to query
        or download using get_result()

        Example:
        >>> job = object.iterate_edge_async(
                TargetClass, fields, params, async=True)
        >>> time.sleep(10)
        >>> job.remote_read()
        >>> if job:
                result = job.read_result()
                print result
        """
        synchronous = not async
        synchronous_iterator = self.iterate_edge(
            target_objects_class,
            fields,
            params,
            fetch_first_page=synchronous,
            include_summary=include_summary,
        )
        if synchronous:
            return synchronous_iterator

        if not params:
            params = {}
        else:
            params = dict(params)
        self.__class__._assign_fields_to_params(fields, params)

        # To force an async response from an edge, do a POST instead of GET.
        # The response comes in the format of an AsyncJob which
        # indicates the progress of the async request.
        response = self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), target_objects_class.get_endpoint()),
            params=params,
        ).json()

        # AsyncJob stores the real iterator
        # for when the result is ready to be queried
        result = AsyncJob(target_objects_class)

        if 'report_run_id' in response:
            response['id'] = response['report_run_id']
        result._set_data(response)
        return result

    def edge_object(self, target_objects_class, fields=None, params=None):
        """
        Returns first object when iterating over EdgeIterator with argument
        self as source_object and the rest as given __init__ arguments.
        """
        params = {} if not params else params.copy()
        params['limit'] = '1'
        for obj in self.iterate_edge(
            target_objects_class,
            fields=fields,
            params=params,
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
        """Returns iterator over AdAccounts associated with this user."""
        return self.iterate_edge(AdAccount, fields, params)

    def get_ad_account(self, fields=None, params=None):
        """Returns first AdAccount associated with this user."""
        return self.edge_object(AdAccount, fields, params)

    def get_pages(self, fields=None, params=None):
        """Returns iterator over Pages's associated with this user."""
        return self.iterate_edge(Page, fields, params)

    def get_ad_account_groups(self, fields=None, params=None):
        """Returns iterator over AdAccount Groups associated with this user."""
        return self.iterate_edge(AdAccountGroup, fields, params)


class Page(CannotCreate, CannotDelete, CannotUpdate, AbstractCrudObject):

    class Field(object):
        id = 'id'
        name = 'name'
        category = 'category'
        access_token = 'access_token'
        location = 'location'
        website = 'website'
        phone = 'phone'

    class Location(object):
        city = 'city'
        country = 'country'
        latitude = 'latitude'
        longitude = 'longitude'
        street = 'street'
        zip = 'zip'

    @classmethod
    def get_endpoint(cls):
        return 'accounts'

    def get_leadgen_forms(self, fields=None, params=None):
        """
        Returns all leadgen forms on the page
        """
        return self.iterate_edge(LeadgenForm, fields, params)


class Activity(AbstractObject):

    class Field(object):
        event_time = 'event_time'
        event_type = 'event_type'

    @classmethod
    def get_endpoint(cls):
        return 'activities'


class AdAccount(CannotCreate, CannotDelete, HasAdLabels, AbstractCrudObject):

    class Field(object):
        account_groups = 'account_groups'
        account_id = 'account_id'
        account_status = 'account_status'
        adlabels = 'adlabels'
        age = 'age'
        agency_client_declaration = 'agency_client_declaration'
        amount_spent = 'amount_spent'
        balance = 'balance'
        business = 'business'
        business_city = 'business_city'
        business_country_code = 'business_country_code'
        business_name = 'business_name'
        business_state = 'business_state'
        business_street = 'business_street'
        business_street2 = 'business_street2'
        business_zip = 'business_zip'
        capabilities = 'capabilities'
        currency = 'currency'
        end_advertiser = 'end_advertiser'
        funding_source = 'funding_source'
        funding_source_details = 'funding_source_details'
        id = 'id'
        is_personal = 'is_personal'
        media_agency = 'media_agency'
        name = 'name'
        offsite_pixels_tos_accepted = 'offsite_pixels_tos_accepted'
        owner = 'owner'
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

    def opt_out_user_from_targeting(self, schema, users, app_ids=None):
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
            params=CustomAudience.format_params(schema, users, app_ids),
        )

    def get_activities(self, fields=None, params=None):
        """Returns iterator over Activity's associated with this account."""
        return self.iterate_edge(Activity, fields, params)

    def get_ad_users(self, fields=None, params=None):
        """Returns iterator over AdUser's associated with this account."""
        return self.iterate_edge(AdUser, fields, params)

    def get_campaigns(self, fields=None, params=None):
        """Returns iterator over Campaign's associated with this account."""
        return self.iterate_edge(Campaign, fields, params)

    def get_ad_sets(self, fields=None, params=None):
        """Returns iterator over AdSet's associated with this account."""
        return self.iterate_edge(AdSet, fields, params)

    def get_ads(self, fields=None, params=None):
        """Returns iterator over Ad's associated with this account."""
        return self.iterate_edge(Ad, fields, params)

    def get_ad_conversion_pixels(self, fields=None, params=None):
        """
        Returns iterator over AdConversionPixels associated with this account.
        """
        return self.iterate_edge(AdConversionPixel, fields, params)

    def get_ad_creatives(self, fields=None, params=None):
        """Returns iterator over AdCreative's associated with this account."""
        return self.iterate_edge(AdCreative, fields, params)

    def get_ad_images(self, fields=None, params=None):
        """Returns iterator over AdImage's associated with this account."""
        return self.iterate_edge(AdImage, fields, params)

    def get_insights(self, fields=None, params=None, async=False):
        return self.iterate_edge_async(
            Insights,
            fields,
            params,
            async,
            include_summary=False,
        )

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

    def get_transactions(self, fields=None, params=None):
        """Returns iterator over Transaction's associated with this account."""
        return self.iterate_edge(Transaction, fields, params)

    def get_ad_preview(self, fields=None, params=None):
        """Returns iterator over previews generated under this account."""
        return self.iterate_edge(GeneratePreview, fields, params)

    def get_ads_pixels(self, fields=None, params=None):
        return self.edge_object(AdsPixel, fields, params)

    def get_targeting_description(self, fields=None, params=None):
        """
        Returns TargetingDescription object associated with this account.
        """
        return self.edge_object(TargetingDescription, fields, params)

    def get_ad_labels(self, fields=None, params=None):
        """
        Returns all the ad labels associated with the ad account
        """
        return self.iterate_edge(AdLabel, fields, params)

    def get_ad_creatives_by_labels(self, fields=None, params=None):
        """
        Returns the ad creatives associated with the ad AdLabel
        """
        return self.iterate_edge(AdCreativesByLabels, fields, params)

    def get_ads_by_labels(self, fields=None, params=None):
        """
        Returns the ad Groups associated with the ad AdLabel
        """
        return self.iterate_edge(AdsByLabels, fields, params)

    def get_adsets_by_labels(self, fields=None, params=None):
        """
        Returns the ad sets associated with the ad AdLabel
        """
        return self.iterate_edge(AdSetsByLabels, fields, params)

    def get_campaigns_by_labels(self, fields=None, params=None):
        """
        Returns the ad campaigns associated with the ad AdLabel
        """
        return self.iterate_edge(CampaignsByLabels, fields, params)

    def get_minimum_budgets(self, fields=None, params=None):
        """
        Returns the minimum budget associated with the AdAccount
        """
        return self.iterate_edge(MinimumBudget, fields, params)

    def get_ad_place_page_sets(self, fields=None, params=None):
        """
        Returns the ad place page sets associated with the AdAccount
        """
        return self.iterate_edge(AdPlacePageSet, fields, params)

    def get_custom_conversions(self, fields=None, params=None):
        """
        Returns the custom conversions associated with the AdAccount
        """
        return self.iterate_edge(CustomConversion, fields, params)


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


class AdAccountGroupAccount(AbstractObject):

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


class Campaign(CanValidate, HasStatus, HasObjective, HasAdLabels, CanArchive,
               AbstractCrudObject):

    class Field(object):
        account_id = 'account_id'
        adlabels = 'adlabels'
        buying_type = 'buying_type'
        configured_status = 'configured_status'
        effective_status = 'effective_status'
        id = 'id'
        is_completed = 'is_completed'
        name = 'name'
        objective = 'objective'
        promoted_object = 'promoted_object'
        spend_cap = 'spend_cap'
        start_time = 'start_time'
        stop_time = 'stop_time'
        updated_time = 'updated_time'

    class BuyingType(object):
        auction = 'AUCTION'
        fixed_price = 'FIXED_PRICE'
        reserved = 'RESERVED'

    @classmethod
    def get_endpoint(cls):
        return 'campaigns'

    def get_ad_sets(self, fields=None, params=None):
        """Returns iterator over AdSet's associated with this campaign."""
        return self.iterate_edge(AdSet, fields, params)

    def get_ads(self, fields=None, params=None):
        """Returns iterator over Ad's associated with this campaign."""
        return self.iterate_edge(Ad, fields, params)

    def get_insights(self, fields=None, params=None, async=False):
        return self.iterate_edge_async(
            Insights,
            fields,
            params,
            async,
            include_summary=False,
        )


class AdSet(CanValidate, HasStatus, CanArchive, HasAdLabels,
            AbstractCrudObject):

    class Field(HasBidInfo, object):
        account_id = 'account_id'
        adlabels = 'adlabels'
        bid_amount = 'bid_amount'
        bid_info = 'bid_info'
        billing_event = 'billing_event'
        budget_remaining = 'budget_remaining'
        campaign_id = 'campaign_id'
        adset_schedule = 'adset_schedule'
        configured_status = 'configured_status'
        created_time = 'created_time'
        creative_sequence = 'creative_sequence'
        daily_budget = 'daily_budget'
        effective_status = 'effective_status'
        end_time = 'end_time'
        id = 'id'
        is_autobid = 'is_autobid'
        lifetime_budget = 'lifetime_budget'
        lifetime_imps = 'lifetime_imps'
        name = 'name'
        optimization_goal = 'optimization_goal'
        product_ad_behavior = 'product_ad_behavior'
        pacing_type = 'pacing_type'
        promoted_object = 'promoted_object'
        rf_prediction_id = 'rf_prediction_id'
        rtb_flag = 'rtb_flag'
        start_time = 'start_time'
        targeting = 'targeting'
        updated_time = 'updated_time'

    class BillingEvent(object):
        app_installs = 'APP_INSTALLS'
        clicks = 'CLICKS'
        impressions = 'IMPRESSIONS'
        link_clicks = 'LINK_CLICKS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        video_views = 'VIDEO_VIEWS'

    class OptimizationGoal(object):
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        clicks = 'CLICKS'
        engaged_users = 'ENGAGED_USERS'
        event_responses = 'EVENT_RESPONSES'
        external = 'EXTERNAL'
        impressions = 'IMPRESSIONS'
        link_clicks = 'LINK_CLICKS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        offsite_conversions = 'OFFSITE_CONVERSIONS'
        page_engagement = 'PAGE_ENGAGEMENT'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        reach = 'REACH'
        social_impressions = 'SOCIAL_IMPRESSIONS'
        video_views = 'VIDEO_VIEWS'

    class PacingType(object):
        day_parting = 'day_parting'
        standard = 'standard'
        no_pacing = 'no_pacing'

    @classmethod
    def get_endpoint(cls):
        return 'adsets'

    def get_ads(self, fields=None, params=None):
        """Returns iterator over Ad's associated with this set."""
        return self.iterate_edge(Ad, fields, params)

    def get_ad_creatives(self, fields=None, params=None):
        """Returns iterator over AdCreative's associated with this set."""
        return self.iterate_edge(AdCreative, fields, params)

    def get_insights(self, fields=None, params=None, async=False):
        return self.iterate_edge_async(
            Insights,
            fields,
            params,
            async,
            include_summary=False,
        )


class Ad(HasStatus, CanArchive, HasAdLabels, AbstractCrudObject):

    class Field(HasBidInfo, object):
        account_id = 'account_id'
        ad_review_feedback = 'ad_review_feedback'
        adlabels = 'adlabels'
        adset_id = 'adset_id'
        bid_amount = 'bid_amount'
        bid_info = 'bid_info'
        campaign_id = 'campaign_id'
        configured_status = 'configured_status'
        conversion_specs = 'conversion_specs'
        created_time = 'created_time'
        creative = 'creative'
        effective_status = 'effective_status'
        failed_delivery_checks = 'failed_delivery_checks'
        id = 'id'
        name = 'name'
        redownload = 'redownload'
        social_prefs = 'social_prefs'
        tracking_specs = 'tracking_specs'
        updated_time = 'updated_time'
        view_tags = 'view_tags'

        class Creative(object):
            creative_id = 'creative_id'

    @classmethod
    def get_endpoint(cls):
        return 'ads'

    def get_ad_creatives(self, fields=None, params=None):
        """Returns iterator over AdCreatives associated with this ad."""
        return self.iterate_edge(AdCreative, fields, params)

    def get_targeting_description(self, fields=None, params=None):
        """Returns TargetingDescription object associated with this ad."""
        return self.edge_object(TargetingDescription, fields, params)

    def get_keyword_stats(self, fields=None, params=None):
        """Returns iterator over KeywordStats associated with this ad."""
        return self.edge_object(KeywordStats, fields, params)

    def get_ad_preview(self, fields=None, params=None):
        """Returns AdPreview object associated with this ad."""
        return self.edge_object(AdPreview, fields, params)

    def get_reach_estimate(self, fields=None, params=None):
        """Returns iterator over ReachEstimates associated with this ad."""
        return self.iterate_edge(ReachEstimate, fields, params)

    def get_click_tracking_tag(self, fields=None, params=None):
        """Returns iterator over ClickTrackingTags associated with this ad."""
        return self.iterate_edge(ClickTrackingTag, fields, params)

    def get_insights(self, fields=None, params=None, async=False):
        return self.iterate_edge_async(
            Insights,
            fields,
            params,
            async,
            include_summary=False,
        )

    def get_leads(self, fields=None, params=None):
        """
        Returns all the leads associated with the Ad
        """
        return self.iterate_edge(Lead, fields, params)


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


class AdsPixel(CannotUpdate, CannotDelete, AbstractCrudObject):

    class Field(object):
        audiences = 'audiences'
        code = 'code'
        id = 'id'
        last_fired_time = 'last_fired_time'
        name = 'name'
        owner_ad_account = 'owner_ad_account'

    def share_pixel_with_ad_account(self, business_id, account_id):
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'shared_accounts'),
            params={
                'business': business_id,
                'account_id': account_id,
            },
        )

    def share_pixel_with_agency(self, business_id, agency_id):
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'shared_agencies'),
            params={
                'business': business_id,
                'agency_id': agency_id,
            },
        )

    def get_ad_accounts(self, business_id):
        response = self.get_api_assured().call(
            'GET',
            (self.get_id_assured(), 'shared_accounts'),
            params={'business': business_id},
        ).json()

        ret_val = []
        if response:
            keys = response['data']
            for item in keys:
                search_obj = AdAccount()
                search_obj.update(item)
                ret_val.append(search_obj)
        return ret_val

    def get_agencies(self):
        response = self.get_api_assured().call(
            'GET',
            (self.get_id_assured(), 'shared_agencies'),
        ).json()

        ret_val = []
        if response:
            keys = response['data']
            for item in keys:
                search_obj = Business()
                search_obj.update(item)
                ret_val.append(search_obj)
        return ret_val

    def unshare_pixel_from_ad_account(self, business_id, account_id):
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'shared_accounts'),
            params={
                'business': business_id,
                'account_id': account_id,
            },
        )

    def unshare_pixel_from_agency(self, business_id, agency_id):
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'shared_agencies'),
            params={
                'business': business_id,
                'agency_id': agency_id,
            },
        )

    def get_stats(self, fields=None, params=None):
        """Returns iterator over Stats associated with this pixel."""
        return self.edge_object(AdsPixelStat, fields, params)

    @deprecated(replacement='unshare_pixel_from_ad_account')
    def unshare_pixel(self, business_id, account_id):
        return self.unshare_pixel_from_ad_account(business_id, account_id)

    @deprecated(replacement='unshare_pixel_from_agency')
    def unshare_pixel_agencies(self, business_id, agency_id):
        return self.unshare_pixel_from_agency(business_id, agency_id)

    @deprecated(replacement='share_pixel_with_ad_account')
    def share_pixel(self, business_id, account_id):
        return self.share_pixel_with_ad_account(business_id, account_id)

    @deprecated(replacement='share_pixel_with_agency')
    def share_pixel_agencies(self, business_id, agency_id):
        return self.share_pixel_with_agency(business_id, agency_id)

    @deprecated(replacement='get_ad_accounts')
    def list_ad_accounts(self, business_id):
        return self.get_ad_accounts(business_id)

    @deprecated(replacement='get_agencies')
    def list_shared_agencies(self):
        return self.get_agencies()

    @classmethod
    def get_endpoint(cls):
        return 'adspixels'


class AdCreative(HasAdLabels, AbstractCrudObject):

    class Field(object):
        actor_id = 'actor_id'
        actor_image_hash = 'actor_image_hash'
        actor_name = 'actor_name'
        adlabels = 'adlabels'
        applink_treatment = 'applink_treatment'
        body = 'body'
        call_to_action_type = 'call_to_action_type'
        dynamic_ad_voice = 'dynamic_ad_voice'
        filename = 'filename'
        follow_redirect = 'follow_redirect'
        id = 'id'
        image_crops = 'image_crops'
        image_file = 'image_file'
        image_hash = 'image_hash'
        image_url = 'image_url'
        instagram_actor_id = 'instagram_actor_id'
        instagram_permalink_url = 'instagram_permalink_url'
        link_deep_link_url = 'link_deep_link_url'
        link_url = 'link_url'
        name = 'name'
        object_id = 'object_id'
        object_store_url = 'object_store_url'
        object_story_id = 'object_story_id'
        object_story_spec = 'object_story_spec'
        object_type = 'object_type'
        object_url = 'object_url'
        place_page_set_id = 'place_page_set_id'
        preview_url = 'preview_url'
        product_set_id = 'product_set_id'
        template_url = 'template_url'
        thumbnail_url = 'thumbnail_url'
        title = 'title'
        url_tags = 'url_tags'
        video_id = 'video_id'

    @classmethod
    def get_endpoint(cls):
        return 'adcreatives'

    def get_ad_preview(self, fields=None, params=None):
        """
        Returns iterator over AdCreativePreviews associated with this creative.
        """
        return self.iterate_edge(AdCreativePreview, fields, params)


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

    @classmethod
    def remote_create_from_zip(cls, filename, parent_id, api=None):
        api = api or FacebookAdsApi.get_default_api()
        open_file = open(filename, 'rb')
        response = api.call(
            'POST',
            (parent_id, cls.get_endpoint()),
            files={filename: open_file},
        )
        open_file.close()

        data = response.json()

        objs = []
        for image_filename in data['images']:
            image = AdImage(parent_id=parent_id)
            image.update(data['images'][image_filename])
            image[cls.Field.id] = '%s:%s' % (
                parent_id[4:],
                data['images'][image_filename][cls.Field.hash],
            )
            objs.append(image)

        return objs

    def get_node_path(self):
        return (self.get_parent_id_assured(), self.get_endpoint())

    def _set_data(self, data):
        """
            `data` may have a different structure depending if you're creating
            new AdImages or iterating over existing ones using something like
            AdAccount.get_ad_images().

            While reading existing images, _set_data from AbstractCrudObject
            handles everything correctly, but we need to treat the
            remote_create case.

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

        if 'images' in data:
            _, data = data['images'].popitem()

            for key in map(str, data):
                self._data[key] = data[key]

                # clear history due to the update
                self._changes.pop(key, None)

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
        api_version=None,
    ):
        """Uploads filename and creates the AdImage object from it.

        It has same arguments as AbstractCrudObject.remote_create except it
        does not have the files argument but requires the 'filename' property
        to be defined.
        """
        if not self[self.Field.filename]:
            raise FacebookBadObjectError(
                "AdImage required a filename to be defined.",
            )
        filename = self[self.Field.filename]
        with open(filename, 'rb') as open_file:
            return_val = super(AdImage, self).remote_create(
                files={filename: open_file},
                batch=batch,
                failure=failure,
                params=params,
                success=success,
                api_version=api_version,
            )
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
        api_version=None,
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


class AdVideo(AbstractCrudObject):

    class Field(object):
        filepath = 'filepath'
        id = 'id'
        slideshow_spec = 'slideshow_spec'

    def remote_create(
        self,
        batch=None,
        failure=None,
        params=None,
        success=None,
    ):
        """
        Uploads filepath and creates the AdVideo object from it.
        It has same arguments as AbstractCrudObject.remote_create except it
        does not have the files argument but requires the 'filepath' property
        to be defined.
        """
        if self.Field.slideshow_spec in self:
            request = VideoUploadRequest(self.get_api_assured())
            spec = self[self.Field.slideshow_spec]
            print(spec)
            request.setParams(params={'slideshow_spec': {
                'images_urls': self[self.Field.slideshow_spec]['images_urls'],
                'duration_ms': self[self.Field.slideshow_spec]['duration_ms'],
                'transition_ms': self[self.Field.slideshow_spec]['transition_ms'],
            }})
            request.send((self.get_parent_id_assured(), 'advideos'))
            exit()
        elif not (self.Field.filepath in self):
            raise FacebookBadObjectError(
                "AdVideo requires a filepath or slideshow_spec to be defined.",
            )
        video_uploader = VideoUploader()
        response = video_uploader.upload(self)
        self._set_data(response)
        return response

    def waitUntilEncodingReady(self, interval=30, timeout=600):
        if 'id' not in self:
            raise FacebookError(
                'Invalid Video ID',
            )
        VideoEncodingStatusChecker.waitUntilReady(
            self.get_api_assured(),
            self['id'],
            interval,
            timeout,
        )

    def get_thumbnails(self, fields=None, params=None):
        """
        Returns all the thumbnails associated with the ad video
        """
        return self.iterate_edge(VideoThumbnail, fields, params)


class VideoThumbnail(AbstractObject):

    class Field(object):
        id = 'id'
        height = 'height'
        name = 'name'
        scale = 'scale'
        uri = 'uri'
        width = 'width'
        is_preferred = 'is_preferred'

    @classmethod
    def get_endpoint(cls):
        return 'thumbnails'


class GeneratePreview(AbstractObject):

    class Field(object):
        ad_format = 'ad_format'
        body = 'body'
        creative = 'creative'
        post = 'post'
        product_item_ids = 'product_item_ids'

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


class AdCreativePreview(GeneratePreview):

    @classmethod
    def get_endpoint(cls):
        return 'previews'


class AdPreview(AdCreativePreview):

    @classmethod
    def get_endpoint(cls):
        return 'previews'


class AdsPixelStat(AbstractObject):

    class Field(object):
        aggregation = 'aggregation'
        end_time = 'end_time'
        start_time = 'start_time'

    class Aggregation(object):
        browser_type = 'browser_type'
        custom_data_field = 'custom_data_field'
        device_os = 'device_os'
        device_type = 'device_type'
        event = 'event'
        host = 'host'
        pixel_fire = 'pixel_fire'
        url = 'url'

    @classmethod
    def get_endpoint(cls):
        return 'stats'


class KeywordStats(AbstractObject):

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
        ad_id = 'ad_id'
        id = 'id'
        url = 'url'

    @classmethod
    def get_endpoint(cls):
        return 'trackingtag'

    def get_node_path(self):
        return (
            self.get_parent_id_assured(),
            self.get_endpoint()
        )

    def remote_delete(self, params=None):
        return self.get_api_assured().call(
            'DELETE',
            self.get_node_path(),
            params=params,
        )


class CustomAudience(AbstractCrudObject):

    class Field(object):
        account_id = 'account_id'
        approximate_count = 'approximate_count'
        data_source = 'data_source'
        delivery_status = 'delivery_status'
        description = 'description'
        force_delete_lookalikes = 'force_delete_lookalikes'
        id = 'id'
        pixel_id = 'pixel_id'
        lookalike_audience_ids = 'lookalike_audience_ids'
        lookalike_spec = 'lookalike_spec'
        name = 'name'
        operation_status = 'operation_status'
        opt_out_link = 'opt_out_link'
        origin_audience_id = 'origin_audience_id'
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

        class MultiKeySchema(object):
            email = 'EMAIL'
            phone = 'PHONE'
            gen = 'GEN'
            doby = 'DOBY'
            dobm = 'DOBM'
            dobd = 'DOBD'
            ln = 'LN'
            fn = 'FN'
            fi = 'FI'
            ct = 'CT'
            st = 'ST'
            zip = 'ZIP'
            madid = 'MADID'

    class Subtype(object):
        custom = 'CUSTOM'
        lookalike = 'LOOKALIKE'
        website = 'WEBSITE'
        app = 'APP'
        partner = 'PARTNER'
        managed = 'MANAGED'
        video = 'VIDEO'
        app_combination = 'APP_COMBINATION'

    @classmethod
    def get_endpoint(cls):
        return 'customaudiences'

    @classmethod
    def format_params(cls,
                      schema,
                      users,
                      is_raw=False,
                      app_ids=None,
                      pre_hashed=None):
        hashed_users = []
        if schema in (cls.Schema.phone_hash,
                      cls.Schema.email_hash,
                      cls.Schema.mobile_advertiser_id):
            for user in users:
                if schema == cls.Schema.email_hash:
                    user = user.strip(" \t\r\n\0\x0B.").lower()
                if isinstance(user, six.text_type) and not(pre_hashed):
                    user = user.encode('utf8')  # required for hashlib
                if pre_hashed:
                    hashed_users.append(user)
                else:
                    hashed_users.append(hashlib.sha256(user).hexdigest())
        elif isinstance(schema, list):
            # SDK will support only single PII
            if not is_raw:
                raise FacebookBadObjectError(
                    "Please send single PIIs i.e. is_raw should be true. " +
                    "The combining of the keys will be done internally.",
                )
            # users is array of array
            for user in users:
                if len(schema) != len(user):
                    raise FacebookBadObjectError(
                        "Number of keys in each list in the data should " +
                        "match the number of keys specified in scheme",
                    )
                    break

                # If the keys are already hashed then send as it is
                if pre_hashed:
                    hashed_users.append(user)
                else:
                    counter = 0
                    hashed_user = []
                    for key in user:
                        key = key.strip(" \t\r\n\0\x0B.").lower()
                        key = CustomAudience.normalize_key(schema[counter],
                                                           str(key))
                        if isinstance(key, six.text_type):
                            key = key.encode('utf8')
                        key = hashlib.sha256(key).hexdigest()
                        counter = counter + 1
                        hashed_user.append(key)
                    hashed_users.append(hashed_user)

        payload = {
            'schema': schema,
            'is_raw': is_raw,
            'data': hashed_users or users,
        }

        if schema == cls.Schema.uid:
            if not app_ids:
                raise FacebookBadObjectError(
                    "Custom Audiences with type " + cls.Schema.uid +
                    "require at least one app_id",
                )
            payload['app_ids'] = app_ids

        return {
            'payload': payload,
        }

    @classmethod
    def normalize_key(cls, key_name, key_value=None):
        """
            Normalize the value based on the key
        """
        if key_value is None:
            return key_value

        if(key_name == CustomAudience.Schema.MultiKeySchema.email or
           key_name == CustomAudience.Schema.MultiKeySchema.madid):
            return key_value

        if(key_name == CustomAudience.Schema.MultiKeySchema.phone):
            key_value = re.sub(r'[^0-9]', '', key_value)
            return key_value

        if(key_name == CustomAudience.Schema.MultiKeySchema.gen):
            key_value = key_value.strip()[:1]
            return key_value

        if(key_name == CustomAudience.Schema.MultiKeySchema.doby):
            key_value = re.sub(r'[^0-9]', '', key_value)
            return key_value

        if(key_name == CustomAudience.Schema.MultiKeySchema.dobm or
           key_name == CustomAudience.Schema.MultiKeySchema.dobd):

            key_value = re.sub(r'[^0-9]', '', key_value)
            if len(key_value) == 1:
                key_value = '0' + key_value
            return key_value

        if(key_name == CustomAudience.Schema.MultiKeySchema.ln or
           key_name == CustomAudience.Schema.MultiKeySchema.fn or
           key_name == CustomAudience.Schema.MultiKeySchema.ct or
           key_name == CustomAudience.Schema.MultiKeySchema.fi or
           key_name == CustomAudience.Schema.MultiKeySchema.st):
            key_value = re.sub(r'[^a-zA-Z]', '', key_value)
            return key_value

        if(key_name == CustomAudience.Schema.MultiKeySchema.zip):
            key_value = re.split('-', key_value)[0]
            return key_value

    def add_users(self,
                  schema,
                  users,
                  is_raw=False,
                  app_ids=None,
                  pre_hashed=None):
        """Adds users to this CustomAudience.

        Args:
            schema: A CustomAudience.Schema value specifying the type of values
                in the users list.
            users: A list of identities respecting the schema specified.

        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'users'),
            params=CustomAudience.format_params(schema,
                                                users,
                                                is_raw,
                                                app_ids,
                                                pre_hashed,
                                                ),
        )

    def remove_users(self,
                     schema,
                     users,
                     is_raw=False,
                     app_ids=None,
                     pre_hashed=None):
        """Deletes users from this CustomAudience.

        Args:
            schema: A CustomAudience.Schema value specifying the type of values
                in the users list.
            users: A list of identities respecting the schema specified.

        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'users'),
            params=CustomAudience.format_params(schema,
                                                users,
                                                is_raw,
                                                app_ids,
                                                pre_hashed,
                                                ),
        )

    def share_audience(self, account_ids):
        """Shares this CustomAudience with the specified account_ids.

        Args:
            account_ids: A list of account ids.

        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            'POST',
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
            'DELETE',
            (self.get_id_assured(), 'adaccounts'),
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
        id = 'id'
        lookalike_spec = 'lookalike_spec'
        name = 'name'
        origin_audience_id = 'origin_audience_id'

        class LookalikeSpec(object):
            type = 'type'
            ratio = 'ratio'
            starting_ratio = 'starting_ratio'
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

    class Field(object):
        country = "country"
        currency = "currency"
        rate = "rate"

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
            'POST',
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
            'POST',
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
        country = 'adcountry'
        education = 'adeducationschool'
        employer = 'adworkemployer'
        geolocation = 'adgeolocation'
        geometadata = 'adgeolocationmeta'
        interest = 'adinterest'
        interest_suggestion = 'adinterestsuggestion'
        interest_validate = 'adinterestvalid'
        keyword = 'adkeyword'
        locale = 'adlocale'
        major = 'adeducationmajor'
        position = 'adworkposition'
        radius_suggestion = 'adradiussuggestion'
        targeting_category = 'adtargetingcategory'
        zipcode = 'adzipcode'

    @classmethod
    def search(cls, params=None, api=None):
        api = api or FacebookAdsApi.get_default_api()
        if not api:
            raise FacebookBadObjectError(
                "An Api instance must be provided as an argument or set as "
                "the default Api in FacebookAdsApi.",
            )

        params = {} if not params else params.copy()
        response = api.call(
            FacebookAdsApi.HTTP_METHOD_GET,
            "/".join((
                FacebookSession.GRAPH,
                FacebookAdsApi.API_VERSION,
                'search'
            )),
            params,
        ).json()

        ret_val = []
        if response:
            keys = response['data']
            # The response object can be either a dictionary of dictionaries
            # or a dictionary of lists.
            if isinstance(keys, list):
                for item in keys:
                    search_obj = TargetingSearch()
                    search_obj.update(item)
                    ret_val.append(search_obj)
            elif isinstance(keys, dict):
                for item in keys:
                    search_obj = TargetingSearch()
                    search_obj.update(keys[item])
                    if keys[item]:
                        ret_val.append(search_obj)
        return ret_val


class TargetingSpecsField(object):

    age_max = 'age_max'
    age_min = 'age_min'
    behaviors = 'behaviors'
    cities = 'cities'
    college_years = 'college_years'
    conjunctive_user_adclusters = 'conjunctive_user_adclusters'
    connections = 'connections'
    countries = 'countries'
    custom_audiences = 'custom_audiences'
    dynamic_audience_ids = 'dynamic_audience_ids'
    education_majors = 'education_majors'
    education_schools = 'education_schools'
    education_statuses = 'education_statuses'
    ethnic_affinity = 'ethnic_affinity'
    excluded_connections = 'excluded_connections'
    excluded_custom_audiences = 'excluded_custom_audiences'
    excluded_geo_locations = 'excluded_geo_locations'
    excluded_product_audience_specs = 'excluded_product_audience_specs'
    excluded_user_adclusters = 'excluded_user_adclusters'
    family_statuses = 'family_statuses'
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
    product_audience_specs = 'product_audience_specs'
    regions = 'regions'
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


class Business(CannotCreate, CannotDelete, AbstractCrudObject):

    class Field(object):
        created_by = 'created_by'
        creation_time = 'creation_time'
        id = 'id'
        name = 'name'
        primary_page = 'primary_page'
        timezone_id = 'timezone_id'
        update_time = 'update_time'
        updated_by = 'updated_by'
        vertical_id = 'vertical_id'

    def get_product_catalogs(self, fields=None, params=None):
        return self.iterate_edge(ProductCatalog, fields, params)

    def get_insights(self, fields=None, params=None, async=False):
        return self.iterate_edge_async(
            Insights,
            fields,
            params,
            async,
            include_summary=False,
        )


class ProductCatalog(AbstractCrudObject):

    class Field(object):
        id = 'id'
        name = 'name'

    class Role(object):
        admin = 'ADMIN'

    class Availability(object):
        available_for_order = 'available for order'
        in_stock = 'in stock'
        out_of_stock = 'out of stock'
        preorder = 'preorder'

    class AgeGroup(object):
        adult = 'adult'
        infant = 'infant'
        kids = 'kids'
        newborn = 'newborn'
        toddler = 'toddler'

    class Gender(object):
        men = 'men'
        women = 'women'
        unisex = 'unisex'

    class Condition(object):
        new = 'new'
        refurbished = 'refurbished'
        used = 'used'

    @classmethod
    def get_endpoint(cls):
        return 'product_catalogs'

    def get_product_feeds(self, fields=None, params=None):
        return self.iterate_edge(ProductFeed, fields, params)

    def get_product_sets(self, fields=None, params=None):
        return self.iterate_edge(ProductSet, fields, params)

    def add_user(self, user, role):
        params = {
            'user': user,
            'role': role,
        }
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'userpermissions'),
            params=params,
        )

    def remove_user(self, user):
        params = {
            'user': user,
        }
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'userpermissions'),
            params=params,
        )

    def add_external_event_sources(self, pixel_ids):
        params = {
            'external_event_sources': pixel_ids,
        }
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'external_event_sources'),
            params=params,
        )

    def remove_external_event_sources(self, pixel_ids):
        params = {
            'external_event_sources': pixel_ids,
        }
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'external_event_sources'),
            params=params,
        )

    def get_external_event_sources(self, fields=None, params=None):
        return self.iterate_edge(
            ProductCatalogExternalEventSource,
            fields,
            params,
        )

    def get_products(self, fields=None, params=None):
        """get products in a product catalog

        Args:
            fields:
                list of fields of ProductItem
            params:
                filter:
                    JSON Filter Specification for filter products
        """
        return self.iterate_edge(Product, fields, params)

    def update_product(self, retailer_id, **kwargs):
        """Updates a product stored in a product catalog

        Args:
            retailer_id: product id from product feed. g:price tag in Google
                Shopping feed
            kwargs: key-value pairs to update on the object, being key the
                field name and value the updated value

        Returns:
            The FacebookResponse object.
        """
        if not kwargs:
            raise FacebookError(
                """No fields to update provided. Example:
                   catalog = ProductCatalog('catalog_id')
                   catalog.update_product(
                       retailer_id,
                       price=100,
                       availability=Product.Availability.out_of_stock
                   )
                """,
            )

        product_endpoint = ':'.join((
            'catalog',
            self.get_id_assured(),
            self.b64_encoded_id(retailer_id),
        ))

        url = '/'.join((
            FacebookSession.GRAPH,
            FacebookAdsApi.API_VERSION,
            product_endpoint,
        ))

        return self.get_api_assured().call(
            'POST',
            url,
            params=kwargs,
        )

    def b64_encoded_id(self, retailer_id):
        # # we need a byte string for base64.b64encode argument
        b64_id = base64.urlsafe_b64encode(retailer_id.encode('utf8'))

        # and we need a str to join with other url snippets
        return b64_id.decode('utf8')


class ProductCatalogExternalEventSource(
    CannotCreate,
    CannotDelete,
    CannotUpdate,
    AbstractObject
):

    @classmethod
    def get_endpoint(cls):
        return 'external_event_sources'


class ProductFeed(AbstractCrudObject):

    class Field(object):
        country = 'country'
        delimiter = 'delimiter'
        encoding = 'encoding'
        file_name = 'file_name'
        format = 'format'
        id = 'id'
        name = 'name'
        quotes = 'quotes'
        schedule = 'schedule'

    class Format(object):
        tsv = 'TSV'
        xml = 'XML'

    class Encoding(object):
        ascii = 'ASCII'
        autodetect = 'AUTODETECT'
        latin_1 = 'LATIN_1'
        utf_16 = 'UTF_16'
        utf_8 = 'UTF_8'

    class Delimiter(object):
        pipe = 'PIPE'
        tab = 'TAB'
        tilde = 'TILDE'

    @classmethod
    def get_endpoint(cls):
        return 'product_feeds'

    def get_products(self, fields=None, params=None):
        return self.iterate_edge(Product, fields, params)


class ProductFeedUpload(AbstractCrudObject):

    class Field(object):
        end_time = 'end_time'
        id = 'id'
        start_time = 'start_time'

    @classmethod
    def get_endpoint(cls):
        return 'uploads'

    def get_errors(self, fields=None, params=None):
        return self.iterate_edge(ProductFeedUploadError, fields, params)


class ProductFeedUploadError(AbstractCrudObject):

    class Field(object):
        column_number = 'column_number'
        description = 'description'
        id = 'id'
        row_number = 'row_number'
        severity = 'severity'
        summary = 'summary'

    @classmethod
    def get_endpoint(cls):
        return 'errors'


class ProductSet(AbstractCrudObject):

    class Field(object):
        filter = 'filter'
        id = 'id'
        name = 'name'

    @classmethod
    def get_endpoint(cls):
        return 'product_sets'

    def get_product_groups(self, fields=None, params=None):
        return self.iterate_edge(ProductGroup, fields, params)

    def get_products(self, fields=None, params=None):
        return self.iterate_edge(Product, fields, params)


class ProductGroup(AbstractCrudObject):

    class Field(object):
        id = 'id'

    @classmethod
    def get_endpoint(cls):
        return 'product_groups'


class Product(AbstractCrudObject):

    class Field(object):
        additional_image_link = 'additional_image_link'
        age_group = 'age_group'
        availability = 'availability'
        brand = 'brand'
        color = 'color'
        condition = 'condition'
        description = 'description'
        expiration_date = 'expiration_date'
        gender = 'gender'
        google_product_category = 'google_product_category'
        gtin = 'gtin'
        id = 'id'
        image_link = 'image_link'
        item_group_id = 'item_group_id'
        link = 'link'
        material = 'material'
        mpn = 'mpn'
        name = 'name'
        pattern = 'pattern'
        price = 'price'
        product_type = 'product_type'
        retailer_id = 'retailer_id'
        sale_price = 'sale_price'
        sale_price_effective_date = 'sale_price_effective_date'
        shipping = 'shipping'
        shipping_size = 'shipping_size'
        shipping_weight = 'shipping_weight'
        title = 'title'
        url = 'url'

    class Availability(object):
        in_stock = 'IN_STOCK'
        out_of_stock = 'OUT_OF_STOCK'
        preorder = 'PREORDER'

    class Condition(object):
        new = 'PC_NEW'
        refurbished = 'PC_REFURBISHED'
        used = 'PC_USED'

    @classmethod
    def get_endpoint(cls):
        return 'products'


class ProductAudience(AbstractCrudObject):

    class Field(object):
        description = 'description'
        exclusions = 'exclusions'
        id = 'id'
        inclusions = 'inclusions'
        name = 'name'
        pixel_id = 'pixel_id'
        product_set_id = 'product_set_id'

    @classmethod
    def get_endpoint(cls):
        return 'product_audiences'


class Insights(CannotCreate, CannotDelete, CannotUpdate, AbstractCrudObject):
    class Field(object):
        account_id = 'account_id'
        account_name = 'account_name'
        action_values = 'action_values'
        actions = 'actions'
        actions_per_impression = 'actions_per_impression'
        ad_id = 'ad_id'
        ad_name = 'ad_name'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        async_percent_completion = 'async_percent_completion'
        async_status = 'async_status'
        call_to_action_clicks = 'call_to_action_clicks'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        cost_per_action_type = 'cost_per_action_type'
        cost_per_inline_link_click = 'cost_per_inline_link_click'
        cost_per_inline_post_engagement = 'cost_per_inline_post_engagement'
        cost_per_total_action = 'cost_per_total_action'
        cost_per_unique_click = 'cost_per_unique_click'
        cpm = 'cpm'
        cpp = 'cpp'
        ctr = 'ctr'
        date_start = 'date_start'
        date_stop = 'date_stop'
        frequency = 'frequency'
        id = 'id'
        impressions = 'impressions'
        inline_link_clicks = 'inline_link_clicks'
        inline_post_engagement = 'inline_post_engagement'
        product_id = 'product_id'
        reach = 'reach'
        relevance_score = 'relevance_score'
        report_run_id = 'report_run_id'
        social_clicks = 'social_clicks'
        social_impressions = 'social_impressions'
        social_reach = 'social_reach'
        spend = 'spend'
        total_action_value = 'total_action_value'
        total_actions = 'total_actions'
        total_unique_actions = 'total_unique_actions'
        unique_clicks = 'unique_clicks'
        unique_ctr = 'unique_ctr'
        unique_social_clicks = 'unique_social_clicks'
        video_avg_pct_watched_actions = 'video_avg_pct_watched_actions'
        video_avg_sec_watched_actions = 'video_avg_sec_watched_actions'
        video_complete_watched_actions = 'video_complete_watched_actions'
        video_p100_watched_actions = 'video_p100_watched_actions'
        video_p25_watched_actions = 'video_p25_watched_actions'
        video_p50_watched_actions = 'video_p50_watched_actions'
        video_p75_watched_actions = 'video_p75_watched_actions'
        video_p95_watched_actions = 'video_p95_watched_actions'
        website_ctr = 'website_ctr'

    @classmethod
    def get_endpoint(cls):
        return 'insights'

    class Preset(object):
        last_14_days = 'last_14_days'
        last_28_days = 'last_28_days'
        last_30_days = 'last_30_days'
        last_3_months = 'last_3_months'
        last_7_days = 'last_7_days'
        last_90_days = 'last_90_days'
        last_month = 'last_month'
        last_week = 'last_week'
        this_month = 'this_month'
        this_quarter = 'this_quarter'
        this_week = 'this_week'
        today = 'today'
        yesterday = 'yesterday'

    class Increment(object):
        monthly = 'monthly'
        all_days = 'all_days'

    class Breakdown(object):
        age = 'age'
        country = 'country'
        gender = 'gender'
        hourly_stats_aggregated_by_advertiser_time_zone = \
            'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = \
            'hourly_stats_aggregated_by_audience_time_zone'
        impression_device = 'impression_device'
        place_page_id = 'place_page_id'
        placement = 'placement'

    class Level(object):
        account = 'account'
        ad = 'ad'
        adset = 'adset'
        campaign = 'campaign'

    class ActionBreakdown(object):
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_target_id = 'action_target_id'
        action_type = 'action_type'
        action_video_type = 'action_video_type'

    class ActionAttributionWindow(object):
        click_1d = '1d_click'
        view_1d = '1d_view'
        click_28d = '28d_click'
        view_28d = '28d_view'
        click_7d = '7d_click'
        view_7d = '7d_view'
        default = 'default'

    class Operator(object):
        all = 'all'
        any = 'any'
        contain = 'contain'
        equal = 'equal'
        greater_than = 'greater_than'
        greater_than_or_equal = 'greater_than_or_equal'
        in_ = 'in'
        in_range = 'in_range'
        less_than = 'less_than'
        less_than_or_equal = 'less_than_or_equal'
        none = 'none'
        not_contain = 'not_contain'
        not_equal = 'not_equal'
        not_in = 'not_in'
        not_in_range = 'not_in_range'

    class ActionReportTime(object):
        conversion = 'conversion'
        impression = 'impression'


class AdLabel(AbstractCrudObject):

    class Field(object):
        id = 'id'
        name = 'name'

    @classmethod
    def get_endpoint(cls):
        return 'adlabels'


class AdsByLabels(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'adsbylabels'


class AdCreativesByLabels(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'adcreativesbylabels'


class AdSetsByLabels(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'adsetsbylabels'


class CampaignsByLabels(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'campaignsbylabels'


class Lead(AbstractCrudObject):

    class Field(object):
        Ad_id = 'ad_id'
        created_time = 'created_time'
        field_data = 'field_data'
        form_id = 'form_id'
        id = 'id'

    @classmethod
    def get_endpoint(cls):
        return 'leads'


class LeadgenForm(AbstractCrudObject):

    class Field(object):
        created_time = 'created_time'
        customized_tcpa_content = 'customized_tcpa_content'
        follow_up_action_text = 'follow_up_action_text'
        follow_up_action_url = 'follow_up_action_url'
        id = 'id'
        leadgen_export_csv_url = 'leadgen_export_csv_url'
        leads = 'leads'
        locale = 'locale'
        name = 'name'
        privacy_policy_url = 'privacy_policy_url'
        tcpa_compliance = 'tcpa_compliance'

    @classmethod
    def get_endpoint(cls):
        return 'leadgen_forms'

    def get_leads(self, fields=None, params=None):
        """
        Returns all the leads associated with the ad leadgen form
        """
        return self.iterate_edge(Lead, fields, params)


class MinimumBudget(AbstractObject):

    class Field(object):
        currency = 'currency'
        min_daily_budget_imp = 'min_daily_budget_imp'
        min_daily_budget_high_freq = 'min_daily_budget_high_freq'
        min_daily_budget_low_freq = 'min_daily_budget_low_freq'

    @classmethod
    def get_endpoint(cls):
        return 'minimum_budgets'


class AsyncJob(CannotCreate, AbstractCrudObject):

    class Field(object):
        id = 'id'
        async_status = 'async_status'
        async_percent_completion = 'async_percent_completion'

    def __init__(self, target_objects_class):
        AbstractCrudObject.__init__(self)
        self.target_objects_class = target_objects_class

    def get_result(self, params=None):
        """
        Gets the final result from an async job
        Accepts params such as limit
        """
        return self.iterate_edge(
            self.target_objects_class,
            params=params,
            include_summary=False,
        )

    def __nonzero__(self):
        return self[self.Field.async_percent_completion] == 100


class AdPlacePageSet(CannotDelete, AbstractCrudObject):

    class Field(object):
        account_id = 'account_id'
        id = 'id'
        name = 'name'
        pages_count = 'pages_count'
        parent_page = 'parent_page'

    @classmethod
    def get_endpoint(cls):
        return 'ad_place_page_sets'


class CustomConversion(CannotDelete, AbstractCrudObject):

    class Field(object):
        custom_event_type = 'custom_event_type'
        description = 'description'
        id = 'id'
        name = 'name'
        pixel_id = 'pixel_id'
        pixel_rule = 'pixel_rule'

    @classmethod
    def get_endpoint(cls):
        return 'customconversions'
