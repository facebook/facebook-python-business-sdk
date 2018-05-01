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
mixins contains attributes that objects share
"""

from facebook_business.exceptions import FacebookBadObjectError


class CanValidate(object):
    """
    An instance of CanValidate will allow the ad objects
    to call remote_validate() to verify if its parameters are valid
    """
    def remote_validate(self, params=None):
        params = params or {}
        data_cache = dict(self._data)
        changes_cache = dict(self._changes)
        params['execution_options'] = ['validate_only']
        self.save(params=params)
        self._data = data_cache
        self._changes = changes_cache
        return self


class CanArchive(object):

    """
    An instance of CanArchive will allow the ad objects
    to call remote_delete() to be deleted using a POST request against
    the object's status field.
    """
    def remote_delete(
        self,
        batch=None,
        failure=None,
        success=None
    ):
        return self.remote_update(
            params={
                'status': self.Status.deleted,
            },
            batch=batch,
            failure=failure,
            success=success,
        )

    """
    An instance of CanArchive will allow the ad objects
    to call remote_archive() to be archived
    """
    def remote_archive(
        self,
        batch=None,
        failure=None,
        success=None
    ):
        return self.remote_update(
            params={
                'status': self.Status.archived,
            },
            batch=batch,
            failure=failure,
            success=success,
        )


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


class HasObjective(object):

    """
    An instance of HasObjective will have an enum attribute Objective.
    """

    class Objective(object):
        brand_awareness = 'BRAND_AWARENESS'
        canvas_app_engagement = 'CANVAS_APP_ENGAGEMENT'
        canvas_app_installs = 'CANVAS_APP_INSTALLS'
        event_responses = 'EVENT_RESPONSES'
        lead_generation = 'LEAD_GENERATION'
        local_awareness = 'LOCAL_AWARENESS'
        mobile_app_engagement = 'MOBILE_APP_ENGAGEMENT'
        mobile_app_installs = 'MOBILE_APP_INSTALLS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        link_clicks = 'LINK_CLICKS'
        conversions = 'CONVERSIONS'
        video_views = 'VIDEO_VIEWS'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'


class HasStatus(object):

    """
    An instance of HasStatus will have an enum attribute Status.
    """

    class Status(object):
        active = 'ACTIVE'
        archived = 'ARCHIVED'
        deleted = 'DELETED'
        paused = 'PAUSED'


class HasBidInfo(object):

    """
    An instance of HasBidInfo will have an enum attribute BidInfo.
    """

    class BidInfo(object):
        actions = 'ACTIONS'
        clicks = 'CLICKS'
        impressions = 'IMPRESSIONS'
        reach = 'REACH'
        social = 'SOCIAL'


class HasAdLabels(object):

    def add_labels(self, labels=None):
        """Adds labels to an ad object.
        Args:
            labels: A list of ad label IDs
        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'adlabels'),
            params={'adlabels': [{'id': label} for label in labels]},
        )

    def remove_labels(self, labels=None):
        """Remove labels to an ad object.
        Args:
            labels: A list of ad label IDs
        Returns:
            The FacebookResponse object.
        """
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'adlabels'),
            params={'adlabels': [{'id': label} for label in labels]},
        )


class ValidatesFields(object):
    def __setitem__(self, key, value):
        if key not in self.Field.__dict__:
            raise FacebookBadObjectError(
                "\"%s\" is not a valid field of %s"
                % (key, self.__class__.__name__)
            )
        else:
            super(ValidatesFields, self).__setitem__(key, value)
