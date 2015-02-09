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
Integration tests for the Python Facebook Ads API SDK.

How to run:
    python -m facebookads.test.integration access_token
'''

import unittest
import time
import sys
import os
import json

from .. import objects
from .. import specs
from .. import api
from .. import session
from .. import exceptions as fbexceptions


class FacebookAdsTestCase(unittest.TestCase):

    TEST_SESSION = None
    TEST_API = None
    TEST_ACCOUNT = None
    TEST_ID = str(int(time.time()) % 1000)
    TEST_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'test.png')

    def setUp(self):
        super(FacebookAdsTestCase, self).setUp()
        self.remote_objects = []

    def tearDown(self):
        self.delete_remote_objects()
        super(FacebookAdsTestCase, self).tearDown()

    def delete_remote_objects(self):
        """
        Delete accumulated remote objects.
        """
        for o in reversed(self.remote_objects):
            if o.Field.id in o and o.get_id() is not None:
                try:
                    o.remote_delete()
                except Exception:
                    if isinstance(o, objects.AdImage):
                        # AdImages are often reused automatically since the
                        # hash is unique. They can't be deleted until all the
                        # references are cleaned up.
                        pass
                    else:
                        # Error out the test if an object can't be deleted,
                        # since this probably indicates a coding issue in the
                        # tests.
                        raise

    def delete_in_teardown(self, obj):
        """
        Prepare to delete obj in tearDown.
        """
        self.remote_objects.append(obj)

    def new_test_ad_creative(self):
        creative = objects.AdCreative(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(creative)
        creative.update({
            objects.AdCreative.Field.name: ('AdCreativeTestCase %s' %
                                            self.TEST_ID),
        })

        return creative

    def new_test_ad_campaign(self):
        campaign = objects.AdCampaign(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(campaign)
        campaign.update({
            objects.AdCampaign.Field.name: 'AdSetTestCase %s' % self.TEST_ID,
        })

        return campaign

    def new_test_ad_set(self, campaign):
        campaign_group_id = campaign.get_id_assured()

        ad_set = objects.AdSet(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(ad_set)
        ad_set.update({
            objects.AdSet.Field.name: 'AdSetTestCase %s' % self.TEST_ID,
            objects.AdSet.Field.campaign_group_id: campaign_group_id,
            objects.AdSet.Field.status: objects.AdSet.Status.paused,
            objects.AdSet.Field.pacing_type: [
                objects.AdSet.PacingType.standard,
            ],
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

    def new_test_ad_group(self, ad_set):
        campaign_id = ad_set.get_id_assured()

        img = objects.AdImage(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(img)
        img[objects.AdImage.Field.filename] = self.TEST_IMAGE_PATH
        img.remote_create()
        image_hash = img.get_hash()

        creative = objects.AdCreative(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(creative)
        creative.update({
            objects.AdCreative.Field.title: "Test AdCreative %s" % self.TEST_ID,
            objects.AdCreative.Field.body: "Test ad",
            objects.AdCreative.Field.object_url: "https://www.facebook.com/",
            objects.AdCreative.Field.image_hash: image_hash,
        })
        creative.remote_create()
        creative_id = creative.get_id_assured()

        ad_group = objects.AdGroup(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(ad_group)
        ad_group.update({
            objects.AdGroup.Field.name: 'AdGroupTestCase %s' % self.TEST_ID,
            objects.AdGroup.Field.campaign_id: campaign_id,
            objects.AdGroup.Field.creative: {
                objects.AdGroup.Field.Creative.creative_id: creative_id,
            },
            objects.AdGroup.Field.status: objects.AdGroup.Status.paused,
        })

        return ad_group

    def new_test_ad_image(self):
        img = objects.AdImage(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(img)
        img[objects.AdImage.Field.filename] = self.TEST_IMAGE_PATH
        img.remote_create()
        return img


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
        assert subject[subject.Field.id] is None

        subject.remote_create()

        assert subject[subject.Field.id] is not None

    @classmethod
    def assert_can_read(cls, subject):
        '''Tests if object can be read.
        Reads default fields of subject and sees if subject matches with its
        mirror in all the subject's fields.
        '''
        assert subject.Field.id in subject

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
        assert subject.Field.id in subject

        subject.remote_update()

        fields_to_read = subject.get_default_read_fields()
        mirror = cls.get_mirror(subject)
        mirror.remote_read(fields=fields_to_read)
        for field in fields_to_read:
            assert subject[field] == mirror[field]

    @classmethod
    def assert_can_delete(cls, subject):
        assert subject.Field.id in subject

        subject.remote_delete()

        if hasattr(subject.Field, 'status'):
            subject.remote_read(fields=[subject.Field.status])
            assert subject[subject.Field.status] == 'DELETED'
        else:
            assert subject.Field.id not in subject

    @classmethod
    def assert_can_archive(cls, subject):
        assert subject.Field.id in subject

        subject.remote_archive()

        subject.remote_read(fields=[subject.Field.status])
        assert subject[subject.Field.status] == 'ARCHIVED'

    @classmethod
    def assert_can_validate(cls, subject):
        assert 'execution_options' not in subject
        cached_data = dict(subject)
        subject.remote_validate()
        assert 'execution_options' not in subject
        assert cached_data == subject._data


class AdUserTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(AdUserTestCase, self).setUp()
        self.orig_aduser_fields = objects.AdUser.get_default_read_fields()
        objects.AdUser.set_default_read_fields([
            objects.AdUser.Field.name,
        ])

    def tearDown(self):
        objects.AdUser.set_default_read_fields(self.orig_aduser_fields)
        super(AdUserTestCase, self).tearDown()

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

    def setUp(self):
        super(AdAccountTestCase, self).setUp()
        self.orig_adaccount_fields = objects.AdAccount.get_default_read_fields()
        objects.AdAccount.set_default_read_fields([
            objects.AdAccount.Field.account_status,
            objects.AdAccount.Field.business_name,
            objects.AdAccount.Field.timezone_name,
            objects.AdAccount.Field.daily_spend_limit,
        ])

    def tearDown(self):
        objects.AdAccount.set_default_read_fields(self.orig_adaccount_fields)
        super(AdAccountTestCase, self).tearDown()

    def runTest(self):
        self.subject = self.get_mirror(self.TEST_ACCOUNT)
        self.assert_can_read(self.subject)


class AdCampaignTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(AdCampaignTestCase, self).setUp()
        self.orig_adcampaign_fields = \
            objects.AdCampaign.get_default_read_fields()
        objects.AdCampaign.set_default_read_fields([
            objects.AdCampaign.Field.name,
        ])

    def tearDown(self):
        objects.AdCampaign.set_default_read_fields(self.orig_adcampaign_fields)
        super(AdCampaignTestCase, self).tearDown()

    def runTest(self):
        self.subject = self.new_test_ad_campaign()

        self.assert_can_validate(self.subject)

        self.assert_can_create(self.subject)

        self.assert_can_read(self.subject)

        self.subject.update({
            objects.AdCampaign.Field.name: 'AdCampaignTestCase Updated %s'
                                           % self.TEST_ID
        })
        self.assert_can_update(self.subject)

        self.assert_can_archive(self.subject)

        self.assert_can_delete(self.subject)


class GetByIDsTestCase(AbstractCrudObjectTestCase):

    def runTest(self):
        self.campaign1 = self.new_test_ad_campaign()
        self.campaign1['name'] = "Campaign 1"
        self.campaign1.remote_create()
        self.campaign2 = self.new_test_ad_campaign()
        self.campaign2['name'] = "Campaign 2"
        self.campaign2.remote_create()

        campaigns = objects.AdCampaign.get_by_ids(
            ids=[self.campaign1.get_id(), self.campaign2.get_id()],
            fields=['name']
        )

        assert len(campaigns) == 2
        assert (sorted(c['name'] for c in campaigns) ==
                ['Campaign 1', 'Campaign 2'])


class DefaultReadFieldsTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(DefaultReadFieldsTestCase, self).setUp()
        self.orig_adcampaign_fields = \
            objects.AdCampaign.get_default_read_fields()

    def tearDown(self):
        objects.AdCampaign.set_default_read_fields(self.orig_adcampaign_fields)
        super(DefaultReadFieldsTestCase, self).tearDown()

    def runTest(self):
        campaign = self.new_test_ad_campaign()
        campaign.remote_create()
        same_campaign = objects.AdCampaign(campaign.get_id())
        same_campaign.remote_read()
        assert objects.AdCampaign.Field.status not in same_campaign

        campaigns = objects.AdCampaign.get_by_ids(ids=[campaign.get_id()])
        assert objects.AdCampaign.Field.status not in campaigns[0]

        objects.AdCampaign.set_default_read_fields([
            objects.AdCampaign.Field.status,
        ])
        same_campaign.remote_read()
        assert objects.AdCampaign.Field.status in same_campaign

        campaigns = objects.AdCampaign.get_by_ids(ids=[campaign.get_id()])
        assert objects.AdCampaign.Field.status in campaigns[0]


class AdSetTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(AdSetTestCase, self).setUp()
        self.orig_adset_fields = objects.AdSet.get_default_read_fields()
        objects.AdSet.set_default_read_fields([
            objects.AdSet.Field.daily_budget,
            objects.AdSet.Field.created_time,
            objects.AdSet.Field.campaign_group_id,
            objects.AdSet.Field.bid_type,
            objects.AdSet.Field.name,
        ])

    def tearDown(self):
        objects.AdSet.set_default_read_fields(self.orig_adset_fields)
        super(AdSetTestCase, self).tearDown()

    def runTest(self):
        self.campaign = self.new_test_ad_campaign()
        self.campaign.remote_create()

        self.subject = self.new_test_ad_set(self.campaign)

        self.assert_can_validate(self.subject)

        self.assert_can_create(self.subject)

        self.assert_can_read(self.subject)

        self.subject.update({
            objects.AdSet.Field.name: 'AdSetTestCase Updated %s' % self.TEST_ID,
        })
        self.assert_can_update(self.subject)

        self.assert_can_archive(self.subject)

        self.assert_can_delete(self.subject)


class AdGroupTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(AdGroupTestCase, self).setUp()
        self.orig_adgroup_fields = objects.AdGroup.get_default_read_fields()
        objects.AdGroup.set_default_read_fields([
            objects.AdGroup.Field.created_time,
            objects.AdGroup.Field.name,
            objects.AdGroup.Field.campaign_id,
        ])

    def tearDown(self):
        objects.AdGroup.set_default_read_fields(self.orig_adgroup_fields)
        super(AdGroupTestCase, self).tearDown()

    def runTest(self):
        self.campaign = self.new_test_ad_campaign()
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

        self.assert_can_archive(self.subject)

        self.assert_can_delete(self.subject)


class CustomAudienceTestCase(AbstractCrudObjectTestCase):

    def runTest(self):
        ca = objects.CustomAudience(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(ca)
        ca[objects.CustomAudience.Field.name] = \
            'Custom Audience Test ' + self.TEST_ID
        ca.remote_create()

        users = ['someone@example.com']

        try:
            ca.add_users(objects.CustomAudience.Schema.email_hash, users)
        except:
            self.fail("Could not add users")

        try:
            ca.remove_users(objects.CustomAudience.Schema.email_hash, users)
        except:
            self.fail("Could not remove users")


class MultiProductAdObjectStorySpecTestCase(AbstractCrudObjectTestCase):

    def runTest(self):
        creative = self.new_test_ad_creative()
        creative[objects.AdCreative.Field.name] = 'MPA Creative'

        story = specs.ObjectStorySpec()
        story[story.Field.page_id] = self.PAGE_ID

        link = specs.LinkData()
        link[link.Field.link] = 'https://www.facebook.com'
        link[link.Field.caption] = 'My Caption'

        img = objects.AdImage(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(img)
        img[objects.AdImage.Field.filename] = self.TEST_IMAGE_PATH
        img.remote_create()

        product1 = specs.AttachmentData()
        product1.update({
            specs.AttachmentData.Field.link: 'https://www.facebook.com',
            specs.AttachmentData.Field.image_hash: img.get_hash(),
            specs.AttachmentData.Field.name: 'Product 1',
            specs.AttachmentData.Field.description: '$100',
        })

        product2 = specs.AttachmentData()
        product2.update({
            specs.AttachmentData.Field.link: 'https://www.facebook.com',
            specs.AttachmentData.Field.image_hash: img.get_hash(),
            specs.AttachmentData.Field.name: 'Product 2',
            specs.AttachmentData.Field.description: '$200',
        })

        product3 = specs.AttachmentData()
        product3.update({
            specs.AttachmentData.Field.link: 'https://www.facebook.com',
            specs.AttachmentData.Field.image_hash: img.get_hash(),
            specs.AttachmentData.Field.name: 'Product 3',
            specs.AttachmentData.Field.description: '$300',
        })

        link[link.Field.child_attachments] = [product1, product2, product3]
        story[story.Field.link_data] = link
        creative[creative.Field.object_story_spec] = story

        self.assert_can_create(creative)
        self.assert_can_delete(creative)


class BlameFieldSpecsTestCase(AbstractCrudObjectTestCase):
    def runTest(self):
        set = objects.AdSet(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(set)
        set['name'] = 'foo'
        set['daily_budget'] = 100
        set['campaign_status'] = 100

        try:
            set.remote_create()
        except fbexceptions.FacebookRequestError as e:
            assert e.api_blame_field_specs() == [['campaign_group_id']]
        else:
            self.fail("remote_create unexpectedly succeeded")


class AdImageTestCase(AbstractCrudObjectTestCase):

    def test_can_read(self):
        self.new_test_ad_image()
        self.TEST_ACCOUNT.get_ad_images()


class BatchTestCase(FacebookAdsTestCase):

    def setUp(self):
        self.created_ids = []
        self.num_campaigns = 5
        super(BatchTestCase, self).setUp()

    def create_campaigns(self):
        ret_val = []
        for i in range(self.num_campaigns):
            campaign = self.new_test_ad_campaign()
            ret_val.append(campaign)
            self.delete_in_teardown(campaign)
        return ret_val

    def check_ids(self, campaigns):
        # Check if the campaigns were created by counting distinct ids
        ids = set(filter(None, [campaign[objects.AdCampaign.Field.id]
                                for campaign in campaigns]))
        self.created_ids.append(ids)
        self.assertEqual(len(ids), len(campaigns))

    def check_batch_size(self, batch):
        # Make sure the calls went into the batch, not executed directly
        self.assertEqual(len(batch), self.num_campaigns)

    def execute_batch(self, batch, max_tries):
        # Avoid a flaky test by retrying the batch calls if needed
        for i in range(max_tries):
            if batch:
                batch = batch.execute()
            else:
                break

    def test_batch_call(self):
        campaigns = self.create_campaigns()
        batch = FacebookAdsTestCase.TEST_API.new_batch()
        for campaign in campaigns:
            campaign.remote_create(batch=batch)
        self.check_batch_size(batch)
        self.execute_batch(batch, self.num_campaigns)
        self.check_ids(campaigns)


if __name__ == '__main__':
    try:
        config_file = open('./config.json')
    except IOError:
        print("No config file found, skipping integration tests")
        sys.exit()

    config = json.load(config_file)
    config_file.close()

    test_account_id = config['act_id']
    page_id = config['page_id']
    app_id = config['app_id']
    app_secret = config['app_secret']

    if 'access_token' in config:
        access_token = config['access_token']
    else:
        if len(sys.argv) < 2:
            raise TypeError("Please provide the access token as an argument")

        access_token = sys.argv.pop()

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
    FacebookAdsTestCase.PAGE_ID = page_id

    unittest.main()
