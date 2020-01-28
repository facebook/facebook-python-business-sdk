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
    python -m facebook_business.test.integration
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

@patch('requests.Session.request')
class CampaignTestCase(IntegrationTestCase):
    campaign_id = 'campaign_id'

    def test_get_campaign(self, mock_request):
        ad_label = '{"name": "test_label"}'
        bid_strategy = 'LOWEST_COST_WITHOUT_CAP'
        iterative_split_test_configs = '{"name": "test_config"}'
        promoted_object = '{"page_id": "page_id"}'
        upstream_events = '{"name": "event_1", "event_id": "10"}'
        recommendations = '{"code": "1772120"}'
        issues_info = (
            '{"level": "AD", "error_code": "1815869",'
            '"error_summary": "Ad post is not available"}'
        )
        self.mock_response.status_code = 200
        self.mock_response._content = (
            '{"account_id": "act_123",'
            '"adlabels": %s,'
            '"bid_strategy": "%s",'
            '"boosted_object_id": "123",'
            '"budget_rebalance_flag": "false",'
            '"budget_remaining": "150",'
            '"buying_type": "AUCTION",'
            '"can_create_brand_lift_study": "true",'
            '"can_use_spend_cap": "true",'
            '"configured_status": "PAUSED",'
            '"created_time": "3728193",'
            '"daily_budget": "100",'
            '"effective_status": "PAUSED",'
            '"id": "campaign_id",'
            '"issues_info": %s,'
            '"last_budget_toggling_time": "3892193",'
            '"lifetime_budget": "10000",'
            '"name": "test_campaign",'
            '"execution_options": "include_recommendations",'
            '"iterative_split_test_configs": %s,'
            '"objective": "LINK_CLICKS",'
            '"recommendations": %s,'
            '"pacing_type": "standard",'
            '"promoted_object": %s,'
            '"special_ad_category": "EMPLOYMENT",'
            '"spend_cap": "922337203685478",'
            '"status": "PAUSED",'
            '"topline_id": "135",'
            '"upstream_events": %s,'
            '"start_time": "3728232",'
            '"stop_time": "3872293"'
            '}'
        ) % (
            ad_label,
            bid_strategy,
            issues_info,
            iterative_split_test_configs,
            recommendations,
            promoted_object,
            upstream_events,
        )

        mock_request.return_value = self.mock_response

        # reference : codegen/api_specs/specs/Campaign.json
        fields = [
            'account_id',
            'adlabels',
            'bid_strategy',
            'boosted_object_id',
            'brand_lift_studies',
            'budget_rebalance_flag',
            'budget_remaining',
            'buying_type',
            'can_create_brand_lift_study',
            'can_use_spend_cap',
            'configured_status',
            'created_time',
            'daily_budget',
            'effective_status',
            'id',
            'issues_info',
            'last_budget_toggling_time',
            'lifetime_budget',
            'name',
            'objective',
            'pacing_type',
            'promoted_object',
            'recommendations',
            'source_campaign',
            'source_campaign_id',
            'special_ad_category',
            'spend_cap',
            'start_time',
            'status',
            'stop_time',
            'topline_id',
            'updated_time',
        ]
        params = {
        }

        campaign = Campaign(self.campaign_id).api_get(
            fields=fields,
            params=params,
        )

        assert isinstance(campaign, Campaign)
        assert campaign['account_id'] == 'act_123'
        assert campaign['bid_strategy'] == 'LOWEST_COST_WITHOUT_CAP'
        assert campaign['adlabels'] == [json.loads(ad_label)]
        assert campaign['budget_rebalance_flag'] == 'false'
        assert campaign['boosted_object_id'] == '123'
        assert campaign['budget_remaining'] == '150'
        assert campaign['buying_type'] == 'AUCTION'
        assert campaign['can_create_brand_lift_study'] == 'true'
        assert campaign['can_use_spend_cap'] == 'true'
        assert campaign['configured_status'] == 'PAUSED'
        assert campaign['created_time'] == '3728193'
        assert campaign['daily_budget'] == '100'
        assert campaign['effective_status'] == 'PAUSED'
        assert campaign['id'] == 'campaign_id'
        assert campaign['issues_info'] == [json.loads(issues_info)]
        assert campaign['last_budget_toggling_time'] == '3892193'
        assert campaign['lifetime_budget'] == '10000'
        assert campaign['execution_options'] == ['include_recommendations']
        assert campaign['iterative_split_test_configs'] == [json.loads(iterative_split_test_configs)]
        assert campaign['name'] == 'test_campaign'
        assert campaign['objective'] == 'LINK_CLICKS'
        assert campaign['recommendations'] == [json.loads(recommendations)]
        assert campaign['pacing_type'] == ['standard']
        assert isinstance(campaign['promoted_object'], AdPromotedObject)
        assert campaign['special_ad_category'] == 'EMPLOYMENT'
        assert campaign['spend_cap'] == '922337203685478'
        assert campaign['status'] == 'PAUSED'
        assert campaign['topline_id'] == '135'
        assert campaign['upstream_events'] == json.loads(upstream_events)
        assert campaign['start_time'] == '3728232'
        assert campaign['stop_time'] == '3872293'

    def test_get_campaign_with_wrong_fields(self, mock_request):

        with warnings.catch_warnings(record=True) as warning, self.assertRaises(FacebookRequestError):
            self.mock_response.status_code = 400
            self.mock_response._content = '{"error": {"message": "(#100) Tried accessing nonexisting field"}}'
            mock_request.return_value = self.mock_response

            fields = [
                'unexist_field',
            ]
            params = {
            }
            campaign = Campaign(self.campaign_id).api_get(
                fields=fields,
                params=params,
            )

            assert len(warning) == 1
            assert issubclass(warning[0].category, UserWarning)


    def test_create_campaign(self, mock_request):

        with warnings.catch_warnings(record=True) as warning:
            self.mock_response.status_code = 200
            self.mock_response._content = '{"id":"campaign_id", "success": "true"}'
            mock_request.return_value = self.mock_response
            fields = []

            # reference : codegen/api_specs/specs/Campaign.json
            params = {
                'adlabels': [{'name': 'test_ad_label'}],
                'bid_strategy': 'LOWEST_COST_WITHOUT_CAP',
                'budget_rebalance_flag': False,
                'buying_type': 'string',
                'daily_budget': 100,
                'execution_options': ["include_recommendations"],
                'iterative_split_test_configs': [{'name':'test_config'}],
                'lifetime_budget': 1000,
                'name': 'string',
                'objective': 'LINK_CLICKS',
                'pacing_type': ["test_pacing_type"],
                'promoted_object': {'name': 'test_page', 'id': 'page_id'},
                'source_campaign_id': 'campaign_id',
                'special_ad_category': 'EMPLOYMENT',
                'spend_cap': 2,
                'status': 'PAUSED',
                'topline_id': 'string',
                'upstream_events': {'key': 'value'},
            }

            campaign = AdAccount('id').create_campaign(fields, params)
            assert len(warning) == 0
            assert isinstance(campaign, Campaign)
            assert campaign['id'] == 'campaign_id'


    def test_create_campaign_with_wrong_params(self, mock_request):

        with warnings.catch_warnings(record=True) as warning, self.assertRaises(FacebookRequestError):
            self.mock_response.status_code = 400
            self.mock_response._content = '{"error": {"message": "(#100) The parameter special_ad_category must be an special_ad_category_enum."}}'
            mock_request.return_value = self.mock_response

            fields = []
            params = {
                'status': 3,
                'special_ad_category': 'wrong_enum',
            }

            campaign = AdAccount('id').create_campaign(fields, params)
            assert len(warning) == 2
            assert issubclass(warning[-1].category, UserWarning)


if __name__ == '__main__':
    unittest.main()
