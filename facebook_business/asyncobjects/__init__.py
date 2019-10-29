import facebook_business.objects as baseobjects
from facebook_business.adobjects import ad
from facebook_business.adobjects import adaccount
from facebook_business.adobjects import adset
from facebook_business.adobjects import business
from facebook_business.adobjects import campaign
from facebook_business.adobjects import adspixel
from facebook_business.asyncobjects.abstractcrudaioobject import AbstractCrudAioObject
from facebook_business.asyncobjects.edgelessiterator import EdgeLessIterator


class AdUser(AbstractCrudAioObject, baseobjects.AdUser):
    pass


class Page(AbstractCrudAioObject, baseobjects.Page):
    pass


class AdAccount(AbstractCrudAioObject, adaccount.AdAccount):
    def add_user(self, user, business, role):
        params = {
            'user': user,
            'business': business,
            'role': role,
        }
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'userpermissions'),
            params=params,
        )

    def get_activities_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Activity's associated with this account."""
        return self.iterate_edge_aio(baseobjects.Activity, fields, params, limit=limit)

    def get_ad_users_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdUser's associated with this account."""
        return self.iterate_edge_aio(AdUser, fields, params, limit=limit)

    def get_campaigns_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Campaign's associated with this account."""
        return self.iterate_edge_aio(Campaign, fields, params, limit=limit)

    def get_ad_sets_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdSet's associated with this account."""
        return self.iterate_edge_aio(AdSet, fields, params, limit=limit)

    def get_ads_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Ad's associated with this account."""
        return self.iterate_edge_aio(Ad, fields, params, limit=limit)

    def get_ad_conversion_pixels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over AdConversionPixels associated with this account.
        """
        return self.iterate_edge_aio(adspixel.AdsPixel, fields, params, limit=limit)

    def get_ad_creatives_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdCreative's associated with this account."""
        return self.iterate_edge_aio(AdCreative, fields, params, limit=limit)

    def get_ad_images_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdImage's associated with this account."""
        return self.iterate_edge_aio(AdImage, fields, params, limit=limit)

    def get_broad_category_targeting_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over BroadCategoryTargeting's associated with this
        account.
        """
        return self.iterate_edge_aio(baseobjects.BroadCategoryTargeting, fields, params, limit=limit)

    def get_custom_audiences_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over CustomAudience's associated with this account.
        """
        return self.iterate_edge_aio(CustomAudience, fields, params, limit=limit)

    def get_reach_estimate_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over ReachEstimate's associated with this account.
        """
        return self.iterate_edge_aio(baseobjects.ReachEstimate, fields, params, limit=limit)

    def get_ad_preview_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over previews generated under this account."""
        return self.iterate_edge_aio(baseobjects.GeneratePreview, fields, params, limit=limit)

    def get_ad_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns all the ad labels associated with the ad account
        """
        return self.iterate_edge_aio(baseobjects.AdLabel, fields, params, limit=limit)

    def get_ad_creatives_by_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad creatives associated with the ad AdLabel
        """
        return self.iterate_edge_aio(baseobjects.AdCreativesByLabels, fields, params, limit=limit)

    def get_ads_by_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad Groups associated with the ad AdLabel
        """
        return self.iterate_edge_aio(baseobjects.AdsByLabels, fields, params, limit=limit)

    def get_adsets_by_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad sets associated with the ad AdLabel
        """
        return self.iterate_edge_aio(baseobjects.AdSetsByLabels, fields, params, limit=limit)

    def get_campaigns_by_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad campaigns associated with the ad AdLabel
        """
        return self.iterate_edge_aio(baseobjects.CampaignsByLabels, fields, params, limit=limit)

    def get_minimum_budgets_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the minimum budget associated with the AdAccount
        """
        return self.iterate_edge_aio(baseobjects.MinimumBudget, fields, params,
                                     limit=limit)

    def get_ad_place_page_sets_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad place page sets associated with the AdAccount
        """
        return self.iterate_edge_aio(baseobjects.AdPlacePageSet, fields, params, limit=limit)

    def get_custom_conversions_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the custom conversions associated with the AdAccount
        """
        return self.iterate_edge_aio(baseobjects.CustomConversion, fields, params, limit=limit)

    def get_insights_aio(self, fields=None, params=None, limit=1000, is_async=False,
                         has_action=None, needs_action_device=None,
                         has_filters=False, for_date=None, needs_carousel_name=False):
        """
        If 'is_async' is False, returns EdgeIterator.

        If 'is_async' is True, creates a job and job iterator for it and
        returns the job iterator (AsyncAioJobIterator class, subclass of EdgeIterator).

        Regardless the async parameter, it puts the iterator to the queue so that
        the results of execution are later available  through
        FacebookAdsAsyncApi.get_default_api().get_all_async_results() call.
        """
        if is_async:
            return self.iterate_edge_async_aio(
                Insights, fields, params, has_action,
                needs_action_device, limit=limit,
                has_filters=has_filters, for_date=for_date,
                needs_carousel_name=needs_carousel_name
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )


