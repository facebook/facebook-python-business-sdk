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
Integration tests for the Python Facebook Business SDK.

How to run:
    python -m facebook_business.test.integration access_token
'''

import unittest
import time
import sys
import os
import json

from .. import objects
from .. import specs
from .. import api
from .. import apiconfig
from .. import session
from .. import exceptions as fbexceptions

class FacebookAdsTestCase(unittest.TestCase):

    TEST_SESSION = None
    TEST_API = None
    TEST_BUSINESS = None
    TEST_ACCOUNT = None
    TEST_ID = str(int(time.time()) % 1000)
    TEST_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'misc/image.png')
    TEST_ZIP_PATH = os.path.join(os.path.dirname(__file__), 'misc/images.zip')
    TEST_SECONDARY_ACCOUNT = None
    TEST_SECONDARY_BUSINESS = None

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

    def new_test_campaign(self):
        campaign = objects.Campaign(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(campaign)
        campaign.update({
            objects.Campaign.Field.name: 'CampaignTestCase %s' % self.TEST_ID,
        })

        return campaign

    def new_test_ad_set(self, campaign):
        campaign_id = campaign.get_id_assured()

        ad_set = objects.AdSet(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(ad_set)
        ad_set.update({
            objects.AdSet.Field.name: 'AdSetTestCase %s' % self.TEST_ID,
            objects.AdSet.Field.campaign_id: campaign_id,
            'status': objects.AdSet.Status.paused,
            objects.AdSet.Field.pacing_type: [
                objects.AdSet.PacingType.standard,
            ],
            objects.AdSet.Field.daily_budget: 2500,
            objects.AdSet.Field.optimization_goal:
            objects.AdSet.OptimizationGoal.impressions,
            objects.AdSet.Field.billing_event:
            objects.AdSet.BillingEvent.impressions,
            objects.AdSet.Field.bid_amount: 500,
            objects.AdSet.Field.targeting: {
                objects.TargetingSpecsField.geo_locations: {
                    'countries': [
                        'US',
                    ],
                },
            },
        })

        return ad_set

    def new_test_ad(self, ad_set):
        adset_id = ad_set.get_id_assured()

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
            objects.AdCreative.Field.title:
                "Test AdCreative %s" % self.TEST_ID,
            objects.AdCreative.Field.body: "Test ad",
            objects.AdCreative.Field.object_url: "https://www.facebook.com/",
            objects.AdCreative.Field.image_hash: image_hash,
        })
        creative.remote_create()
        creative_id = creative.get_id_assured()

        ad = objects.Ad(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(ad)
        ad.update({
            objects.Ad.Field.name: 'AdTestCase %s' % self.TEST_ID,
            objects.Ad.Field.adset_id: adset_id,
            objects.Ad.Field.creative: {
                'creative_id': creative_id,
            },
            'status': objects.Ad.Status.paused,
        })

        return ad

    def new_test_ad_image(self):
        img = objects.AdImage(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(img)
        img[objects.AdImage.Field.filename] = self.TEST_IMAGE_PATH
        img.remote_create()
        return img

    def new_test_ad_label(self):
        label = objects.AdLabel(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        label[objects.AdLabel.Field.name] = 'Test Label'
        label.remote_create()
        self.delete_in_teardown(label)
        return label

    def new_test_pixel(self):
        account = objects.AdAccount(self.TEST_ACCOUNT.get_id_assured())
        pixels = account.get_ads_pixels()

        if len(pixels) > 0:
            return pixels[0]

        pixel = objects.AdsPixel(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        pixel[objects.AdsPixel.Field.name] = 'My new Pixel'
        pixel.remote_create()
        return pixel


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

    @classmethod
    def assert_can_save(cls, subject):
        """
        Asserts that the id is empty before creation and then updates
        """
        assert subject[subject.Field.id] is None

        subject.remote_save()

        assert subject[subject.Field.id] is not None

        subject.remote_save()

        mirror = cls.get_mirror(subject)

        assert subject[subject.Field.id] == mirror[mirror.Field.id]

    def test_can_select_api_version(self):
        image_file = os.path.join(os.path.dirname(__file__), 'test.png')

        test_image_one = objects.AdImage(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )

        test_image_one[objects.AdImage.Field.filename] = image_file

        assert test_image_one.remote_create(
            api_version=apiconfig.ads_api_config['API_VERSION']) is not None

        test_image_two = objects.AdImage(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )

        test_image_two[objects.AdImage.Field.filename] = image_file

        try:
            test_image_two.remote_create(
                api_version=apiconfig.ads_api_config['API_VERSION'])
        except fbexceptions.FacebookBadObjectError as e:
            assert e is not None


class AdUserTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(AdUserTestCase, self).setUp()
        self.orig_aduser_fields = objects.AdUser.get_default_read_fields()
        objects.AdUser.set_default_read_fields(
            [
                objects.AdUser.Field.name,
            ],
        )

    def tearDown(self):
        objects.AdUser.set_default_read_fields(self.orig_aduser_fields)
        super(AdUserTestCase, self).tearDown()

    def runTest(self):
        self.subject = objects.AdUser('me')

        self.assert_can_read(self.subject)

        for user in self.TEST_ACCOUNT.get_ad_users(
            fields=[objects.AdUser.Field.role],
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
        self.orig_adaccount_fields = \
            objects.AdAccount.get_default_read_fields()
        objects.AdAccount.set_default_read_fields(
            [
                objects.AdAccount.Field.account_status,
                objects.AdAccount.Field.business_name,
                objects.AdAccount.Field.timezone_name,
            ],
        )

    def tearDown(self):
        objects.AdAccount.set_default_read_fields(self.orig_adaccount_fields)
        super(AdAccountTestCase, self).tearDown()

    def runTest(self):
        self.subject = self.get_mirror(self.TEST_ACCOUNT)
        self.assert_can_read(self.subject)


class CampaignTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(CampaignTestCase, self).setUp()
        self.orig_campaign_fields = \
            objects.Campaign.get_default_read_fields()
        objects.Campaign.set_default_read_fields(
            [
                objects.Campaign.Field.name,
            ],
        )

    def tearDown(self):
        objects.Campaign.set_default_read_fields(self.orig_campaign_fields)
        super(CampaignTestCase, self).tearDown()

    def runTest(self):
        self.subject = self.new_test_campaign()

        self.assert_can_validate(self.subject)

        self.assert_can_create(self.subject)

        self.assert_can_read(self.subject)

        self.subject.update({
            objects.Campaign.Field.name:
                'CampaignTestCase Updated %s' % self.TEST_ID,
        })
        self.assert_can_update(self.subject)

        self.assert_can_archive(self.subject)

        self.assert_can_delete(self.subject)


class GetByIDsTestCase(AbstractCrudObjectTestCase):

    def runTest(self):
        self.campaign1 = self.new_test_campaign()
        self.campaign1['name'] = "Campaign 1"
        self.campaign1.remote_create()
        self.campaign2 = self.new_test_campaign()
        self.campaign2['name'] = "Campaign 2"
        self.campaign2.remote_create()

        campaigns = objects.Campaign.get_by_ids(
            ids=[self.campaign1.get_id(), self.campaign2.get_id()],
            fields=['name'],
        )

        assert len(campaigns) == 2
        assert (sorted(c['name'] for c in campaigns) ==
                ['Campaign 1', 'Campaign 2'])


class DefaultReadFieldsTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(DefaultReadFieldsTestCase, self).setUp()
        self.orig_campaign_fields = \
            objects.Campaign.get_default_read_fields()

    def tearDown(self):
        objects.Campaign.set_default_read_fields(self.orig_campaign_fields)
        super(DefaultReadFieldsTestCase, self).tearDown()

    def runTest(self):
        campaign = self.new_test_campaign()
        campaign.remote_create()
        same_campaign = objects.Campaign(campaign.get_id())
        same_campaign.remote_read()
        assert objects.Campaign.Field.status not in same_campaign

        campaigns = objects.Campaign.get_by_ids(ids=[campaign.get_id()])
        assert objects.Campaign.Field.status not in campaigns[0]

        objects.Campaign.set_default_read_fields(
            [
                objects.Campaign.Field.status,
            ],
        )
        same_campaign.remote_read()
        assert objects.Campaign.Field.status in same_campaign

        campaigns = objects.Campaign.get_by_ids(ids=[campaign.get_id()])
        assert objects.Campaign.Field.status in campaigns[0]


class AdSetTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(AdSetTestCase, self).setUp()
        self.orig_adset_fields = objects.AdSet.get_default_read_fields()
        objects.AdSet.set_default_read_fields(
            [
                objects.AdSet.Field.daily_budget,
                objects.AdSet.Field.created_time,
                objects.AdSet.Field.campaign_id,
                objects.AdSet.Field.name,
            ],
        )

    def tearDown(self):
        objects.AdSet.set_default_read_fields(self.orig_adset_fields)
        super(AdSetTestCase, self).tearDown()

    def runTest(self):
        self.campaign = self.new_test_campaign()
        self.campaign.remote_create()

        self.subject = self.new_test_ad_set(self.campaign)

        self.assert_can_validate(self.subject)

        self.assert_can_create(self.subject)

        self.assert_can_read(self.subject)

        self.subject.update({
            objects.AdSet.Field.name:
                'AdSetTestCase Updated %s' % self.TEST_ID,
        })
        self.assert_can_update(self.subject)

        self.assert_can_archive(self.subject)

        self.assert_can_delete(self.subject)


class AdTestCase(AbstractCrudObjectTestCase):

    def setUp(self):
        super(AdTestCase, self).setUp()
        self.orig_ad_fields = objects.Ad.get_default_read_fields()
        objects.Ad.set_default_read_fields(
            [
                objects.Ad.Field.created_time,
                objects.Ad.Field.name,
                objects.Ad.Field.adset_id,
            ],
        )

    def tearDown(self):
        objects.Ad.set_default_read_fields(self.orig_ad_fields)
        super(AdTestCase, self).tearDown()

    def runTest(self):
        self.campaign = self.new_test_campaign()
        self.campaign.remote_create()

        self.ad_set = self.new_test_ad_set(self.campaign)
        self.ad_set.remote_create()

        self.subject = self.new_test_ad(self.ad_set)

        self.assert_can_create(self.subject)

        self.assert_can_read(self.subject)

        self.subject.update({
            objects.Ad.Field.name: 'AdTestCase Updated %s' % (
                self.TEST_ID
            ),
        })
        self.assert_can_update(self.subject)

        self.assert_can_archive(self.subject)

        self.assert_can_delete(self.subject)


class TargetingSearchTestCase(AbstractObjectTestCase):
    def test_call(self):
        params = {
            'q': 'uk',
            'type': 'adgeolocation',
            'location_types': ['country'],
        }
        resp = objects.TargetingSearch.search(params=params)
        assert len(resp) > 0


class CustomAudienceTestCase(AbstractCrudObjectTestCase):

    def runTest(self):
        ca = objects.CustomAudience(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        self.delete_in_teardown(ca)
        ca[objects.CustomAudience.Field.name] = \
            'Custom Audience Test ' + self.TEST_ID
        ca[objects.CustomAudience.Field.subtype] = 'CUSTOM'
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


class AdImageTestCase(AbstractCrudObjectTestCase):

    def test_can_upload_zip(self):
        images = objects.AdImage.remote_create_from_zip(
            filename=self.TEST_ZIP_PATH,
            parent_id=self.TEST_ACCOUNT.get_id(),
        )
        assert len(images) == 2

    def test_can_read(self):
        self.new_test_ad_image()
        self.TEST_ACCOUNT.get_ad_images()


class InsightsTestCase(AbstractCrudObjectTestCase):
    def test_can_read_without_job(self):
        self.TEST_ACCOUNT.get_insights(
            fields=[
                objects.Insights.Field.unique_clicks,
                objects.Insights.Field.impressions,
                objects.Insights.Field.campaign_id,
                objects.Insights.Field.campaign_name,
            ],
            params={
                'date_preset': objects.Insights.Preset.today,
                'level': objects.Insights.Level.campaign,
            },
        )


class AdLabelTestCase(AbstractCrudObjectTestCase):
    """
        Create a new ad set object and test adding and removing labels
    """
    def runTest(self):
        label = self.new_test_ad_label()
        adlabels = [label.get_id()]
        ad_set = self.new_test_ad_set()

        try:
            ad_set.add_labels(adlabels)
        except:
            self.fail("Could not add ad labels")

        try:
            ad_set.remove_labels(adlabels)
        except:
            self.fail("Could not remove ad labels")


class AdsPixelTestCase(AbstractCrudObjectTestCase):

    def runTest(self):
        pixel = self.new_test_pixel()

        pixel.share_pixel(
            self.TEST_BUSINESS.get_id(),
            self.TEST_SECONDARY_ACCOUNT.get_id(),
        )

        pixel.unshare_pixel_from_ad_account(
            self.TEST_BUSINESS.get_id(),
            self.TEST_SECONDARY_ACCOUNT.get_id(),
        )

        pixel.share_pixel_with_ad_account(
            self.TEST_BUSINESS.get_id(),
            self.TEST_SECONDARY_ACCOUNT.get_id(),
        )

        old_resp = pixel.list_ad_accounts(
            self.TEST_BUSINESS.get_id(),
        )

        resp = pixel.get_ad_accounts(
            self.TEST_BUSINESS.get_id(),
        )

        assert len(old_resp) > 1
        assert len(resp) > 1

        pixel.share_pixel_agencies(
            self.TEST_BUSINESS.get_id(),
            self.TEST_SECONDARY_BUSINESS.get_id(),
        )

        pixel.unshare_pixel_from_agency(
            self.TEST_BUSINESS.get_id(),
            self.TEST_SECONDARY_BUSINESS.get_id(),
        )

        pixel.share_pixel_with_agency(
            self.TEST_BUSINESS.get_id(),
            self.TEST_SECONDARY_BUSINESS.get_id(),
        )

        old_resp = pixel.list_shared_agencies()
        resp = pixel.get_agencies()

        assert len(old_resp) > 1
        assert len(resp) > 1


class CustomConversion(AbstractCrudObjectTestCase):

    @unittest.skip('Deletion is not supported')
    def runTest(self):
        pixel = self.new_test_pixel()
        custom_conversion = objects.CustomConversion(
            parent_id=self.TEST_ACCOUNT.get_id_assured(),
        )
        custom_conversion.update({
            objects.CustomConversion.Field.name: 'Example Custom Conversion',
            objects.CustomConversion.Field.pixel_id:
            pixel[objects.AdsPixel.id],
            objects.CustomConversion.Field.pixel_rule: {
                'url': {'i_contains': 'thankyou.html'},
            },
            objects.CustomConversion.Field.custom_event_type: 'PURCHASE',
        })

        custom_conversion.remote_create()


class BatchTestCase(FacebookAdsTestCase):

    def setUp(self):
        self.created_ids = []
        self.num_campaigns = 5
        super(BatchTestCase, self).setUp()

    def create_campaigns(self):
        ret_val = []
        for i in range(self.num_campaigns):
            campaign = self.new_test_campaign()
            ret_val.append(campaign)
            self.delete_in_teardown(campaign)
        return ret_val

    def check_ids(self, campaigns):
        # Check if the campaigns were created by counting distinct ids
        ids = set(
            filter(
                None,
                [campaign[objects.Campaign.Field.id]
                    for campaign in campaigns],
            ),
        )
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
    test_business_id = config['business']
    page_id = config['page_id']
    app_id = config['app_id']
    app_secret = config['app_secret']
    test_sec_business_id = config['sec_business']
    test_sec_account_id = config['sec_act_id']

    if 'access_token' in config:
        access_token = config['access_token']
    else:
        if len(sys.argv) < 2:
            raise TypeError("Please provide the access token as an argument")

        access_token = sys.argv.pop()

    FacebookAdsTestCase.TEST_SESSION = session.FacebookSession(
        app_id,
        app_secret,
        access_token,
    )
    FacebookAdsTestCase.TEST_API = api.FacebookAdsApi(
        FacebookAdsTestCase.TEST_SESSION,
    )
    api.FacebookAdsApi.set_default_api(FacebookAdsTestCase.TEST_API)

    if 'act_' not in test_account_id:
        test_account_id = 'act_' + test_account_id
    FacebookAdsTestCase.TEST_ACCOUNT = objects.AdAccount(test_account_id)
    FacebookAdsTestCase.PAGE_ID = page_id
    FacebookAdsTestCase.TEST_BUSINESS = test_business_id
    FacebookAdsTestCase.TEST_SECONDARY_ACCOUNT = test_sec_account_id
    FacebookAdsTestCase.TEST_SECONDARY_BUSINESS = test_sec_business_id

    unittest.main()
