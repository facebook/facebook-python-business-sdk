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

class LiveVideo(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isLiveVideo = True
        super(LiveVideo, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_break_config = 'ad_break_config'
        ad_break_failure_reason = 'ad_break_failure_reason'
        broadcast_start_time = 'broadcast_start_time'
        copyright = 'copyright'
        creation_time = 'creation_time'
        dash_ingest_url = 'dash_ingest_url'
        dash_preview_url = 'dash_preview_url'
        description = 'description'
        embed_html = 'embed_html'
        field_from = 'from'
        id = 'id'
        is_manual_mode = 'is_manual_mode'
        is_reference_only = 'is_reference_only'
        live_encoders = 'live_encoders'
        live_views = 'live_views'
        permalink_url = 'permalink_url'
        planned_start_time = 'planned_start_time'
        seconds_left = 'seconds_left'
        secure_stream_url = 'secure_stream_url'
        status = 'status'
        stream_url = 'stream_url'
        title = 'title'
        video = 'video'

    class LiveCommentModerationSetting:
        follower = 'FOLLOWER'
        slow = 'SLOW'
        discussion = 'DISCUSSION'
        restricted = 'RESTRICTED'

    class Status:
        unpublished = 'UNPUBLISHED'
        live_now = 'LIVE_NOW'
        scheduled_unpublished = 'SCHEDULED_UNPUBLISHED'
        scheduled_live = 'SCHEDULED_LIVE'
        scheduled_canceled = 'SCHEDULED_CANCELED'

    class StreamType:
        regular = 'REGULAR'
        ambient = 'AMBIENT'

    class BroadcastStatus:
        unpublished = 'UNPUBLISHED'
        live = 'LIVE'
        live_stopped = 'LIVE_STOPPED'
        processing = 'PROCESSING'
        vod = 'VOD'
        scheduled_unpublished = 'SCHEDULED_UNPUBLISHED'
        scheduled_live = 'SCHEDULED_LIVE'
        scheduled_expired = 'SCHEDULED_EXPIRED'
        scheduled_canceled = 'SCHEDULED_CANCELED'

    class Projection:
        equirectangular = 'EQUIRECTANGULAR'
        cubemap = 'CUBEMAP'

    class Source:
        target = 'target'
        owner = 'owner'

    class SpatialAudioFormat:
        ambix_4 = 'ambiX_4'

    class StereoscopicMode:
        mono = 'MONO'
        left_right = 'LEFT_RIGHT'
        top_bottom = 'TOP_BOTTOM'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
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
            target_class=LiveVideo,
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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'ad_break_drop_live_stream': 'bool',
            'ad_break_duration': 'unsigned int',
            'ad_break_encoder_drops_live_stream': 'bool',
            'ad_break_intent': 'bool',
            'ad_break_start_now': 'bool',
            'ad_break_time_offset': 'float',
            'allow_bm_crossposting': 'bool',
            'attribution_app_id': 'string',
            'attribution_app_metadata': 'string',
            'commercial_break_durations': 'list<unsigned int>',
            'content_tags': 'list<string>',
            'crossposting_actions': 'list<map>',
            'custom_labels': 'list<string>',
            'description': 'string',
            'direct_share_status': 'unsigned int',
            'disturbing': 'bool',
            'embeddable': 'bool',
            'end_live_video': 'bool',
            'is_manual_mode': 'bool',
            'live_comment_moderation_setting': 'list<live_comment_moderation_setting_enum>',
            'live_encoders': 'list<string>',
            'place': 'Object',
            'planned_start_time': 'int',
            'privacy': 'Object',
            'product_items': 'list<string>',
            'published': 'bool',
            'schedule_custom_profile_image': 'file',
            'schedule_feed_background_image': 'file',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'status': 'status_enum',
            'stream_type': 'stream_type_enum',
            'tags': 'list<int>',
            'targeting': 'Object',
            'title': 'string',
        }
        enums = {
            'live_comment_moderation_setting_enum': LiveVideo.LiveCommentModerationSetting.__dict__.values(),
            'status_enum': LiveVideo.Status.__dict__.values(),
            'stream_type_enum': LiveVideo.StreamType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LiveVideo,
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
        'ad_break_config': 'Object',
        'ad_break_failure_reason': 'string',
        'broadcast_start_time': 'datetime',
        'copyright': 'VideoCopyright',
        'creation_time': 'datetime',
        'dash_ingest_url': 'string',
        'dash_preview_url': 'string',
        'description': 'string',
        'embed_html': 'string',
        'from': 'Object',
        'id': 'string',
        'is_manual_mode': 'bool',
        'is_reference_only': 'bool',
        'live_encoders': 'list<Object>',
        'live_views': 'unsigned int',
        'permalink_url': 'string',
        'planned_start_time': 'datetime',
        'seconds_left': 'int',
        'secure_stream_url': 'string',
        'status': 'string',
        'stream_url': 'string',
        'title': 'string',
        'video': 'Object',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['LiveCommentModerationSetting'] = LiveVideo.LiveCommentModerationSetting.__dict__.values()
        field_enum_info['Status'] = LiveVideo.Status.__dict__.values()
        field_enum_info['StreamType'] = LiveVideo.StreamType.__dict__.values()
        field_enum_info['BroadcastStatus'] = LiveVideo.BroadcastStatus.__dict__.values()
        field_enum_info['Projection'] = LiveVideo.Projection.__dict__.values()
        field_enum_info['Source'] = LiveVideo.Source.__dict__.values()
        field_enum_info['SpatialAudioFormat'] = LiveVideo.SpatialAudioFormat.__dict__.values()
        field_enum_info['StereoscopicMode'] = LiveVideo.StereoscopicMode.__dict__.values()
        return field_enum_info
