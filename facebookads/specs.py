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
from facebookads.adobjects import adcreativeobjectstoryspec
from facebookads.adobjects import adcreativelinkdatachildattachment
from facebookads.adobjects import adcreativelinkdata
from facebookads.adobjects import adcreativeofferdata
from facebookads.adobjects import adcreativephotodata
from facebookads.adobjects import adcreativetextdata
from facebookads.adobjects import adcreativevideodata


class ObjectStorySpec(adcreativeobjectstoryspec.AdCreativeObjectStorySpec):
    pass


class AttachmentData(adcreativelinkdatachildattachment.AdCreativeLinkDataChildAttachment):
    pass


class LinkData(adcreativelinkdata.AdCreativeLinkData):
    pass


class OfferData(adcreativeofferdata.AdCreativeOfferData):
    pass


class PhotoData(adcreativephotodata.AdCreativePhotoData):
    pass


class TemplateData(adcreativelinkdata.AdCreativeLinkData):
    pass


class TextData(adcreativetextdata.AdCreativeTextData):
    pass


class VideoData(adcreativevideodata.AdCreativeVideoData):
    pass


class SlideshowSpec(ValidatesFields, AbstractObject):
    class Field(object):
        images_urls = 'images_urls'
        duration_ms = 'duration_ms'
        transition_ms = 'transition_ms'
