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

class LiveEncoder(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isLiveEncoder = True
        super(LiveEncoder, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        brand = 'brand'
        creation_time = 'creation_time'
        current_broadcast = 'current_broadcast'
        current_input_stream = 'current_input_stream'
        device_id = 'device_id'
        id = 'id'
        last_heartbeat_time = 'last_heartbeat_time'
        model = 'model'
        name = 'name'
        status = 'status'
        version = 'version'

    class CapAudioCodecs:
        aac = 'AAC'

    class CapStreamingProtocols:
        https_dash = 'HTTPS_DASH'
        rtmps = 'RTMPS'
        webrtc = 'WEBRTC'

    class CapVideoCodecs:
        h264 = 'H264'

    class Status:
        capture = 'CAPTURE'
        live = 'LIVE'
        none = 'NONE'
        preview = 'PREVIEW'
        ready = 'READY'
        register = 'REGISTER'

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            target_class=LiveEncoder,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'broadcast_id': 'string',
            'cap_audio_codecs': 'list<cap_audio_codecs_enum>',
            'cap_streaming_protocols': 'list<cap_streaming_protocols_enum>',
            'cap_video_codecs': 'list<cap_video_codecs_enum>',
            'error_code': 'unsigned int',
            'error_msg': 'string',
            'input_audio_channels': 'unsigned int',
            'input_audio_samplerate': 'unsigned int',
            'input_video_framerate': 'string',
            'input_video_gop_num_b_frames': 'unsigned int',
            'input_video_gop_size': 'unsigned int',
            'input_video_height': 'unsigned int',
            'input_video_interlace_mode': 'string',
            'input_video_width': 'unsigned int',
            'name': 'string',
            'needs_transcoder_restart': 'bool',
            'needs_transcoder_restart_reason': 'list<string>',
            'status': 'status_enum',
            'target_token': 'string',
            'version': 'string',
        }
        enums = {
            'cap_audio_codecs_enum': LiveEncoder.CapAudioCodecs.__dict__.values(),
            'cap_streaming_protocols_enum': LiveEncoder.CapStreamingProtocols.__dict__.values(),
            'cap_video_codecs_enum': LiveEncoder.CapVideoCodecs.__dict__.values(),
            'status_enum': LiveEncoder.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LiveEncoder,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_telemetry(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'bitrate': 'unsigned int',
            'broadcast_id': 'string',
            'cpu_load_15m': 'float',
            'cpu_load_1m': 'float',
            'cpu_load_5m': 'float',
            'cpu_temperature': 'unsigned int',
            'cpu_usage': 'float',
            'framerate': 'float',
            'frames_dropped': 'float',
            'gpu_temperature': 'unsigned int',
            'gpu_usage': 'float',
            'last_audio_timecode': 'unsigned int',
            'last_video_keyframe_timecode': 'unsigned int',
            'last_video_timecode': 'unsigned int',
            'memory_usage': 'float',
            'network_latency': 'float',
            'network_rx_bandwidth': 'unsigned int',
            'network_rx_packets_dropped': 'float',
            'network_rx_packets_errors': 'float',
            'network_tx_bandwidth': 'unsigned int',
            'network_tx_packets_dropped': 'float',
            'network_tx_packets_errors': 'float',
            'process_uptime': 'unsigned int',
            'status': 'status_enum',
            'timestamp': 'unsigned int',
            'total_audio_frames_sent': 'unsigned int',
            'total_video_frames_sent': 'unsigned int',
            'total_video_keyframes_sent': 'unsigned int',
            'uptime': 'unsigned int',
        }
        enums = {
            'status_enum': LiveEncoder.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/telemetry',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LiveEncoder,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LiveEncoder, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'brand': 'string',
        'creation_time': 'datetime',
        'current_broadcast': 'LiveVideo',
        'current_input_stream': 'LiveVideoInputStream',
        'device_id': 'string',
        'id': 'string',
        'last_heartbeat_time': 'datetime',
        'model': 'string',
        'name': 'string',
        'status': 'string',
        'version': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CapAudioCodecs'] = LiveEncoder.CapAudioCodecs.__dict__.values()
        field_enum_info['CapStreamingProtocols'] = LiveEncoder.CapStreamingProtocols.__dict__.values()
        field_enum_info['CapVideoCodecs'] = LiveEncoder.CapVideoCodecs.__dict__.values()
        field_enum_info['Status'] = LiveEncoder.Status.__dict__.values()
        return field_enum_info