class Campaign(AbstractCrudAioObject, campaign.Campaign):
    def get_ad_sets_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdSet's associated with this campaign."""
        return self.iterate_edge_aio(AdSet, fields, params, limit=limit)

    def get_ads_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Ad's associated with this campaign."""
        return self.iterate_edge_aio(Ad, fields, params, limit=limit)

    def get_insights_aio(self, fields=None, params=None, limit=1000, is_async=False,
                         has_action=None, needs_action_device=None,
                         has_filters=False, for_date=None, needs_carousel_name=False):
        """
        If 'is_async' is False, returns EdgeIterator.

        If 'is_async' is True, creates a job and job iterator for it and
        returns the job iterator (AsyncAioJobIterator class, subclass of EdgeIterator).

        Regardless the async parameter, it puts the iterator to the queue so that
        the results of execution are later available  through
        FacebookAdsAsyncApi.get_default_api().get_all_async_results() call.
        """
        if is_async:
            return self.iterate_edge_async_aio(
                Insights, fields, params, has_action,
                needs_action_device, limit=limit,
                has_filters=has_filters, for_date=for_date,
                needs_carousel_name=needs_carousel_name
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )


class AdSet(AbstractCrudAioObject, adset.AdSet):
    def get_ads_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Ad's associated with this set."""
        return self.iterate_edge_aio(Ad, fields, params, limit=limit)

    def get_ad_creatives_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdCreative's associated with this set."""
        return self.iterate_edge_aio(AdCreative, fields, params, limit=limit)

    def get_insights_aio(self, fields=None, params=None, limit=1000, is_async=False,
                         has_action=None, needs_action_device=None,
                         has_filters=False, for_date=None, needs_carousel_name=False):
        """
        If 'is_async' is False, returns EdgeIterator.

        If 'is_async' is True, creates a job and job iterator for it and
        returns the job iterator (AsyncAioJobIterator class, subclass of EdgeIterator).

        Regardless the async parameter, it puts the iterator to the queue so that
        the results of execution are later available  through
        FacebookAdsAsyncApi.get_default_api().get_all_async_results() call.
        """
        if is_async:
            return self.iterate_edge_async_aio(
                Insights, fields, params, has_action,
                needs_action_device, limit=limit,
                has_filters=has_filters, for_date=for_date,
                needs_carousel_name=needs_carousel_name
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )


class TargetingSearch(AbstractCrudAioObject, baseobjects.AbstractCrudObject, baseobjects.TargetingSearch):

    # TODO: replace this hack with a paged iterator abstract base
    class Field(object):
        id = 'id'

    class DemographicSearchClasses(object):
        demographics = 'demographics'
        ethnic_affinity = 'ethnic_affinity'
        family_statuses = 'family_statuses'
        generation = 'generation'
        home_ownership = 'home_ownership'
        home_type = 'home_type'
        home_value = 'home_value'
        household_composition = 'household_composition'
        income = 'income'
        industries = 'industries'
        life_events = 'life_events'
        markets = 'markets'
        moms = 'moms'
        net_worth = 'net_worth'
        office_type = 'office_type'
        politics = 'politics'

    class TargetingSearchTypes(object):
        country = 'adcountry'
        education = 'adeducationschool'
        employer = 'adworkemployer'
        geolocation = 'adgeolocation'
        geometadata = 'adgeolocationmeta'
        interest = 'adinterest'
        interest_suggestion = 'adinterestsuggestion'
        interest_validate = 'adinterestvalid'
        keyword = 'adkeyword'
        locale = 'adlocale'
        major = 'adeducationmajor'
        position = 'adworkposition'
        radius_suggestion = 'adradiussuggestion'
        targeting_category = 'adtargetingcategory'
        zipcode = 'adzipcode'

    @classmethod
    def get_endpoint(cls):
        return 'search'

    @classmethod
    def get_all_countries(cls):
        ts = cls('no')
        country_iter = EdgeLessIterator(
                ts, params={'type': ts.TargetingSearchTypes.country, 'q': ''})
        country_iter.submit_next_page_aio()
        return [x for x in country_iter]

    @classmethod
    def get_all_regions(cls):
        ts = cls('no')
        reg_iter = EdgeLessIterator(
                ts, params={'type': ts.TargetingSearchTypes.geolocation,
                            'location_types': ['region'], 'q': ''})
        reg_iter.submit_next_page_aio()
        return [x for x in reg_iter]


