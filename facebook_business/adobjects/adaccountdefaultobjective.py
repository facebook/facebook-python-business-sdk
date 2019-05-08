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

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAccountDefaultObjective(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdAccountDefaultObjective, self).__init__()
        self._isAdAccountDefaultObjective = True
        self._api = api

    class Field(AbstractObject.Field):
        default_objective_for_user = 'default_objective_for_user'
        objective_for_level = 'objective_for_level'

    class DefaultObjectiveForUser:
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        canvas_app_engagement = 'CANVAS_APP_ENGAGEMENT'
        canvas_app_installs = 'CANVAS_APP_INSTALLS'
        event_responses = 'EVENT_RESPONSES'
        lead_generation = 'LEAD_GENERATION'
        link_clicks = 'LINK_CLICKS'
        local_awareness = 'LOCAL_AWARENESS'
        messages = 'MESSAGES'
        mobile_app_engagement = 'MOBILE_APP_ENGAGEMENT'
        mobile_app_installs = 'MOBILE_APP_INSTALLS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'
        video_views = 'VIDEO_VIEWS'
        website_conversions = 'WEBSITE_CONVERSIONS'

    class ObjectiveForLevel:
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        canvas_app_engagement = 'CANVAS_APP_ENGAGEMENT'
        canvas_app_installs = 'CANVAS_APP_INSTALLS'
        event_responses = 'EVENT_RESPONSES'
        lead_generation = 'LEAD_GENERATION'
        link_clicks = 'LINK_CLICKS'
        local_awareness = 'LOCAL_AWARENESS'
        messages = 'MESSAGES'
        mobile_app_engagement = 'MOBILE_APP_ENGAGEMENT'
        mobile_app_installs = 'MOBILE_APP_INSTALLS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'
        video_views = 'VIDEO_VIEWS'
        website_conversions = 'WEBSITE_CONVERSIONS'

    _field_types = {
        'default_objective_for_user': 'DefaultObjectiveForUser',
        'objective_for_level': 'ObjectiveForLevel',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DefaultObjectiveForUser'] = AdAccountDefaultObjective.DefaultObjectiveForUser.__dict__.values()
        field_enum_info['ObjectiveForLevel'] = AdAccountDefaultObjective.ObjectiveForLevel.__dict__.values()
        return field_enum_info


