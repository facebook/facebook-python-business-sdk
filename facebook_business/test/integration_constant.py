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

# This file stores the information needed to perform integration testing
# on the Python Ads SDK.

class FieldName:
    ACCOUNT_ID = 'account_id'
    ACTOR_ID = 'actor_id'
    AD_FORMAT = 'ad_format'
    ADLABELS = 'adlabels'
    ADSET_ID = 'adset_id'
    ADSET_SCHEDULE = 'adset_schedule'
    APPLINK_TREATMENT = 'applink_treatment'
    AUTHORIZATION_CATEGORY = 'authorization_category'
    AUTO_UPDATE = 'auto_update'
    ASSET_FEED_ID = 'asset_feed_id'
    BID_ADJUSTMENTS = 'bid_adjustments'
    BID_AMOUNT = 'bid_amount'
    BID_STRATEGY = 'bid_strategy'
    BILLING_EVENT = 'billing_event'
    BODY = 'body'
    BOOSTED_OBJECT_ID = 'boosted_object_id'
    BRAND_LIFT_STUDIES = 'brand_lift_studies'
    BUDGET_REBALANCE_FLAG = 'budget_rebalance_flag'
    BUDGET_REMAINING = 'budget_remaining'
    BUYING_TYPE = 'buying_type'
    CALL_TO_ACTION_TYPE = 'call_to_action_type'
    CAMPAIGN_ID = 'campaign_id'
    CAN_CREATE_BRAND_LIFT_STUDY = 'can_create_brand_lift_study'
    CAN_USE_SPEND_CAP = 'can_use_spend_cap'
    CATEGORIZATION_CRITERIA = 'categorization_criteria'
    CONFIGURED_STATUS = 'configured_status'
    CREATED_TIME = 'created_time'
    DAILY_BUDGET = 'daily_budget'
    DAILY_MIN_SPEND_TARGET = 'daily_min_spend_target'
    DATE_FORMAT = 'date_format'
    DYNAMIC_ASSET_LABEL = 'dynamic_asset_label'
    DYNAMIC_CREATIVE_SPEC = 'dynamic_creative_spec'
    EFFECTIVE_STATUS = 'effective_status'
    EXECUTION_OPTIONS = 'execution_options'
    HEIGHT = 'height'
    ID = 'id'
    IMAGE_HASH = 'image_hash'
    INSTAGRAM_ACTOR_ID = 'instagram_actor_id'
    ISSUES_INFO = 'issues_info'
    ITERATIVE_SPLIT_TEST_CONFIGS = 'iterative_split_test_configs'
    LAST_BUDGET_TOGGLING_TIME = 'last_budget_toggling_time'
    LIFETIME_BUDGET = 'lifetime_budget'
    NAME = 'name'
    OBJECTIVE = 'objective'
    OBJECT_URL = 'object_url'
    OPTIMIZATION_GOAL = 'optimization_goal'
    RECOMMENDATIONS = 'recommendations'
    RENDER_TYPE = 'render_type'
    REVIEW_FEEDBACK = 'review_feedback'
    PACING_TYPE = 'pacing_type'
    PROMOTED_OBJECT = 'promoted_object'
    SOURCE_CAMPAIGN_ID = 'source_campaign_id'
    SPECIAL_AD_CATEGORY = 'special_ad_category'
    SPEND_CAP = 'spend_cap'
    STATUS = 'status'
    TARGETING = 'targeting'
    TITLE = 'title'
    TOPLINE_ID = 'topline_id'
    TUNE_FOR_CATEGORY = 'tune_for_category'
    START_TIME = 'start_time'
    STOP_TIME = 'stop_time'
    UPDATED_TIME = 'updated_time'
    UPSTREAM_EVENTS = 'upstream_events'
    WIDTH = 'width'

