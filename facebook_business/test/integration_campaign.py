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

'''
Unit tests for the Python Facebook Business SDK.

How to run:
    python -m facebook_business.test.integration_campaign
'''

import warnings
import json
from mock import patch
from facebook_business.session import FacebookSession
from facebook_business.exceptions import FacebookRequestError
from facebook_business.api import FacebookAdsApi, FacebookRequest, FacebookResponse
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adpromotedobject import AdPromotedObject
from .integration_utils import *
from .integration_constant import *


class CampaignTestCase(IntegrationTestCase):
    def test_get_campaign(self):
        with warnings.catch_warnings(record=True) as warning:
            self.mock_response.status_code = StatusCode.SUCCESS
            self.mock_response._content = (
                '{'
                '"' + str(FieldName.ACCOUNT_ID) + '":"' + str(TestValue.ACCOUNT_ID) + '",'
                '"' + str(FieldName.ADLABELS) + '":' + str(TestValue.AD_LABEL) + ','
                '"' + str(FieldName.BID_STRATEGY) + '":"' + str(TestValue.BID_STRATEGY) + '",'
                '"' + str(FieldName.BOOSTED_OBJECT_ID) + '":"' + str(TestValue.BOOSTED_OBJECT_ID) + '",'
                '"' + str(FieldName.BRAND_LIFT_STUDIES) + '":' + str(TestValue.BRAND_LIFT_STUDIES) + ','
                '"' + str(FieldName.BUDGET_REBALANCE_FLAG) + '":"' + str(TestValue.BUDGET_REBALANCE_FLAG) + '",'
                '"' + str(FieldName.BUDGET_REMAINING) + '": "' + str(TestValue.BUDGET_REMAINING) + '",'
                '"' + str(FieldName.BUYING_TYPE) + '":"' + str(TestValue.BUYING_TYPE) + '",'
                '"' + str(FieldName.CAN_CREATE_BRAND_LIFT_STUDY) + '":"' + str(TestValue.CAN_CREATE_BRAND_LIFT_STUDY) + '",'
                '"' + str(FieldName.CAN_USE_SPEND_CAP) + '":"' + str(TestValue.CAN_USE_SPEND_CAP) + '",'
                '"' + str(FieldName.CONFIGURED_STATUS) + '":"' + str(TestValue.CONFIGURED_STATUS) + '",'
                '"' + str(FieldName.CREATED_TIME) + '":"' + str(TestValue.CREATED_TIME) + '",'
                '"' + str(FieldName.DAILY_BUDGET) + '":"' + str(TestValue.DAILY_BUDGET) + '",'
                '"' + str(FieldName.EFFECTIVE_STATUS) + '":"' + str(TestValue.EFFECTIVE_STATUS) + '",'
                '"' + str(FieldName.ID) + '": "' + str(TestValue.CAMPAIGN_ID) + '",'
                '"' + str(FieldName.ISSUES_INFO) + '": ' + str(TestValue.ISSUES_INFO) + ','
                '"' + str(FieldName.LAST_BUDGET_TOGGLING_TIME) + '":"' + str(TestValue.LAST_BUDGET_TOGGLING_TIME) + '",'
                '"' + str(FieldName.LIFETIME_BUDGET) + '":"' + str(TestValue.LIFETIME_BUDGET) + '",'
                '"' + str(FieldName.NAME) + '":"' + str(TestValue.NAME) + '",'
                '"' + str(FieldName.OBJECTIVE) + '":"' + str(TestValue.OBJECTIVE) + '",'
                '"' + str(FieldName.RECOMMENDATIONS) + '":' + str(TestValue.RECOMMENDATIONS) + ','
                '"' + str(FieldName.PACING_TYPE) + '":"' + str(TestValue.PACING_TYPE) + '",'
                '"' + str(FieldName.PROMOTED_OBJECT) + '":' + str(TestValue.PROMOTED_OBJECT) + ','
                '"' + str(FieldName.SPECIAL_AD_CATEGORY) + '":"' + str(TestValue.SPECIAL_AD_CATEGORY) + '",'
                '"' + str(FieldName.SPEND_CAP) + '":"' + str(TestValue.SPEND_CAP) + '",'
                '"' + str(FieldName.STATUS) + '":"' + str(TestValue.STATUS) + '",'
                '"' + str(FieldName.TOPLINE_ID) + '":"' + str(TestValue.TOPLINE_ID) + '",'
                '"' + str(FieldName.START_TIME) + '":"' + str(TestValue.START_TIME) + '",'
                '"' + str(FieldName.STOP_TIME) + '":"' + str(TestValue.STOP_TIME) + '",'
                '"' + str(FieldName.UPDATED_TIME) + '":"' + str(TestValue.UPDATED_TIME) + '"'
                '}'
            )

            self.mock_request.return_value = self.mock_response

            # reference : codegen/api_specs/specs/Campaign.json
            fields = [
                FieldName.ACCOUNT_ID,
                FieldName.ADLABELS,
                FieldName.BID_STRATEGY,
                FieldName.BOOSTED_OBJECT_ID,
                FieldName.BRAND_LIFT_STUDIES,
                FieldName.BUDGET_REBALANCE_FLAG,
                FieldName.BUDGET_REMAINING,
                FieldName.BUYING_TYPE,
                FieldName.CAN_CREATE_BRAND_LIFT_STUDY,
                FieldName.CAN_USE_SPEND_CAP,
                FieldName.CONFIGURED_STATUS,
                FieldName.CREATED_TIME,
                FieldName.DAILY_BUDGET,
                FieldName.EFFECTIVE_STATUS,
                FieldName.ID,
                FieldName.ISSUES_INFO,
                FieldName.LAST_BUDGET_TOGGLING_TIME,
                FieldName.LIFETIME_BUDGET,
                FieldName.NAME,
                FieldName.OBJECTIVE,
                FieldName.PACING_TYPE,
                FieldName.PROMOTED_OBJECT,
                FieldName.RECOMMENDATIONS,
                FieldName.SPECIAL_AD_CATEGORY,
                FieldName.SPEND_CAP,
                FieldName.START_TIME,
                FieldName.STATUS,
                FieldName.STOP_TIME,
                FieldName.TOPLINE_ID,
                FieldName.UPDATED_TIME,
            ]
            params = {}

            campaign = Campaign(TestValue.CAMPAIGN_ID).api_get(
                fields=fields,
                params=params,
            )

            assert len(warning) == 0
            assert isinstance(campaign, Campaign)
            assert campaign[FieldName.ACCOUNT_ID] == TestValue.ACCOUNT_ID
            assert campaign[FieldName.ADLABELS] == [json.loads(TestValue.AD_LABEL)]
            assert campaign[FieldName.BID_STRATEGY] == TestValue.BID_STRATEGY
            assert campaign[FieldName.BOOSTED_OBJECT_ID] == TestValue.BOOSTED_OBJECT_ID
            assert campaign[FieldName.BRAND_LIFT_STUDIES] == [json.loads(TestValue.BRAND_LIFT_STUDIES)]
            assert campaign[FieldName.BUDGET_REBALANCE_FLAG] == TestValue.BUDGET_REBALANCE_FLAG
            assert campaign[FieldName.BUDGET_REMAINING] == TestValue.BUDGET_REMAINING
            assert campaign[FieldName.BUYING_TYPE] == TestValue.BUYING_TYPE
            assert campaign[FieldName.CAN_CREATE_BRAND_LIFT_STUDY] == TestValue.CAN_CREATE_BRAND_LIFT_STUDY
            assert campaign[FieldName.CAN_USE_SPEND_CAP] == TestValue.CAN_USE_SPEND_CAP
            assert campaign[FieldName.CONFIGURED_STATUS] == TestValue.CONFIGURED_STATUS
            assert campaign[FieldName.CREATED_TIME] == TestValue.CREATED_TIME
            assert campaign[FieldName.DAILY_BUDGET] == TestValue.DAILY_BUDGET
            assert campaign[FieldName.EFFECTIVE_STATUS] == TestValue.EFFECTIVE_STATUS
            assert campaign[FieldName.ID] == TestValue.CAMPAIGN_ID
            assert campaign[FieldName.ISSUES_INFO] == [json.loads(TestValue.ISSUES_INFO)]
            assert campaign[FieldName.LAST_BUDGET_TOGGLING_TIME] == TestValue.LAST_BUDGET_TOGGLING_TIME
            assert campaign[FieldName.LIFETIME_BUDGET] == TestValue.LIFETIME_BUDGET
            assert campaign[FieldName.NAME] == TestValue.NAME
            assert campaign[FieldName.OBJECTIVE] == TestValue.OBJECTIVE
            assert campaign[FieldName.PACING_TYPE] == [TestValue.PACING_TYPE]
            assert isinstance(campaign[FieldName.PROMOTED_OBJECT], AdPromotedObject)
            assert campaign[FieldName.RECOMMENDATIONS] == [json.loads(TestValue.RECOMMENDATIONS)]
            assert campaign[FieldName.SPECIAL_AD_CATEGORY] == TestValue.SPECIAL_AD_CATEGORY
            assert campaign[FieldName.SPEND_CAP] == TestValue.SPEND_CAP
            assert campaign[FieldName.STATUS] == TestValue.STATUS
            assert campaign[FieldName.START_TIME] == TestValue.START_TIME
            assert campaign[FieldName.STOP_TIME] == TestValue.STOP_TIME
            assert campaign[FieldName.TOPLINE_ID] == TestValue.TOPLINE_ID
            assert campaign[FieldName.UPDATED_TIME] == TestValue.UPDATED_TIME


    def test_get_campaign_with_wrong_fields(self):
        with warnings.catch_warnings(record=True) as warning, self.assertRaises(FacebookRequestError):
            self.mock_response.status_code = StatusCode.ERROR
            self.mock_request.return_value = self.mock_response

            fields = [
                'unexist_field',
            ]
            params = {}

            campaign = Campaign(TestValue.CAMPAIGN_ID).api_get(
                fields=fields,
                params=params,
            )

            assert len(warning) == 1
            assert issubclass(warning[0].category, UserWarning)


    def test_create_campaign(self):
        with warnings.catch_warnings(record=True) as warning:
            self.mock_response.status_code = StatusCode.SUCCESS
            self.mock_response._content = '{"' + str(FieldName.ID) + '":"' + str(TestValue.CAMPAIGN_ID) + '", "success": "true"}'
            self.mock_request.return_value = self.mock_response

            fields = []
            # reference : codegen/api_specs/specs/Campaign.json
            params = {
                FieldName.ADLABELS: [json.loads(TestValue.AD_LABEL)],
                FieldName.BID_STRATEGY: TestValue.BID_STRATEGY,
                FieldName.BUDGET_REBALANCE_FLAG: False,
                FieldName.BUYING_TYPE: TestValue.BUYING_TYPE,
                FieldName.DAILY_BUDGET: TestValue.DAILY_BUDGET,
                FieldName.EXECUTION_OPTIONS: [TestValue.EXECUTION_OPTIONS],
                FieldName.ITERATIVE_SPLIT_TEST_CONFIGS: [json.loads(TestValue.ITERATIVE_SPLIT_TEST_CONFIGS)],
                FieldName.LIFETIME_BUDGET: TestValue.LIFETIME_BUDGET,
                FieldName.NAME: TestValue.NAME,
                FieldName.OBJECTIVE: TestValue.OBJECTIVE,
                FieldName.PACING_TYPE: [TestValue.PACING_TYPE],
                FieldName.PROMOTED_OBJECT: json.loads(TestValue.PROMOTED_OBJECT),
                FieldName.SOURCE_CAMPAIGN_ID: TestValue.CAMPAIGN_ID,
                FieldName.SPECIAL_AD_CATEGORY: TestValue.SPECIAL_AD_CATEGORY,
                FieldName.SPEND_CAP: TestValue.SPEND_CAP,
                FieldName.STATUS: TestValue.STATUS,
                FieldName.TOPLINE_ID: TestValue.TOPLINE_ID,
                FieldName.UPSTREAM_EVENTS: json.loads(TestValue.UPSTREAM_EVENTS),
            }

            campaign = AdAccount(TestValue.ACCOUNT_ID).create_campaign(
                fields,
                params,
            )

            assert len(warning) == 0
            assert isinstance(campaign, Campaign)
            assert campaign[FieldName.ID] == TestValue.CAMPAIGN_ID


    def test_create_campaign_with_wrong_params(self):
        with warnings.catch_warnings(record=True) as warning, self.assertRaises(FacebookRequestError):
            self.mock_response.status_code = StatusCode.ERROR
            self.mock_request.return_value = self.mock_response

            fields = []
            params = {
                'status': 3,
                'special_ad_category': 'wrong_enum',
            }

            campaign = AdAccount(TestValue.ACCOUNT_ID).create_campaign(
                fields,
                params,
            )

            assert len(warning) == 2
            assert issubclass(warning[-1].category, UserWarning)


if __name__ == '__main__':
    unittest.main()
