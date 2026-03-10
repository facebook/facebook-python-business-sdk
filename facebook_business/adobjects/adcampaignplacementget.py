# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCampaignPlacementGet(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCampaignPlacementGet, self).__init__()
        self._isAdCampaignPlacementGet = True
        self._api = api

    class Field(AbstractObject.Field):
        effective_audience_network_positions = 'effective_audience_network_positions'
        effective_device_platforms = 'effective_device_platforms'
        effective_facebook_positions = 'effective_facebook_positions'
        effective_instagram_positions = 'effective_instagram_positions'
        effective_messenger_positions = 'effective_messenger_positions'
        effective_oculus_positions = 'effective_oculus_positions'
        effective_publisher_platforms = 'effective_publisher_platforms'
        metadata = 'metadata'
        recommendations = 'recommendations'

    class EffectiveAudienceNetworkPositions:
        classic = 'CLASSIC'
        instream_video = 'INSTREAM_VIDEO'
        rewarded_video = 'REWARDED_VIDEO'

    class EffectiveDevicePlatforms:
        desktop = 'DESKTOP'
        mobile = 'MOBILE'

    class EffectiveFacebookPositions:
        biz_disco_feed = 'BIZ_DISCO_FEED'
        facebook_contextual_bundle = 'FACEBOOK_CONTEXTUAL_BUNDLE'
        fb_reels = 'FB_REELS'
        fb_reels_overlay = 'FB_REELS_OVERLAY'
        feed = 'FEED'
        groups = 'GROUPS'
        group_mall = 'GROUP_MALL'
        group_tab = 'GROUP_TAB'
        instant_article = 'INSTANT_ARTICLE'
        instream_reel = 'INSTREAM_REEL'
        instream_video = 'INSTREAM_VIDEO'
        jobs_browser = 'JOBS_BROWSER'
        marketplace = 'MARKETPLACE'
        notification = 'NOTIFICATION'
        profile_feed = 'PROFILE_FEED'
        profile_reels = 'PROFILE_REELS'
        rhc = 'RHC'
        search = 'SEARCH'
        story = 'STORY'
        story_sticker = 'STORY_STICKER'
        suggested_video = 'SUGGESTED_VIDEO'
        video_feeds = 'VIDEO_FEEDS'

    class EffectiveInstagramPositions:
        effect_tray = 'EFFECT_TRAY'
        explore = 'EXPLORE'
        explore_home = 'EXPLORE_HOME'
        igtv = 'IGTV'
        ig_search = 'IG_SEARCH'
        lead_gen_multi_submit = 'LEAD_GEN_MULTI_SUBMIT'
        profile_feed = 'PROFILE_FEED'
        profile_reels = 'PROFILE_REELS'
        reels = 'REELS'
        reels_instream = 'REELS_INSTREAM'
        reels_overlay = 'REELS_OVERLAY'
        shop = 'SHOP'
        story = 'STORY'
        stream = 'STREAM'

    class EffectiveMessengerPositions:
        messenger_inbox = 'MESSENGER_INBOX'
        messenger_marketing_messages = 'MESSENGER_MARKETING_MESSAGES'
        messenger_story = 'MESSENGER_STORY'
        messenger_thread = 'MESSENGER_THREAD'

    class EffectiveOculusPositions:
        twilight_developer_update = 'TWILIGHT_DEVELOPER_UPDATE'
        twilight_feed = 'TWILIGHT_FEED'
        twilight_feed_spotlight = 'TWILIGHT_FEED_SPOTLIGHT'
        twilight_search = 'TWILIGHT_SEARCH'
        twilight_search_null_state = 'TWILIGHT_SEARCH_NULL_STATE'
        vr_apps = 'VR_APPS'
        vr_rewarded_video = 'VR_REWARDED_VIDEO'

    class EffectivePublisherPlatforms:
        audience_network = 'AUDIENCE_NETWORK'
        facebook = 'FACEBOOK'
        instagram = 'INSTAGRAM'
        messenger = 'MESSENGER'
        oculus = 'OCULUS'
        threads = 'THREADS'
        whatsapp = 'WHATSAPP'

    _field_types = {
        'effective_audience_network_positions': 'list<EffectiveAudienceNetworkPositions>',
        'effective_device_platforms': 'list<EffectiveDevicePlatforms>',
        'effective_facebook_positions': 'list<EffectiveFacebookPositions>',
        'effective_instagram_positions': 'list<EffectiveInstagramPositions>',
        'effective_messenger_positions': 'list<EffectiveMessengerPositions>',
        'effective_oculus_positions': 'list<EffectiveOculusPositions>',
        'effective_publisher_platforms': 'list<EffectivePublisherPlatforms>',
        'metadata': 'object',
        'recommendations': 'list<object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['EffectiveAudienceNetworkPositions'] = AdCampaignPlacementGet.EffectiveAudienceNetworkPositions.__dict__.values()
        field_enum_info['EffectiveDevicePlatforms'] = AdCampaignPlacementGet.EffectiveDevicePlatforms.__dict__.values()
        field_enum_info['EffectiveFacebookPositions'] = AdCampaignPlacementGet.EffectiveFacebookPositions.__dict__.values()
        field_enum_info['EffectiveInstagramPositions'] = AdCampaignPlacementGet.EffectiveInstagramPositions.__dict__.values()
        field_enum_info['EffectiveMessengerPositions'] = AdCampaignPlacementGet.EffectiveMessengerPositions.__dict__.values()
        field_enum_info['EffectiveOculusPositions'] = AdCampaignPlacementGet.EffectiveOculusPositions.__dict__.values()
        field_enum_info['EffectivePublisherPlatforms'] = AdCampaignPlacementGet.EffectivePublisherPlatforms.__dict__.values()
        return field_enum_info


