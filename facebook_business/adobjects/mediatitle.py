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
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class MediaTitle(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isMediaTitle = True
        super(MediaTitle, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        applinks = 'applinks'
        content_category = 'content_category'
        content_countries = 'content_countries'
        content_locale = 'content_locale'
        crew = 'crew'
        currency = 'currency'
        description = 'description'
        episode = 'episode'
        fb_page_alias = 'fb_page_alias'
        fb_page_id = 'fb_page_id'
        genres = 'genres'
        id = 'id'
        images = 'images'
        instagram_username = 'instagram_username'
        media_source = 'media_source'
        media_title_id = 'media_title_id'
        mpaa_rating = 'mpaa_rating'
        performers = 'performers'
        price = 'price'
        release_date = 'release_date'
        sanitized_images = 'sanitized_images'
        season = 'season'
        similar_titles = 'similar_titles'
        subtitle_locale = 'subtitle_locale'
        title = 'title'
        url = 'url'
        view_count_eighty_four_days = 'view_count_eighty_four_days'
        view_count_fourteen_days = 'view_count_fourteen_days'
        view_count_one_day = 'view_count_one_day'
        view_count_seven_days = 'view_count_seven_days'
        view_count_twenty_eight_days = 'view_count_twenty_eight_days'
        wiki_data_item = 'wiki_data_item'
        wikipedia_url = 'wikipedia_url'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MediaTitle,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'applinks': 'AppLinks',
        'content_category': 'string',
        'content_countries': 'list<string>',
        'content_locale': 'string',
        'crew': 'list<string>',
        'currency': 'string',
        'description': 'string',
        'episode': 'unsigned int',
        'fb_page_alias': 'string',
        'fb_page_id': 'Page',
        'genres': 'list<string>',
        'id': 'string',
        'images': 'list<string>',
        'instagram_username': 'string',
        'media_source': 'string',
        'media_title_id': 'string',
        'mpaa_rating': 'string',
        'performers': 'list<string>',
        'price': 'string',
        'release_date': 'string',
        'sanitized_images': 'list<string>',
        'season': 'unsigned int',
        'similar_titles': 'list<string>',
        'subtitle_locale': 'string',
        'title': 'string',
        'url': 'string',
        'view_count_eighty_four_days': 'Object',
        'view_count_fourteen_days': 'Object',
        'view_count_one_day': 'Object',
        'view_count_seven_days': 'Object',
        'view_count_twenty_eight_days': 'Object',
        'wiki_data_item': 'string',
        'wikipedia_url': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


