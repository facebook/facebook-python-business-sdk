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

class CanvasAdSettings(
    AbstractObject,
):

    def __init__(self, api=None):
        super(CanvasAdSettings, self).__init__()
        self._isCanvasAdSettings = True
        self._api = api

    class Field(AbstractObject.Field):
        is_canvas_collection_eligible = 'is_canvas_collection_eligible'
        lead_form_created_time = 'lead_form_created_time'
        lead_form_name = 'lead_form_name'
        lead_gen_form_id = 'lead_gen_form_id'
        leads_count = 'leads_count'
        product_set_id = 'product_set_id'
        use_retailer_item_ids = 'use_retailer_item_ids'

    _field_types = {
        'is_canvas_collection_eligible': 'bool',
        'lead_form_created_time': 'unsigned int',
        'lead_form_name': 'string',
        'lead_gen_form_id': 'string',
        'leads_count': 'int',
        'product_set_id': 'string',
        'use_retailer_item_ids': 'bool',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


