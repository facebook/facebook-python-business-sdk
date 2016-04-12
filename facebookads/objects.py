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

"""
DEPRECATED

This file is kept for backward compatibility.
Please use objects in adobjects folder instead.
"""

from facebookads.adobjects import (
    adaccount,
    adlabel,
    abstractobject,
    abstractcrudobject,
    adimage,
    campaign,
    adset,
    adcreative,
    ad,
    productcatalog,
    adsinsights,
    productitem,
    productgroup,
    productfeeduploaderror,
    productfeedupload,
    productfeed,
    business,
    transaction,
    reachfrequencyprediction,
    reachestimate,
    ratecard,
    partnercategory,
    productset,
    adspixel,
    customaudience,
    offsitepixel,
    adactivity,
    adplacepageset,
    minimumbudget,
    connectionobject,
    externaleventsource,
    customconversion,
    lead,
    videothumbnail,
    targetingsentenceline,
    adaccountgroup,
    leadgenform,
    adkeywordstats,
    broadtargetingcategories,
    lookalikespec,
    targeting,
    adspixelstatsresult,
    adaccountuser,
    advideo,
    page,
    targetingsearch,
    clicktrackingtag,
    adreportrun,
)

import facebookads
import warnings
import functools


def deprecated(fun=None, replacement=None):
    if fun is None:
        return functools.partial(deprecated, replacement=replacement)

    @functools.wraps(fun)
    def inner(*args, **kwargs):
        msg = "%s is deprecated" % fun.__name__
        if replacement:
            msg += "; use %s instead" % replacement
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
        doc = msg + '\n'
        if fun.__doc__:
            doc += fun.__doc__
        fun.__doc__ = doc
        return fun(*args, **kwargs)
    return inner


class EdgeIterator(facebookads.api.Cursor):
    pass


class AbstractObject(abstractobject.AbstractObject):
    pass


class AbstractCrudObject(abstractcrudobject.AbstractCrudObject):
    pass


class AdUser(adaccountuser.AdAccountUser):
    pass


class Page(page.Page):
    pass


class Activity(adactivity.AdActivity):
    pass


class AdAccount(adaccount.AdAccount):

    @deprecated(replacement='get_generate_previews')
    def get_ad_preview(self, fields=None, params=None):
        """Returns iterator over previews generated under this account."""
        return self.get_generate_previews(fields, params)

    @deprecated(replacement='get_targeting_sentence_lines')
    def get_targeting_description(self, fields=None, params=None):
        """
        Returns TargetingDescription object associated with this account.
        """
        return self.get_targeting_sentence_lines(fields, params).get_one()

    @deprecated(replacement='get_broad_targeting_categories')
    def get_broad_category_targeting(self, fields=None, params=None):
        """
        Returns iterator over BroadCategoryTargeting's associated with this
        account.
        """
        return self.get_broad_targeting_categories(fields, params)

    @deprecated(replacement='get_rate_card')
    def get_rate_cards(self, fields=None, params=None):
        """Returns iterator over RateCard's associated with this account."""
        return self.get_rate_card(fields, params)

    @deprecated(replacement='get_ad_sets_by_labels')
    def get_adsets_by_labels(self, fields=None, params=None):
        """
        Returns the ad sets associated with the ad AdLabel
        """
        return self.get_ad_sets_by_labels(fields, params)

    @deprecated(replacement='get_users')
    def get_ad_users(self, fields=None, params=None):
        """Returns iterator over AdUser's associated with this account."""
        return self.get_users(fields, params)


class AdAccountGroup(adaccountgroup.AdAccountGroup):

    def get_users(self, fields=None, params=None):
        """
        Returns iterator over AdAccountGroupUser's associated with this account
        group.
        """
        return self.iterate_edge(AdAccountGroupUser, fields, params)


class AdAccountGroupAccount(AbstractObject):

    class Field(object):
        account_id = 'account_id'
        status = 'status'

    @classmethod
    def get_endpoint(cls):
        return 'adaccounts'

    def get_node_path(self):
        return (
            self.get_parent_id_assured(),
            self.get_endpoint(),
            self.get_id_assured()
        )

    def get_ad_account(self):
        """Returns an AdAccount object with the same account id."""
        return AdAccount(fbid='act_' + self[self.Field.account_id])


