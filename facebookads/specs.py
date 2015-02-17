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
specs module contains classes that help you define and create specs for use
in the Ads API.
"""

from facebookads.objects import AbstractObject
from facebookads.mixins import ValidatesFields


class ObjectStorySpec(ValidatesFields, AbstractObject):
    class Field(object):
        link_data = 'link_data'
        offer_data = 'offer_data'
        page_id = 'page_id'
        photo_data = 'photo_data'
        template_data = 'template_data'
        text_data = 'text_data'
        video_data = 'video_data'


class AttachmentData(ValidatesFields, AbstractObject):
    class Field(object):
        description = 'description'
        image_hash = 'image_hash'
        link = 'link'
        name = 'name'
        picture = 'picture'


class LinkData(ValidatesFields, AbstractObject):
    class Field(object):
        call_to_action = 'call_to_action'
        caption = 'caption'
        child_attachments = 'child_attachments'
        description = 'description'
        image_hash = 'image_hash'
        image_crops = 'image_crops'
        link = 'link'
        message = 'message'
        name = 'name'
        picture = 'picture'


class OfferData(ValidatesFields, AbstractObject):
    class Field(object):
        barcode_type = 'barcode_type'
        barcode = 'barcode'
        claim_limit = 'claim_limit'
        coupon_type = 'coupon_type'
        expiration_time = 'expiration_time'
        image_url = 'image_url'
        message = 'message'
        reminder_time = 'reminder_time'
        redemption_link = 'redemption_link'
        redemption_code = 'redemption_code'
        title = 'title'


class PhotoData(ValidatesFields, AbstractObject):
    class Field(object):
        caption = 'caption'
        url = 'url'


class TemplateData(ValidatesFields, AbstractObject):
    class Field(object):
        call_to_action = 'call_to_action'
        description = 'description'
        link = 'link'
        max_product_count = 'max_product_count'
        message = 'message'
        name = 'name'


class TextData(ValidatesFields, AbstractObject):
    class Field(object):
        message = 'message'


class VideoData(ValidatesFields, AbstractObject):
    class Field(object):
        call_to_action = 'call_to_action'
        description = 'description'
        image_url = 'image_url'
        title = 'title'
        video_id = 'video_id'
