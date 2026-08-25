# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

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

class AdCreativeGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCreativeGet = True
        super(AdCreativeGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        actor_id = 'actor_id'
        actor_type = 'actor_type'
        adlabels = 'adlabels'
        applink_treatment = 'applink_treatment'
        asset_feed_spec = 'asset_feed_spec'
        authorization_category = 'authorization_category'
        body = 'body'
        branded_content = 'branded_content'
        branded_content_boosting_type = 'branded_content_boosting_type'
        bundle_folder_id = 'bundle_folder_id'
        call_to_action = 'call_to_action'
        call_to_action_type = 'call_to_action_type'
        categorization_criteria = 'categorization_criteria'
        category_media_source = 'category_media_source'
        contextual_multi_ads = 'contextual_multi_ads'
        creative_sourcing_spec = 'creative_sourcing_spec'
        degrees_of_freedom_spec = 'degrees_of_freedom_spec'
        destination_spec = 'destination_spec'
        dynamic_ad_voice = 'dynamic_ad_voice'
        effective_authorization_category = 'effective_authorization_category'
        effective_instagram_media_id = 'effective_instagram_media_id'
        effective_instagram_story_id = 'effective_instagram_story_id'
        effective_object_story_id = 'effective_object_story_id'
        enable_direct_install = 'enable_direct_install'
        enable_launch_instant_app = 'enable_launch_instant_app'
        existing_post_title = 'existing_post_title'
        facebook_branded_content = 'facebook_branded_content'
        format_transformation_spec = 'format_transformation_spec'
        id = 'id'
        image_crops = 'image_crops'
        image_hash = 'image_hash'
        image_url = 'image_url'
        instagram_branded_content = 'instagram_branded_content'
        instagram_permalink_url = 'instagram_permalink_url'
        instagram_user_id = 'instagram_user_id'
        interactive_components_spec = 'interactive_components_spec'
        link_og_id = 'link_og_id'
        link_url = 'link_url'
        media_sourcing_spec = 'media_sourcing_spec'
        media_type = 'media_type'
        name = 'name'
        object_id = 'object_id'
        object_store_url = 'object_store_url'
        object_story_id = 'object_story_id'
        object_story_spec = 'object_story_spec'
        object_type = 'object_type'
        object_url = 'object_url'
        omnichannel_link_spec = 'omnichannel_link_spec'
        page_id = 'page_id'
        page_welcome_message = 'page_welcome_message'
        photo_album_source_object_story_id = 'photo_album_source_object_story_id'
        place_page_set_id = 'place_page_set_id'
        platform_customizations = 'platform_customizations'
        playable_asset_id = 'playable_asset_id'
        portrait_customizations = 'portrait_customizations'
        product_set_id = 'product_set_id'
        recommender_settings = 'recommender_settings'
        regional_regulation_disclaimer_spec = 'regional_regulation_disclaimer_spec'
        source_facebook_post_id = 'source_facebook_post_id'
        source_instagram_media_id = 'source_instagram_media_id'
        status = 'status'
        template_url = 'template_url'
        template_url_spec = 'template_url_spec'
        threads_media_id = 'threads_media_id'
        threads_user_id = 'threads_user_id'
        thumbnail_id = 'thumbnail_id'
        thumbnail_url = 'thumbnail_url'
        title = 'title'
        uca_draft_version = 'uca_draft_version'
        url_tags = 'url_tags'
        use_page_actor_override = 'use_page_actor_override'
        video_id = 'video_id'
        visual_hash = 'visual_hash'

    class ActorType:
        page = 'PAGE'
        user = 'USER'

    class ApplinkTreatment:
        automatic = 'AUTOMATIC'
        deeplink_with_appstore_fallback = 'DEEPLINK_WITH_APPSTORE_FALLBACK'
        deeplink_with_web_fallback = 'DEEPLINK_WITH_WEB_FALLBACK'
        web_only = 'WEB_ONLY'

    class AuthorizationCategory:
        none = 'NONE'
        political = 'POLITICAL'
        political_with_digitally_created_media = 'POLITICAL_WITH_DIGITALLY_CREATED_MEDIA'

    class BrandedContentBoostingType:
        creator_boost = 'CREATOR_BOOST'
        creator_inline = 'CREATOR_INLINE'
        sponsor_boost = 'SPONSOR_BOOST'
        sponsor_inline = 'SPONSOR_INLINE'

    class CallToActionType:
        activate_offer = 'ACTIVATE_OFFER'
        add_to_cart = 'ADD_TO_CART'
        apply_now = 'APPLY_NOW'
        ask_about_services = 'ASK_ABOUT_SERVICES'
        ask_a_question = 'ASK_A_QUESTION'
        ask_for_more_info = 'ASK_FOR_MORE_INFO'
        ask_us = 'ASK_US'
        audio_call = 'AUDIO_CALL'
        bet_now = 'BET_NOW'
        blood_donations = 'BLOOD_DONATIONS'
        book_a_consultation = 'BOOK_A_CONSULTATION'
        book_now = 'BOOK_NOW'
        book_test_drive = 'BOOK_TEST_DRIVE'
        book_travel = 'BOOK_TRAVEL'
        browse_shop = 'BROWSE_SHOP'
        buy = 'BUY'
        buy_now = 'BUY_NOW'
        buy_tickets = 'BUY_TICKETS'
        buy_via_message = 'BUY_VIA_MESSAGE'
        call = 'CALL'
        call_me = 'CALL_ME'
        call_now = 'CALL_NOW'
        chat_now = 'CHAT_NOW'
        chat_on_whatsapp = 'CHAT_ON_WHATSAPP'
        chat_with_us = 'CHAT_WITH_US'
        check_availability = 'CHECK_AVAILABILITY'
        civic_action = 'CIVIC_ACTION'
        claim_offer = 'CLAIM_OFFER'
        confirm = 'CONFIRM'
        contact = 'CONTACT'
        contact_us = 'CONTACT_US'
        dial_code = 'DIAL_CODE'
        donate = 'DONATE'
        donate_now = 'DONATE_NOW'
        download = 'DOWNLOAD'
        email_now = 'EMAIL_NOW'
        event_rsvp = 'EVENT_RSVP'
        explore_more = 'EXPLORE_MORE'
        find_a_group = 'FIND_A_GROUP'
        find_out_more = 'FIND_OUT_MORE'
        find_your_groups = 'FIND_YOUR_GROUPS'
        follow_news_storyline = 'FOLLOW_NEWS_STORYLINE'
        follow_page = 'FOLLOW_PAGE'
        follow_user = 'FOLLOW_USER'
        get_a_quote = 'GET_A_QUOTE'
        get_details = 'GET_DETAILS'
        get_directions = 'GET_DIRECTIONS'
        get_event_tickets = 'GET_EVENT_TICKETS'
        get_in_touch = 'GET_IN_TOUCH'
        get_mobile_app = 'GET_MOBILE_APP'
        get_offer = 'GET_OFFER'
        get_offer_view = 'GET_OFFER_VIEW'
        get_promotions = 'GET_PROMOTIONS'
        get_quote = 'GET_QUOTE'
        get_showtimes = 'GET_SHOWTIMES'
        get_started = 'GET_STARTED'
        give_free_rides = 'GIVE_FREE_RIDES'
        go_live = 'GO_LIVE'
        imagine = 'IMAGINE'
        inquire_now = 'INQUIRE_NOW'
        instagram_message = 'INSTAGRAM_MESSAGE'
        install_app = 'INSTALL_APP'
        install_free_mobile_app = 'INSTALL_FREE_MOBILE_APP'
        install_mobile_app = 'INSTALL_MOBILE_APP'
        interested = 'INTERESTED'
        jobs_apply_now = 'JOBS_APPLY_NOW'
        join_channel = 'JOIN_CHANNEL'
        join_group = 'JOIN_GROUP'
        join_live_video = 'JOIN_LIVE_VIDEO'
        learn_more = 'LEARN_MORE'
        like_page = 'LIKE_PAGE'
        link_card = 'LINK_CARD'
        listen_music = 'LISTEN_MUSIC'
        listen_now = 'LISTEN_NOW'
        loyalty_learn_more = 'LOYALTY_LEARN_MORE'
        make_an_appointment = 'MAKE_AN_APPOINTMENT'
        message_page = 'MESSAGE_PAGE'
        message_user = 'MESSAGE_USER'
        missed_call = 'MISSED_CALL'
        mobile_download = 'MOBILE_DOWNLOAD'
        moments = 'MOMENTS'
        no_button = 'NO_BUTTON'
        open_instant_app = 'OPEN_INSTANT_APP'
        open_link = 'OPEN_LINK'
        open_messenger_ext = 'OPEN_MESSENGER_EXT'
        open_movies = 'OPEN_MOVIES'
        order_now = 'ORDER_NOW'
        pay_or_request = 'PAY_OR_REQUEST'
        pay_to_access = 'PAY_TO_ACCESS'
        play = 'PLAY'
        play_game = 'PLAY_GAME'
        play_game_on_facebook = 'PLAY_GAME_ON_FACEBOOK'
        pre_register = 'PRE_REGISTER'
        purchase_gift_cards = 'PURCHASE_GIFT_CARDS'
        raise_money = 'RAISE_MONEY'
        record_now = 'RECORD_NOW'
        refer_friends = 'REFER_FRIENDS'
        register_now = 'REGISTER_NOW'
        remind_me = 'REMIND_ME'
        request_time = 'REQUEST_TIME'
        save = 'SAVE'
        save_offer = 'SAVE_OFFER'
        say_thanks = 'SAY_THANKS'
        search = 'SEARCH'
        search_more = 'SEARCH_MORE'
        see_details = 'SEE_DETAILS'
        see_menu = 'SEE_MENU'
        see_more = 'SEE_MORE'
        see_offer = 'SEE_OFFER'
        see_shop = 'SEE_SHOP'
        sell_now = 'SELL_NOW'
        send_a_gift = 'SEND_A_GIFT'
        send_gift = 'SEND_GIFT'
        send_gift_money = 'SEND_GIFT_MONEY'
        send_invites = 'SEND_INVITES'
        send_tip = 'SEND_TIP'
        send_updates = 'SEND_UPDATES'
        share = 'SHARE'
        shop_now = 'SHOP_NOW'
        shop_with_ai = 'SHOP_WITH_AI'
        sign_up = 'SIGN_UP'
        sotto_subscribe = 'SOTTO_SUBSCRIBE'
        start_a_chat = 'START_A_CHAT'
        start_order = 'START_ORDER'
        subscribe = 'SUBSCRIBE'
        swipe_up_product = 'SWIPE_UP_PRODUCT'
        swipe_up_shop = 'SWIPE_UP_SHOP'
        try_demo = 'TRY_DEMO'
        try_in_camera = 'TRY_IN_CAMERA'
        try_it = 'TRY_IT'
        try_now = 'TRY_NOW'
        try_on = 'TRY_ON'
        try_on_with_ai = 'TRY_ON_WITH_AI'
        unlike_page = 'UNLIKE_PAGE'
        update_app = 'UPDATE_APP'
        use_app = 'USE_APP'
        use_mobile_app = 'USE_MOBILE_APP'
        video_annotation = 'VIDEO_ANNOTATION'
        video_call = 'VIDEO_CALL'
        view_cart = 'VIEW_CART'
        view_channel = 'VIEW_CHANNEL'
        view_instagram_profile = 'VIEW_INSTAGRAM_PROFILE'
        view_in_cart = 'VIEW_IN_CART'
        view_product = 'VIEW_PRODUCT'
        view_resume = 'VIEW_RESUME'
        visit_pages_feed = 'VISIT_PAGES_FEED'
        visit_profile = 'VISIT_PROFILE'
        visit_website = 'VISIT_WEBSITE'
        visit_world = 'VISIT_WORLD'
        vote_now = 'VOTE_NOW'
        watch_app_upgrade = 'WATCH_APP_UPGRADE'
        watch_live_video = 'WATCH_LIVE_VIDEO'
        watch_more = 'WATCH_MORE'
        watch_music_video = 'WATCH_MUSIC_VIDEO'
        watch_video = 'WATCH_VIDEO'
        whatsapp_link = 'WHATSAPP_LINK'
        whatsapp_message = 'WHATSAPP_MESSAGE'
        woodhenge_support = 'WOODHENGE_SUPPORT'

    class CategorizationCriteria:
        brand = 'BRAND'
        category = 'CATEGORY'
        product_type = 'PRODUCT_TYPE'

    class CategoryMediaSource:
        category = 'CATEGORY'
        mixed = 'MIXED'
        products_collage = 'PRODUCTS_COLLAGE'
        products_slideshow = 'PRODUCTS_SLIDESHOW'

    class EffectiveAuthorizationCategory:
        none = 'NONE'
        political = 'POLITICAL'
        political_with_digitally_created_media = 'POLITICAL_WITH_DIGITALLY_CREATED_MEDIA'

    class MediaType:
        automatic = 'AUTOMATIC'
        carousel = 'CAROUSEL'
        carousel_image = 'CAROUSEL_IMAGE'
        collections_image = 'COLLECTIONS_IMAGE'
        collections_video = 'COLLECTIONS_VIDEO'
        existing_instagram_post = 'EXISTING_INSTAGRAM_POST'
        existing_post = 'EXISTING_POST'
        instagram_live_video = 'INSTAGRAM_LIVE_VIDEO'
        post = 'POST'
        scheduled_live_video = 'SCHEDULED_LIVE_VIDEO'
        single_image = 'SINGLE_IMAGE'
        single_link = 'SINGLE_LINK'
        single_photo = 'SINGLE_PHOTO'
        single_video = 'SINGLE_VIDEO'

    class ObjectType:
        application = 'APPLICATION'
        domain = 'DOMAIN'
        event = 'EVENT'
        invalid = 'INVALID'
        offer = 'OFFER'
        page = 'PAGE'
        photo = 'PHOTO'
        post_deleted = 'POST_DELETED'
        privacy_check_fail = 'PRIVACY_CHECK_FAIL'
        share = 'SHARE'
        status = 'STATUS'
        store_item = 'STORE_ITEM'
        video = 'VIDEO'

    _field_types = {
        'account_id': 'string',
        'actor_id': 'int',
        'actor_type': 'ActorType',
        'adlabels': 'list<object>',
        'applink_treatment': 'ApplinkTreatment',
        'asset_feed_spec': 'object',
        'authorization_category': 'AuthorizationCategory',
        'body': 'string',
        'branded_content': 'object',
        'branded_content_boosting_type': 'BrandedContentBoostingType',
        'bundle_folder_id': 'int',
        'call_to_action': 'object',
        'call_to_action_type': 'CallToActionType',
        'categorization_criteria': 'CategorizationCriteria',
        'category_media_source': 'CategoryMediaSource',
        'contextual_multi_ads': 'object',
        'creative_sourcing_spec': 'object',
        'degrees_of_freedom_spec': 'object',
        'destination_spec': 'object',
        'dynamic_ad_voice': 'string',
        'effective_authorization_category': 'EffectiveAuthorizationCategory',
        'effective_instagram_media_id': 'int',
        'effective_instagram_story_id': 'int',
        'effective_object_story_id': 'string',
        'enable_direct_install': 'bool',
        'enable_launch_instant_app': 'bool',
        'existing_post_title': 'string',
        'facebook_branded_content': 'object',
        'format_transformation_spec': 'list<object>',
        'id': 'int',
        'image_crops': 'object',
        'image_hash': 'string',
        'image_url': 'string',
        'instagram_branded_content': 'object',
        'instagram_permalink_url': 'string',
        'instagram_user_id': 'int',
        'interactive_components_spec': 'object',
        'link_og_id': 'int',
        'link_url': 'string',
        'media_sourcing_spec': 'object',
        'media_type': 'MediaType',
        'name': 'string',
        'object_id': 'int',
        'object_store_url': 'string',
        'object_story_id': 'string',
        'object_story_spec': 'object',
        'object_type': 'ObjectType',
        'object_url': 'string',
        'omnichannel_link_spec': 'object',
        'page_id': 'int',
        'page_welcome_message': 'string',
        'photo_album_source_object_story_id': 'string',
        'place_page_set_id': 'int',
        'platform_customizations': 'object',
        'playable_asset_id': 'int',
        'portrait_customizations': 'object',
        'product_set_id': 'int',
        'recommender_settings': 'object',
        'regional_regulation_disclaimer_spec': 'object',
        'source_facebook_post_id': 'int',
        'source_instagram_media_id': 'int',
        'status': 'string',
        'template_url': 'string',
        'template_url_spec': 'object',
        'threads_media_id': 'int',
        'threads_user_id': 'int',
        'thumbnail_id': 'int',
        'thumbnail_url': 'string',
        'title': 'string',
        'uca_draft_version': 'int',
        'url_tags': 'string',
        'use_page_actor_override': 'bool',
        'video_id': 'int',
        'visual_hash': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ActorType'] = AdCreativeGet.ActorType.__dict__.values()
        field_enum_info['ApplinkTreatment'] = AdCreativeGet.ApplinkTreatment.__dict__.values()
        field_enum_info['AuthorizationCategory'] = AdCreativeGet.AuthorizationCategory.__dict__.values()
        field_enum_info['BrandedContentBoostingType'] = AdCreativeGet.BrandedContentBoostingType.__dict__.values()
        field_enum_info['CallToActionType'] = AdCreativeGet.CallToActionType.__dict__.values()
        field_enum_info['CategorizationCriteria'] = AdCreativeGet.CategorizationCriteria.__dict__.values()
        field_enum_info['CategoryMediaSource'] = AdCreativeGet.CategoryMediaSource.__dict__.values()
        field_enum_info['EffectiveAuthorizationCategory'] = AdCreativeGet.EffectiveAuthorizationCategory.__dict__.values()
        field_enum_info['MediaType'] = AdCreativeGet.MediaType.__dict__.values()
        field_enum_info['ObjectType'] = AdCreativeGet.ObjectType.__dict__.values()
        return field_enum_info