class AdAccountGroupUser(AbstractCrudObject):

    class Field(object):
        id = 'uid'
        role = 'role'
        uid = 'uid'

    class Role(object):
        administrator = 1001
        general_user = 1002
        reports_only = 1003

    @classmethod
    def get_endpoint(cls):
        return 'users'

    def get_node_path(self):
        return (
            self.get_parent_id_assured(),
            self.get_endpoint(),
            self.get_id_assured()
        )

    def get_ad_user(self):
        """Returns an AdUser object with the same account id."""
        return AdUser(fbid=self[self.Field.uid])


class Campaign(campaign.Campaign):
    class BuyingType(object):
        auction = 'AUCTION'
        fixed_price = 'FIXED_PRICE'
        reserved = 'RESERVED'

class AdSet(adset.AdSet):
    class PacingType(object):
        day_parting = 'day_parting'
        standard = 'standard'
        no_pacing = 'no_pacing'

class Ad(ad.Ad):
    @deprecated(replacement='get_previews')
    def get_ad_preview(self, fields=None, params=None):
        """Returns AdPreview object associated with this ad."""
        return self.get_previews(fields, params).get_one()

    @deprecated(replacement='get_targeting_sentence_lines')
    def get_targeting_description(self, fields=None, params=None):
        """Returns TargetingDescription object associated with this ad."""
        return self.get_targeting_sentence_lines(fields, params).get_one()

class AdConversionPixel(offsitepixel.OffsitePixel):
    pass


class AdsPixel(adspixel.AdsPixel):

    @deprecated(replacement='unshare_pixel_from_ad_account')
    def unshare_pixel(self, business_id, account_id):
        return self.unshare_pixel_from_ad_account(business_id, account_id)

    @deprecated(replacement='unshare_pixel_from_agency')
    def unshare_pixel_agencies(self, business_id, agency_id):
        return self.unshare_pixel_from_agency(business_id, agency_id)

    @deprecated(replacement='share_pixel_with_ad_account')
    def share_pixel(self, business_id, account_id):
        return self.share_pixel_with_ad_account(business_id, account_id)

    @deprecated(replacement='share_pixel_with_agency')
    def share_pixel_agencies(self, business_id, agency_id):
        return self.share_pixel_with_agency(business_id, agency_id)

    @deprecated(replacement='get_ad_accounts')
    def list_ad_accounts(self, business_id):
        return self.get_ad_accounts(business_id)

    @deprecated(replacement='get_agencies')
    def list_shared_agencies(self):
        return self.get_agencies()


class AdCreative(adcreative.AdCreative):
    @deprecated(replacement='get_previews')
    def get_ad_preview(self, fields=None, params=None):
        self.get_previews(fields=fields, params=params)


class AdImage(adimage.AdImage):
    pass

class AdVideo(advideo.AdVideo):
    pass


class VideoThumbnail(videothumbnail.VideoThumbnail):
    pass


class GeneratePreview(AbstractObject):

    class Field(object):
        ad_format = 'ad_format'
        body = 'body'
        creative = 'creative'
        post = 'post'
        product_item_ids = 'product_item_ids'

    class AdFormat(object):
        desktop_feed_standard = 'DESKTOP_FEED_STANDARD'
        mobile_banner = 'MOBILE_BANNER'
        mobile_feed_standard = 'MOBILE_FEED_STANDARD'
        mobile_interstitial = 'MOBILE_INTERSTITIAL'
        right_column_standard = 'RIGHT_COLUMN_STANDARD'

    @classmethod
    def get_endpoint(cls):
        return 'generatepreviews'

    def get_html(self):
        """Returns the preview html."""
        return self[self.Field.body]


class AdCreativePreview(GeneratePreview):

    @classmethod
    def get_endpoint(cls):
        return 'previews'


class AdPreview(AdCreativePreview):

    @classmethod
    def get_endpoint(cls):
        return 'previews'


class AdsPixelStat(adspixelstatsresult.AdsPixelStatsResult):
    pass