class Ad(AbstractCrudAioObject, ad.Ad):
    def get_ad_creatives_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdCreatives associated with this ad."""
        return self.iterate_edge_aio(AdCreative, fields, params, limit=limit)

    def get_targeting_description_aio(self, fields=None, params=None, limit=1000):
        """Returns TargetingDescription object associated with this ad."""
        return self.edge_object(baseobjects.TargetingDescription, fields, params)

    def get_keyword_stats_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over KeywordStats associated with this ad."""
        return self.edge_object(baseobjects.KeywordStats, fields, params)

    def get_ad_preview_aio(self, fields=None, params=None, limit=1000):
        """Returns AdPreview object associated with this ad."""
        return self.edge_object(baseobjects.AdPreview, fields, params)

    def get_reach_estimate_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over ReachEstimates associated with this ad."""
        return self.iterate_edge_aio(baseobjects.ReachEstimate, fields, params, limit=limit)

    def get_click_tracking_tag_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over ClickTrackingTags associated with this ad."""
        return self.iterate_edge_aio(ClickTrackingTag, fields, params, limit=limit)

    def get_leads_aio(self, fields=None, params=None, limit=1000):
        """
        Returns all the leads associated with the Ad
        """
        return self.iterate_edge_aio(Lead, fields, params, limit=limit)

    def get_insights_aio(self, fields=None, params=None, limit=1000, is_async=False,
                         has_action=None, needs_action_device=None,
                         has_filters=False, for_date=None, needs_carousel_name=False):
        """
        If 'is_async' is False, returns EdgeIterator.

        If 'is_async' is True, creates a job and job iterator for it and
        returns the job iterator (AsyncAioJobIterator class, subclass of EdgeIterator).

        Regardless the async parameter, it puts the iterator to the queue so that
        the results of execution are later available  through
        FacebookAdsAsyncApi.get_default_api().get_all_async_results() call.
        """
        if is_async:
            return self.iterate_edge_async_aio(
                Insights, fields, params, has_action,
                needs_action_device, limit=limit,
                has_filters=has_filters, for_date=for_date,
                needs_carousel_name=needs_carousel_name
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )


class AdConversionPixel(AbstractCrudAioObject, adspixel.AdsPixel):
    pass


class AdsPixel(AbstractCrudAioObject, baseobjects.AdsPixel):
    pass


class AdCreative(AbstractCrudAioObject, baseobjects.AdCreative):
    pass


class AdImage(AbstractCrudAioObject, baseobjects.AdImage):
    pass


class AdVideo(AbstractCrudAioObject, baseobjects.AdVideo):
    pass


class ClickTrackingTag(AbstractCrudAioObject, baseobjects.ClickTrackingTag):
    pass


class CustomAudience(AbstractCrudAioObject, baseobjects.CustomAudience):
    pass


class LookalikeAudience(AbstractCrudAioObject, baseobjects.LookalikeAudience):
    pass


class ReachFrequencyPrediction(AbstractCrudAioObject, baseobjects.ReachFrequencyPrediction):
    pass


class Business(AbstractCrudAioObject, business.Business):
    def get_ad_accounts_aio(self, fields=None, params=None, limit=50):
        return self.iterate_edge_aio(AdAccount, fields, params, limit=limit)

    def get_product_catalogs_aio(self, fields=None, params=None):
        return self.iterate_edge_aio(ProductCatalog, fields, params)

    def get_insights_aio(self, fields=None, params=None, limit=500, is_async=False):
        if is_async:
            return self.iterate_edge_async_aio(
                Insights,
                fields,
                params, limit=limit
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )

    def get_order_id_attributions_aio(self, fields=None, params=None, limit=100, is_async=False):
        if is_async:
            return self.iterate_edge_async_aio(
                OrderIdAttributions,
                fields,
                params, limit=limit
            )
        return self.iterate_edge_aio(
            OrderIdAttributions,
            fields,
            params,
            include_summary=False, limit=limit
        )

    def get_business_projects_aio(self, fields=None, params=None, limit=50):
        return self.iterate_edge_aio(BusinessProject, fields, params, limit=limit)


class BusinessProject(AbstractCrudAioObject, baseobjects.AbstractCrudObject):

    class Field(object):
        id = 'id'
        name = 'name'

    @classmethod
    def get_endpoint(cls):
        return 'businessprojects'


class ProductCatalog(AbstractCrudAioObject, baseobjects.ProductCatalog):
    pass


class ProductFeed(AbstractCrudAioObject, baseobjects.ProductFeed):
    pass


class ProductFeedUpload(AbstractCrudAioObject, baseobjects.ProductFeedUpload):
    pass


class ProductFeedUploadError(AbstractCrudAioObject, baseobjects.ProductFeedUploadError):
    pass


class ProductSet(AbstractCrudAioObject, baseobjects.ProductSet):
    pass


class ProductGroup(AbstractCrudAioObject, baseobjects.ProductGroup):
    pass


class Product(AbstractCrudAioObject, baseobjects.Product):
    pass


class ProductAudience(AbstractCrudAioObject, baseobjects.ProductAudience):
    pass


class AdLabel(AbstractCrudAioObject, baseobjects.AdLabel):
    pass


class Lead(AbstractCrudAioObject, baseobjects.Lead):
    pass


class LeadgenForm(AbstractCrudAioObject, baseobjects.LeadgenForm):
    pass


class AdPlacePageSet(AbstractCrudAioObject, baseobjects.AdPlacePageSet):
    pass


class CustomConversion(AbstractCrudAioObject, baseobjects.CustomConversion):
    pass


class Insights(AbstractCrudAioObject, baseobjects.Insights):
    # TODO: implement async get method
    pass


class OrderIdAttributions(AbstractCrudAioObject, baseobjects.OrderIdAttributions):
    pass
