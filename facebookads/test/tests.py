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
Unit tests for the Python Facebook Ads API SDK.

How to run:
    python -m facebookads.test.tests app_id app_secret access_token account_id
'''

import unittest
import time
import sys
import os

from .. import objects
from .. import api
from .. import session
from .. import exceptions as fbexceptions


class FacebookAdsTestCase(unittest.TestCase):

    TEST_SESSION = None
    TEST_API = None
    TEST_ACCOUNT = None
    TEST_ID = str(int(time.time()) % 1000)
    TEST_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'puget_sound.jpg')

    @classmethod
    def new_test_campaign(cls):
        campaign = cls.TEST_ACCOUNT.child(objects.AdCampaign)
        campaign.update({
            objects.AdCampaign.Field.name: 'AdSetTestCase %s' % cls.TEST_ID
        })

        return campaign

    @classmethod
    def new_test_ad_set(cls, campaign):
        campaign_group_id = campaign.get_id_assured()

        ad_set = cls.TEST_ACCOUNT.child(objects.AdSet)
        ad_set.update({
            objects.AdSet.Field.name: 'AdSetTestCase %s' % cls.TEST_ID,
            objects.AdSet.Field.campaign_group_id: campaign_group_id,
            objects.AdSet.Field.status: objects.AdSet.Status.paused,
            objects.AdSet.Field.daily_budget: 100,
            objects.AdSet.Field.bid_type: objects.AdSet.BidType.cpc,
            objects.AdSet.Field.bid_info: {
                objects.AdSet.Field.BidInfo.clicks: 20,
            },
            objects.AdSet.Field.targeting: {
                objects.TargetingSpecsField.geo_locations: {
                    'countries': [
                        'US',
                    ],
                },
            },
        })

        return ad_set

    @classmethod
    def new_test_ad_group(cls, ad_set):
        campaign_id = ad_set.get_id_assured()

        img = cls.TEST_ACCOUNT.child(objects.AdImage)
        img.remote_create_from_filename(cls.TEST_IMAGE_PATH)
        image_hash = img.get_hash()

        creative = cls.TEST_ACCOUNT.child(objects.AdCreative)
        creative.update({
            objects.AdCreative.Field.title: "Test AdCreative %s" % cls.TEST_ID,
            objects.AdCreative.Field.body: "Test ad",
            objects.AdCreative.Field.object_url: "https://www.facebook.com/",
            objects.AdCreative.Field.image_hash: image_hash,
        })
        creative.remote_create()
        creative_id = creative.get_id_assured()

        ad_group = cls.TEST_ACCOUNT.child(objects.AdGroup)
        ad_group.update({
            objects.AdGroup.Field.name: 'AdGroupTestCase %s' % cls.TEST_ID,
            objects.AdGroup.Field.campaign_id: campaign_id,
            objects.AdGroup.Field.creative: {
                objects.AdGroup.Field.Creative.creative_id: creative_id,
            },
        })

        return ad_group


class AbstractObjectTestCase(FacebookAdsTestCase):

    pass


class AbstractCrudObjectTestCase(AbstractObjectTestCase):

    @classmethod
    def get_mirror(cls, subject):
        '''
        Returns object of same class as subject and with same id.
        '''
        return subject.__class__(subject.get_id())

    @classmethod
    def assert_can_create(cls, subject):
        '''Tests if object can be created.
        It asserts that id is empty before creation, and populated after.
        '''
        assert subject.__class__.Field.id not in subject

        subject.remote_create()

        assert subject.__class__.Field.id in subject

    @classmethod
    def assert_can_read(cls, subject):
        '''Tests if object can be read.
        Reads default fields of subject and sees if subject matches with its
        mirror in all the subject's fields.
        '''
        assert subject.__class__.Field.id in subject

        fields_to_read = subject.get_default_read_fields()

        subject.remote_read(fields=fields_to_read)

        for field in fields_to_read:
            assert field in subject

        mirror = cls.get_mirror(subject)
        mirror.remote_read(fields=fields_to_read)
        for field in fields_to_read:
            assert subject[field] == mirror[field]

    @classmethod
    def assert_can_update(cls, subject):
        assert subject.__class__.Field.id in subject

        subject.remote_update()

        fields_to_read = subject.get_default_read_fields()
        mirror = cls.get_mirror(subject)
        mirror.remote_read(fields=fields_to_read)
        for field in fields_to_read:
            assert subject[field] == mirror[field]

    @classmethod
    def assert_can_delete(cls, subject):
        assert subject.__class__.Field.id in subject

        subject.remote_delete()

        assert subject.__class__.Field.id not in subject


class AdUserTestCase(AbstractCrudObjectTestCase):

    @classmethod
    def setUpClass(cls):
        objects.AdUser.set_default_read_fields([
            objects.AdUser.Field.name,
        ])

    def runTest(self):
        self.subject = objects.AdUser('me')

        self.assert_can_read(self.subject)

        for user in self.TEST_ACCOUNT.get_ad_users(
            fields=[objects.AdUser.Field.role]
        ):
            if user == self.subject:
                valid_roles = (
                    objects.AdUser.Role.administrator,
                    objects.AdUser.Role.manager,
                )
                assert user[objects.AdUser.Field.role] in valid_roles


class AdAccountTestCase(AbstractCrudObjectTestCase):

    @classmethod
    def setUpClass(cls):
        objects.AdAccount.set_default_read_fields([
            objects.AdAccount.Field.account_status,
            objects.AdAccount.Field.business_name,
            objects.AdAccount.Field.timezone_name,
            objects.AdAccount.Field.daily_spend_limit,
        ])

    def runTest(self):
        self.subject = self.get_mirror(self.TEST_ACCOUNT)
        self.assert_can_read(self.subject)


class AdCampaignTestCase(AbstractCrudObjectTestCase):

    @classmethod
    def setUpClass(cls):
        objects.AdCampaign.set_default_read_fields([
            objects.AdCampaign.Field.name,
        ])

    def runTest(self):
        self.subject = self.new_test_campaign()

        self.assert_can_create(self.subject)

        self.assert_can_read(self.subject)

        self.subject.update({
            objects.AdCampaign.Field.name: 'AdCampaignTestCase Updated %s'
                                           % self.TEST_ID
        })
        self.assert_can_update(self.subject)

        self.assert_can_delete(self.subject)


class AdSetTestCase(AbstractCrudObjectTestCase):

    @classmethod
    def setUpClass(cls):
        objects.AdSet.set_default_read_fields([
            objects.AdSet.Field.daily_budget,
            objects.AdSet.Field.created_time,
            objects.AdSet.Field.campaign_group_id,
            objects.AdSet.Field.bid_type,
            objects.AdSet.Field.name,
        ])

    def runTest(self):
        self.campaign = self.new_test_campaign()
        self.campaign.remote_create()

        self.subject = self.new_test_ad_set(self.campaign)

        self.assert_can_create(self.subject)

        self.assert_can_read(self.subject)

        self.subject.update({
            objects.AdSet.Field.name: 'AdSetTestCase Updated %s' % self.TEST_ID,
        })
        self.assert_can_update(self.subject)

        self.assert_can_delete(self.subject)
        self.campaign.remote_delete()

    def tearDown(self):
        try:
            self.subject.remote_delete()
        except fbexceptions.FacebookBadObjectError:
            pass

        try:
            self.campaign.remote_delete()
        except fbexceptions.FacebookBadObjectError:
            pass


class AdGroupTestCase(AbstractCrudObjectTestCase):

    @classmethod
    def setUpClass(cls):
        objects.AdGroup.set_default_read_fields([
            objects.AdGroup.Field.created_time,
            objects.AdGroup.Field.name,
            objects.AdGroup.Field.campaign_id,
        ])

    def runTest(self):
        self.campaign = self.new_test_campaign()
        self.campaign.remote_create()
        self.ad_set = self.new_test_ad_set(self.campaign)
        self.ad_set.remote_create()

        self.subject = self.new_test_ad_group(self.ad_set)

        self.assert_can_create(self.subject)

        self.assert_can_read(self.subject)

        self.subject.update({
            objects.AdGroup.Field.name: 'AdGroupTestCase Updated %s' % (
                self.TEST_ID
            ),
        })
        self.assert_can_update(self.subject)

        self.assert_can_delete(self.subject)

        self.ad_set.remote_delete()
        self.campaign.remote_delete()

    def tearDown(self):
        try:
            self.subject.remote_delete()
        except fbexceptions.FacebookBadObjectError:
            pass

        try:
            self.ad_set.remote_delete()
        except fbexceptions.FacebookBadObjectError:
            pass

        try:
            self.campaign.remote_delete()
        except fbexceptions.FacebookBadObjectError:
            pass


if __name__ == '__main__':
    test_account_id = sys.argv.pop()
    access_token = sys.argv.pop()
    app_secret = sys.argv.pop()
    app_id = sys.argv.pop()

    FacebookAdsTestCase.TEST_SESSION = session.FacebookSession(
        app_id,
        app_secret,
        access_token
    )
    FacebookAdsTestCase.TEST_API = api.FacebookAdsApi(
        FacebookAdsTestCase.TEST_SESSION
    )
    api.FacebookAdsApi.set_default_api(FacebookAdsTestCase.TEST_API)

    if 'act_' not in test_account_id:
        test_account_id = 'act_' + test_account_id
    FacebookAdsTestCase.TEST_ACCOUNT = objects.AdAccount(test_account_id)

    unittest.main()