class KeywordStats(adkeywordstats.AdKeywordStats):
    pass


class BroadCategoryTargeting(broadtargetingcategories.BroadTargetingCategories):
    pass


class ClickTrackingTag(clicktrackingtag.ClickTrackingTag):
    pass

class CustomAudience(customaudience.CustomAudience):
    pass


class ConnectionObject(connectionobject.ConnectionObject):

    class Type(object):
        application = 2
        domain = 7
        event = 3
        page = 1
        place = 6


class LookalikeAudience(customaudience.CustomAudience):

    class Field(customaudience.CustomAudience.Field):
        class LookalikeSpec(lookalikespec.LookalikeSpec.Field):
            pass

    class LookalikeType(object):
        reach = 'reach'
        similarity = 'similarity'

    class ConversionType(object):
        page_likes = 'page_likes'

    @classmethod
    def get_endpoint(cls):
        return 'customaudiences'


class PartnerCategory(partnercategory.PartnerCategory):
    pass


class RateCard(ratecard.RateCard):
    pass


class ReachEstimate(reachestimate.ReachEstimate):
    pass


class ReachFrequencyPrediction(reachfrequencyprediction.ReachFrequencyPrediction):
    pass


class TargetingDescription(targetingsentenceline.TargetingSentenceLine):
    pass


class TargetingSearch(targetingsearch.TargetingSearch):
    pass

class TargetingSpecsField(targeting.Targeting.Field):
    pass


class Transaction(transaction.Transaction):
    pass


class Business(business.Business):

    class Field(object):
        created_by = 'created_by'
        creation_time = 'creation_time'
        id = 'id'
        name = 'name'
        primary_page = 'primary_page'
        timezone_id = 'timezone_id'
        update_time = 'update_time'
        updated_by = 'updated_by'
        vertical_id = 'vertical_id'


class ProductCatalog(productcatalog.ProductCatalog):
    pass


class ProductCatalogExternalEventSource(externaleventsource.ExternalEventSource):
    pass


class ProductFeed(productfeed.ProductFeed):

    class Format(object):
        tsv = 'TSV'
        xml = 'XML'

class ProductFeedUpload(productfeedupload.ProductFeedUpload):
    pass


class ProductFeedUploadError(productfeeduploaderror.ProductFeedUploadError):
    pass


class ProductSet(productset.ProductSet):
    pass


class ProductGroup(productgroup.ProductGroup):
    pass


class Product(productitem.ProductItem):
    class Field(productitem.ProductItem.Field):
        title = 'title'


class ProductAudience(customaudience.CustomAudience):

    class Field(customaudience.CustomAudience.Field):
        product_set_id = 'product_set_id'
        inclusions = 'inclusions'
        exclusions = 'exclusions'

    @classmethod
    def get_endpoint(cls):
        return 'product_audiences'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_product_audience(fields, params, batch, pending)


class Insights(adsinsights.AdsInsights):

    class Preset(adsinsights.AdsInsights.DatePreset):
        pass

    class Breakdown(adsinsights.AdsInsights.Breakdowns):
        pass

    class ActionBreakdown(adsinsights.AdsInsights.SummaryActionBreakdowns):
        pass

    class ActionAttributionWindow(adsinsights.AdsInsights.ActionAttributionWindows):
        pass


class AdLabel(adlabel.AdLabel):
    pass

class AdsByLabels(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'adsbylabels'


class AdCreativesByLabels(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'adcreativesbylabels'


class AdSetsByLabels(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'adsetsbylabels'


class CampaignsByLabels(AbstractObject):

    @classmethod
    def get_endpoint(cls):
        return 'campaignsbylabels'


class Lead(lead.Lead):
    pass


class LeadgenForm(leadgenform.LeadgenForm):
    pass


class MinimumBudget(minimumbudget.MinimumBudget):
    pass


class AsyncJob(adreportrun.AdReportRun):

    def __init__(self, target_objects_class):
        adreportrun.AdReportRun.__init__(self)
        self.target_objects_class = target_objects_class


class AdPlacePageSet(adplacepageset.AdPlacePageSet):
    pass


class CustomConversion(customconversion.CustomConversion):
    pass