class TestValue:
    ACCESS_TOKEN = 'accesstoken'
    ACCOUNT_ID = 'act_123'
    ACTOR_ID = '1245'
    AD_LABEL = '{"name": "test_label"}'
    AD_FORMAT = 'DESKTOP_FEED_STANDARD'
    ADSET_ID = '12345'
    ADSET_SCHEDULE = '{"pacing_type": "standard"}'
    APPLINK_TREATMENT = 'deeplink_with_web_fallback'
    APP_ID = '1234567'
    APP_SECRET = 'appsecret'
    APP_URL = 'http://test.com'
    ASSET_FEED_ID = '123'
    AUTHORIZATION_CATEGORY = 'NONE'
    AUTO_UPDATE = 'true'
    BID_ADJUSTMENTS = '{"user_groups": "test_group"}'
    BID_AMOUNT = '30000'
    BID_STRATEGY = 'LOWEST_COST_WITHOUT_CAP'
    BILLING_EVENT = 'IMPRESSIONS'
    BODY = "This is my test body"
    BOOSTED_OBJECT_ID = '12345678'
    BRAND_LIFT_STUDIES = (
        '{'
        '"id": "cell_id",'
        '"name":"Group A",'
        '"treatment_percentage": "50",'
        '"adsets": {"id" : "adset_id"}'
        '}'
    )
    BUDGET_REBALANCE_FLAG = 'false'
    BUDGET_REMAINING = '150'
    BUSINESS_ID = '111111'
    BUYING_TYPE = 'AUCTION'
    CALL_TO_ACTION_TYPE = 'CONTACT'
    CAMPAIGN_ID = '1234321'
    CAN_CREATE_BRAND_LIFT_STUDY = 'true'
    CAN_USE_SPEND_CAP = 'true'
    CATEGORIZATION_CRITERIA = 'brand'
    CONFIGURED_STATUS = 'PAUSED'
    CREATED_TIME = '3728193'
    CREATIVE_ID = '1523548'
    DAILY_BUDGET = '200'
    DAILY_MIN_SPEND_TARGET = '50'
    DATE_FORMAT = 'U'
    DYNAMIC_ASSET_LABEL = 'test dynamic asset label'
    DYNAMIC_CREATIVE_SPEC = (
        '{'
        '"message": "test message",'
        '"description": "test description"'
        '}'
    )
    EFFECTIVE_STATUS = 'PAUSED'
    EXECUTION_OPTIONS = 'include_recommendations'
    HEIGHT = 690
    IMAGE_HASH = '9fdba2b8a67f316e107d3cbbfad2952'
    INSTAGRAM_ACTOR_ID = '12321'
    ISSUES_INFO = (
        '{'
        '"level": "AD",'
        '"error_code": "1815869",'
        '"error_summary": "Ad post is not available"'
        '}'
    )
    ITERATIVE_SPLIT_TEST_CONFIGS = '{"name": "test_config"}'
    LAST_BUDGET_TOGGLING_TIME = '3892193'
    LIFETIME_BUDGET = '10000'
    NAME = 'test_name'
    OBJECTIVE = 'LINK_CLICKS'
    OBJECT_URL = 'http://test.object.com'
    OPTIMIZATION_GOAL = 'LINK_CLICKS'
    PACING_TYPE = 'standard'
    PAGE_ID = '13531'
    PROMOTED_OBJECT = '{"page_id": "13531"}'
    RECOMMENDATIONS = '{"code": "1772120"}'
    RENDER_TYPE = 'FALLBACK'
    REVIEW_FEEDBACK = 'test review'
    SECONDARY_BUSINESS_ID = '2222222'
    SECONDARY_ACCOUNT_ID = 'act_456'
    SECONDARY_PAGE_ID = '24642'
    SPECIAL_AD_CATEGORY = 'EMPLOYMENT'
    SPEND_CAP = '922337203685478'
    START_TIME = '3728232'
    STATUS = 'PAUSED'
    STOP_TIME = '3872293'
    TARGETING = (
        '{'
        '"geo_locations": {"countries": "US"},'
        '"interests":{"id": "12345678910", "name": "Parenting"}'
        '}'
    )
    TITLE = 'test_title'
    TOPLINE_ID = '32123'
    TUNE_FOR_CATEGORY = 'CREDIT'
    UPDATED_TIME = '3728132'
    UPSTREAM_EVENTS = '{"name": "event_1", "event_id": "12121"}'
    WIDTH = 540
