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

class AdCreativeFeaturesSpec(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeFeaturesSpec, self).__init__()
        self._isAdCreativeFeaturesSpec = True
        self._api = api

    class Field(AbstractObject.Field):
        advantage_plus_creative = 'advantage_plus_creative'
        audio = 'audio'
        carousel_to_video = 'carousel_to_video'
        cv_transformation = 'cv_transformation'
        description_automation = 'description_automation'
        dha_optimization = 'dha_optimization'
        ig_glados_feed = 'ig_glados_feed'
        image_auto_crop = 'image_auto_crop'
        image_background_gen = 'image_background_gen'
        image_enhancement = 'image_enhancement'
        image_templates = 'image_templates'
        image_touchups = 'image_touchups'
        image_uncrop = 'image_uncrop'
        inline_comment = 'inline_comment'
        media_liquidity_animated_image = 'media_liquidity_animated_image'
        media_order = 'media_order'
        media_type_automation = 'media_type_automation'
        product_extensions = 'product_extensions'
        product_metadata_automation = 'product_metadata_automation'
        product_tags = 'product_tags'
        profile_card = 'profile_card'
        standard_enhancements = 'standard_enhancements'
        standard_enhancements_catalog = 'standard_enhancements_catalog'
        text_generation = 'text_generation'
        text_optimizations = 'text_optimizations'
        video_auto_crop = 'video_auto_crop'
        video_highlight = 'video_highlight'

    _field_types = {
        'advantage_plus_creative': 'AdCreativeFeatureDetails',
        'audio': 'AdCreativeFeatureDetails',
        'carousel_to_video': 'AdCreativeFeatureDetails',
        'cv_transformation': 'AdCreativeFeatureDetails',
        'description_automation': 'AdCreativeFeatureDetails',
        'dha_optimization': 'AdCreativeFeatureDetails',
        'ig_glados_feed': 'AdCreativeFeatureDetails',
        'image_auto_crop': 'AdCreativeFeatureDetails',
        'image_background_gen': 'AdCreativeFeatureDetails',
        'image_enhancement': 'AdCreativeFeatureDetails',
        'image_templates': 'AdCreativeFeatureDetails',
        'image_touchups': 'AdCreativeFeatureDetails',
        'image_uncrop': 'AdCreativeFeatureDetails',
        'inline_comment': 'AdCreativeFeatureDetails',
        'media_liquidity_animated_image': 'AdCreativeFeatureDetails',
        'media_order': 'AdCreativeFeatureDetails',
        'media_type_automation': 'AdCreativeFeatureDetails',
        'product_extensions': 'AdCreativeFeatureDetails',
        'product_metadata_automation': 'AdCreativeFeatureDetails',
        'product_tags': 'AdCreativeFeatureDetails',
        'profile_card': 'AdCreativeFeatureDetails',
        'standard_enhancements': 'AdCreativeFeatureDetails',
        'standard_enhancements_catalog': 'AdCreativeFeatureDetails',
        'text_generation': 'AdCreativeFeatureDetails',
        'text_optimizations': 'AdCreativeFeatureDetails',
        'video_auto_crop': 'AdCreativeFeatureDetails',
        'video_highlight': 'AdCreativeFeatureDetails',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


