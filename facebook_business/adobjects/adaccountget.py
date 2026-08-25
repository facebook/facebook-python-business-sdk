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

class AdAccountGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountGet = True
        super(AdAccountGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_controls = 'account_controls'
        account_currency_ratio_to_usd = 'account_currency_ratio_to_usd'
        account_id = 'account_id'
        account_status = 'account_status'
        active_billing_date_preference = 'active_billing_date_preference'
        activities = 'activities'
        ad_account_promotable_objects = 'ad_account_promotable_objects'
        ad_column_sizes = 'ad_column_sizes'
        ad_limits_insights = 'ad_limits_insights'
        adcreatives = 'adcreatives'
        addrafts = 'addrafts'
        adimages = 'adimages'
        adlabels = 'adlabels'
        adrules_count_by_type = 'adrules_count_by_type'
        adrules_history = 'adrules_history'
        adrules_library = 'adrules_library'
        ads = 'ads'
        ads_paused = 'ads_paused'
        ads_volume = 'ads_volume'
        adsets = 'adsets'
        adspaymentcycle = 'adspaymentcycle'
        adspixels = 'adspixels'
        adtrust_dsl = 'adtrust_dsl'
        advertisable_applications = 'advertisable_applications'
        advideos = 'advideos'
        age = 'age'
        agencies = 'agencies'
        agency_client_declaration = 'agency_client_declaration'
        agency_fee_config = 'agency_fee_config'
        ai_generated_features_test_framework_enrolled = 'ai_generated_features_test_framework_enrolled'
        all_capabilities = 'all_capabilities'
        all_payment_methods = 'all_payment_methods'
        am_oneshop_settings = 'am_oneshop_settings'
        amount_spent = 'amount_spent'
        amount_spent_history = 'amount_spent_history'
        applications = 'applications'
        applied_publisher_block_lists = 'applied_publisher_block_lists'
        archived_adgroup_count = 'archived_adgroup_count'
        archived_campaign_count = 'archived_campaign_count'
        archived_campaign_group_count = 'archived_campaign_group_count'
        asset_feed_spec_from_existing_post = 'asset_feed_spec_from_existing_post'
        asset_feed_spec_from_instagram_media = 'asset_feed_spec_from_instagram_media'
        asset_score = 'asset_score'
        assigned_partners = 'assigned_partners'
        attr_window_deprecation_group = 'attr_window_deprecation_group'
        auth_flow_for_trust_tier_state = 'auth_flow_for_trust_tier_state'
        authorized_country_for_political_ads = 'authorized_country_for_political_ads'
        automatic_creative_optimization_test_framework_enrolled = 'automatic_creative_optimization_test_framework_enrolled'
        average_daily_campaign_budget = 'average_daily_campaign_budget'
        average_daily_campaign_group_budget = 'average_daily_campaign_group_budget'
        average_lifetime_campaign_budget = 'average_lifetime_campaign_budget'
        average_lifetime_campaign_group_budget = 'average_lifetime_campaign_group_budget'
        balance = 'balance'
        brand_safety_content_filter_levels = 'brand_safety_content_filter_levels'
        brand_safety_excluded_topics = 'brand_safety_excluded_topics'
        business = 'business'
        business_ad_account_requests = 'business_ad_account_requests'
        business_city = 'business_city'
        business_country_code = 'business_country_code'
        business_name = 'business_name'
        business_restriction_reason = 'business_restriction_reason'
        business_state = 'business_state'
        business_street = 'business_street'
        business_street2 = 'business_street2'
        business_verification_status = 'business_verification_status'
        business_zip = 'business_zip'
        businessprojects = 'businessprojects'
        call_ads_ad_account_similar_advertiser_budget_recommendation = 'call_ads_ad_account_similar_advertiser_budget_recommendation'
        call_ads_similar_advertiser_budget_recommendation = 'call_ads_similar_advertiser_budget_recommendation'
        campaign_group_with_cbo = 'campaign_group_with_cbo'
        campaigns = 'campaigns'
        can_bypass_fs_check = 'can_bypass_fs_check'
        can_create_brand_lift_study = 'can_create_brand_lift_study'
        can_pay_now = 'can_pay_now'
        can_remove_payment_methods = 'can_remove_payment_methods'
        can_repay_now = 'can_repay_now'
        can_see_collaborative_ads_reporting = 'can_see_collaborative_ads_reporting'
        capabilities = 'capabilities'
        connected_instagram_accounts = 'connected_instagram_accounts'
        cpas_campaign_default_budget = 'cpas_campaign_default_budget'
        cpas_campaign_group_default_budget = 'cpas_campaign_group_default_budget'
        created_time = 'created_time'
        creation_packages = 'creation_packages'
        ctwa_smb_enforcing_days_left = 'ctwa_smb_enforcing_days_left'
        ctx_advertiser_sabr_lifetime_duration_recommendation = 'ctx_advertiser_sabr_lifetime_duration_recommendation'
        ctx_dfo_objective_defaults = 'ctx_dfo_objective_defaults'
        ctx_flexible_format_targeting = 'ctx_flexible_format_targeting'
        currency = 'currency'
        current_addrafts = 'current_addrafts'
        current_unbilled_spend = 'current_unbilled_spend'
        current_unpaid_unrepaid_invoice = 'current_unpaid_unrepaid_invoice'
        custom_audience_info = 'custom_audience_info'
        customaudiences = 'customaudiences'
        customconversions = 'customconversions'
        customer_po_number = 'customer_po_number'
        daily_spend_limit = 'daily_spend_limit'
        dcaf = 'dcaf'
        default_dsa_beneficiary = 'default_dsa_beneficiary'
        default_dsa_payor = 'default_dsa_payor'
        default_unified_attribution_spec = 'default_unified_attribution_spec'
        default_values = 'default_values'
        disable_reason = 'disable_reason'
        domain_and_site_links = 'domain_and_site_links'
        dsa_recommendations = 'dsa_recommendations'
        dynamic_probation_dsl = 'dynamic_probation_dsl'
        end_advertiser = 'end_advertiser'
        end_advertiser_name = 'end_advertiser_name'
        existing_customers = 'existing_customers'
        expired_funding_source_details = 'expired_funding_source_details'
        extended_credit = 'extended_credit'
        extended_credit_info = 'extended_credit_info'
        extended_credit_invoice_group = 'extended_credit_invoice_group'
        failed_delivery_checks = 'failed_delivery_checks'
        fb_entity = 'fb_entity'
        flex_single_objective = 'flex_single_objective'
        funding_source = 'funding_source'
        funding_source_details = 'funding_source_details'
        generatepreviews = 'generatepreviews'
        has_active_skan_campaign_groups = 'has_active_skan_campaign_groups'
        has_combo_cards_on_file = 'has_combo_cards_on_file'
        has_extended_credit = 'has_extended_credit'
        has_migrated_permissions = 'has_migrated_permissions'
        has_page_authorized_adaccount = 'has_page_authorized_adaccount'
        has_personal_access = 'has_personal_access'
        has_purchase_optimization_eligible_page = 'has_purchase_optimization_eligible_page'
        has_repay_processing_invoices = 'has_repay_processing_invoices'
        has_started_purchase_optimized_ctm_ad_within_1d = 'has_started_purchase_optimized_ctm_ad_within_1d'
        has_value_rule_set = 'has_value_rule_set'
        id = 'id'
        if_viewer_has_permission_to_advertise = 'if_viewer_has_permission_to_advertise'
        incremental_conversion_optimization_ad_studies = 'incremental_conversion_optimization_ad_studies'
        instagram_accounts = 'instagram_accounts'
        invoicing_emails = 'invoicing_emails'
        ios_fourteen_campaign_limits = 'ios_fourteen_campaign_limits'
        is_attribution_spec_system_default = 'is_attribution_spec_system_default'
        is_ba_skip_delayed_eligible = 'is_ba_skip_delayed_eligible'
        is_biz_migration_eligible = 'is_biz_migration_eligible'
        is_br_entity_account = 'is_br_entity_account'
        is_business_allowed_to_advertise = 'is_business_allowed_to_advertise'
        is_business_verification_eligible = 'is_business_verification_eligible'
        is_closed_by_advertiser_compromise_bot = 'is_closed_by_advertiser_compromise_bot'
        is_collaborative_ads_ad_account = 'is_collaborative_ads_ad_account'
        is_ctx_advertiser = 'is_ctx_advertiser'
        is_direct_deals_enabled = 'is_direct_deals_enabled'
        is_disabled_umbrella = 'is_disabled_umbrella'
        is_eligible_for_advantage_plus_creative_regulated_category = 'is_eligible_for_advantage_plus_creative_regulated_category'
        is_expanded_shopless_awpt_eligible = 'is_expanded_shopless_awpt_eligible'
        is_in_3ds_authorization_enabled_market = 'is_in_3ds_authorization_enabled_market'
        is_mi_billing_info_updated = 'is_mi_billing_info_updated'
        is_mm_lite_api_enabled = 'is_mm_lite_api_enabled'
        is_new_advertiser = 'is_new_advertiser'
        is_notifications_enabled = 'is_notifications_enabled'
        is_oba_opt_out = 'is_oba_opt_out'
        is_omnichannel_campaign_eligible = 'is_omnichannel_campaign_eligible'
        is_pageless_ctwa_eligible = 'is_pageless_ctwa_eligible'
        is_pending_numbers_exposure_flag_enabled = 'is_pending_numbers_exposure_flag_enabled'
        is_personal = 'is_personal'
        is_pinless_debit_eligible = 'is_pinless_debit_eligible'
        is_placement_soft_opt_out_enabled = 'is_placement_soft_opt_out_enabled'
        is_prepay_account = 'is_prepay_account'
        is_retail_media_network = 'is_retail_media_network'
        is_shopless_awpt_eligible = 'is_shopless_awpt_eligible'
        is_tax_id_required = 'is_tax_id_required'
        is_tier_0 = 'is_tier_0'
        is_tier_0_full = 'is_tier_0_full'
        is_tier_1 = 'is_tier_1'
        is_tier_restricted = 'is_tier_restricted'
        is_update_timezone_currency_too_recently = 'is_update_timezone_currency_too_recently'
        is_user_allowed_to_advertise = 'is_user_allowed_to_advertise'
        is_using_higher_daily_flex_rate = 'is_using_higher_daily_flex_rate'
        is_value_rules_smart_default_on = 'is_value_rules_smart_default_on'
        is_wa_cloud_api_user = 'is_wa_cloud_api_user'
        is_youth_ads_pao_basic_advertiser = 'is_youth_ads_pao_basic_advertiser'
        is_youth_ads_pao_basic_advertiser_announcement_eligible = 'is_youth_ads_pao_basic_advertiser_announcement_eligible'
        last_spend_time = 'last_spend_time'
        last_used_time = 'last_used_time'
        liable_address = 'liable_address'
        liable_addresses = 'liable_addresses'
        live_video_advertiser_details = 'live_video_advertiser_details'
        marketing_message_enablement_status = 'marketing_message_enablement_status'
        marketing_messages_settings = 'marketing_messages_settings'
        max_bid = 'max_bid'
        max_billing_threshold = 'max_billing_threshold'
        maybe_pac_internal_post_from_primary_post = 'maybe_pac_internal_post_from_primary_post'
        media_agency = 'media_agency'
        min_billing_threshold = 'min_billing_threshold'
        min_campaign_group_spend_cap = 'min_campaign_group_spend_cap'
        min_daily_budget = 'min_daily_budget'
        min_live_boosting_budget = 'min_live_boosting_budget'
        min_payment = 'min_payment'
        minimum_budgets = 'minimum_budgets'
        modeled_reporting_type = 'modeled_reporting_type'
        moo_default_conversion_bid = 'moo_default_conversion_bid'
        name = 'name'
        next_bill_date = 'next_bill_date'
        offsite_pixels_tos_accepted = 'offsite_pixels_tos_accepted'
        onbehalf_requests = 'onbehalf_requests'
        opportunity_score = 'opportunity_score'
        opportunity_score_weight = 'opportunity_score_weight'
        owner = 'owner'
        owner_business = 'owner_business'
        page_authorized_country_for_political_ads = 'page_authorized_country_for_political_ads'
        pages_in_authorizations = 'pages_in_authorizations'
        partner = 'partner'
        payment_options = 'payment_options'
        pending_billing_date_preference = 'pending_billing_date_preference'
        prepay_account_balance = 'prepay_account_balance'
        promotion_metadata = 'promotion_metadata'
        promotion_metadata_live_crawl = 'promotion_metadata_live_crawl'
        publisher_block_lists = 'publisher_block_lists'
        reachestimate = 'reachestimate'
        reachfrequencypredictions = 'reachfrequencypredictions'
        recommendations = 'recommendations'
        rf_spec = 'rf_spec'
        sales_segment_v2 = 'sales_segment_v2'
        saved_audiences = 'saved_audiences'
        segment = 'segment'
        send_bill_to_address = 'send_bill_to_address'
        send_bill_to_addresses = 'send_bill_to_addresses'
        show_improved_boleto = 'show_improved_boleto'
        show_sac_campaign_group_input = 'show_sac_campaign_group_input'
        site_links_live_crawl = 'site_links_live_crawl'
        sold_to_address = 'sold_to_address'
        sold_to_addresses = 'sold_to_addresses'
        spend_cap = 'spend_cap'
        spend_cap_history = 'spend_cap_history'
        spendlimits = 'spendlimits'
        stored_balance_status = 'stored_balance_status'
        subscribed_apps = 'subscribed_apps'
        targetingbrowse = 'targetingbrowse'
        targetingsearch = 'targetingsearch'
        targetingsuggestions = 'targetingsuggestions'
        tax_country = 'tax_country'
        tax_exempt = 'tax_exempt'
        tax_id = 'tax_id'
        tax_id_status = 'tax_id_status'
        tax_id_type = 'tax_id_type'
        timezone_id = 'timezone_id'
        timezone_name = 'timezone_name'
        timezone_offset_hours_utc = 'timezone_offset_hours_utc'
        tos_accepted = 'tos_accepted'
        total_prepay_balance = 'total_prepay_balance'
        tracking = 'tracking'
        transactions = 'transactions'
        user_access_expire_time = 'user_access_expire_time'
        user_role = 'user_role'
        user_settings = 'user_settings'
        user_tasks = 'user_tasks'
        user_tos_accepted = 'user_tos_accepted'
        users = 'users'
        value_rule_set = 'value_rule_set'
        viewable_business = 'viewable_business'
        viewable_businesses = 'viewable_businesses'

    class AuthFlowForTrustTierState:
        expired = 'EXPIRED'
        failed = 'FAILED'
        in_review = 'IN_REVIEW'
        not_required = 'NOT_REQUIRED'
        not_started = 'NOT_STARTED'
        pending = 'PENDING'
        pending_in_review = 'PENDING_IN_REVIEW'
        revoked = 'REVOKED'
        verified = 'VERIFIED'

    class AuthorizedCountryForPoliticalAds:
        ac = 'AC'
        ad = 'AD'
        ae = 'AE'
        af = 'AF'
        ag = 'AG'
        ai = 'AI'
        al = 'AL'
        am = 'AM'
        an = 'AN'
        ao = 'AO'
        aq = 'AQ'
        ar = 'AR'
        value_as = 'AS'
        at = 'AT'
        au = 'AU'
        aw = 'AW'
        ax = 'AX'
        az = 'AZ'
        ba = 'BA'
        bb = 'BB'
        bd = 'BD'
        be = 'BE'
        bf = 'BF'
        bg = 'BG'
        bh = 'BH'
        bi = 'BI'
        bj = 'BJ'
        bl = 'BL'
        bm = 'BM'
        bn = 'BN'
        bo = 'BO'
        bq = 'BQ'
        br = 'BR'
        bs = 'BS'
        bt = 'BT'
        bv = 'BV'
        bw = 'BW'
        by = 'BY'
        bz = 'BZ'
        ca = 'CA'
        cc = 'CC'
        cd = 'CD'
        cf = 'CF'
        cg = 'CG'
        ch = 'CH'
        ci = 'CI'
        ck = 'CK'
        cl = 'CL'
        cm = 'CM'
        cn = 'CN'
        co = 'CO'
        cr = 'CR'
        cu = 'CU'
        cv = 'CV'
        cw = 'CW'
        cx = 'CX'
        cy = 'CY'
        cz = 'CZ'
        de = 'DE'
        dj = 'DJ'
        dk = 'DK'
        dm = 'DM'
        do = 'DO'
        dz = 'DZ'
        ec = 'EC'
        ee = 'EE'
        eg = 'EG'
        eh = 'EH'
        er = 'ER'
        es = 'ES'
        et = 'ET'
        fi = 'FI'
        fj = 'FJ'
        fk = 'FK'
        fm = 'FM'
        fo = 'FO'
        fr = 'FR'
        ga = 'GA'
        gb = 'GB'
        gd = 'GD'
        ge = 'GE'
        gf = 'GF'
        gg = 'GG'
        gh = 'GH'
        gi = 'GI'
        gl = 'GL'
        gm = 'GM'
        gn = 'GN'
        gp = 'GP'
        gq = 'GQ'
        gr = 'GR'
        gs = 'GS'
        gt = 'GT'
        gu = 'GU'
        gw = 'GW'
        gy = 'GY'
        hk = 'HK'
        hm = 'HM'
        hn = 'HN'
        hr = 'HR'
        ht = 'HT'
        hu = 'HU'
        id = 'ID'
        ie = 'IE'
        il = 'IL'
        im = 'IM'
        value_in = 'IN'
        io = 'IO'
        iq = 'IQ'
        ir = 'IR'
        value_is = 'IS'
        it = 'IT'
        je = 'JE'
        jm = 'JM'
        jo = 'JO'
        jp = 'JP'
        ke = 'KE'
        kg = 'KG'
        kh = 'KH'
        ki = 'KI'
        km = 'KM'
        kn = 'KN'
        kp = 'KP'
        kr = 'KR'
        kw = 'KW'
        ky = 'KY'
        kz = 'KZ'
        la = 'LA'
        lb = 'LB'
        lc = 'LC'
        li = 'LI'
        lk = 'LK'
        lr = 'LR'
        ls = 'LS'
        lt = 'LT'
        lu = 'LU'
        lv = 'LV'
        ly = 'LY'
        ma = 'MA'
        mc = 'MC'
        md = 'MD'
        me = 'ME'
        mf = 'MF'
        mg = 'MG'
        mh = 'MH'
        mk = 'MK'
        ml = 'ML'
        mm = 'MM'
        mn = 'MN'
        mo = 'MO'
        mp = 'MP'
        mq = 'MQ'
        mr = 'MR'
        ms = 'MS'
        mt = 'MT'
        mu = 'MU'
        mv = 'MV'
        mw = 'MW'
        mx = 'MX'
        my = 'MY'
        mz = 'MZ'
        na = 'NA'
        nc = 'NC'
        ne = 'NE'
        nf = 'NF'
        ng = 'NG'
        ni = 'NI'
        nl = 'NL'
        no = 'NO'
        np = 'NP'
        nr = 'NR'
        nu = 'NU'
        nz = 'NZ'
        om = 'OM'
        pa = 'PA'
        pe = 'PE'
        pf = 'PF'
        pg = 'PG'
        ph = 'PH'
        pk = 'PK'
        pl = 'PL'
        pm = 'PM'
        pn = 'PN'
        pr = 'PR'
        ps = 'PS'
        pt = 'PT'
        pw = 'PW'
        py = 'PY'
        qa = 'QA'
        re = 'RE'
        ro = 'RO'
        rs = 'RS'
        ru = 'RU'
        rw = 'RW'
        sa = 'SA'
        sb = 'SB'
        sc = 'SC'
        sd = 'SD'
        se = 'SE'
        sg = 'SG'
        sh = 'SH'
        si = 'SI'
        sj = 'SJ'
        sk = 'SK'
        sl = 'SL'
        sm = 'SM'
        sn = 'SN'
        so = 'SO'
        sr = 'SR'
        ss = 'SS'
        st = 'ST'
        sv = 'SV'
        sx = 'SX'
        sy = 'SY'
        sz = 'SZ'
        tc = 'TC'
        td = 'TD'
        tf = 'TF'
        tg = 'TG'
        th = 'TH'
        tj = 'TJ'
        tk = 'TK'
        tl = 'TL'
        tm = 'TM'
        tn = 'TN'
        to = 'TO'
        tr = 'TR'
        tt = 'TT'
        tv = 'TV'
        tw = 'TW'
        tz = 'TZ'
        ua = 'UA'
        ug = 'UG'
        um = 'UM'
        us = 'US'
        uy = 'UY'
        uz = 'UZ'
        va = 'VA'
        vc = 'VC'
        ve = 'VE'
        vg = 'VG'
        vi = 'VI'
        vn = 'VN'
        vu = 'VU'
        wf = 'WF'
        ws = 'WS'
        xk = 'XK'
        ye = 'YE'
        yt = 'YT'
        za = 'ZA'
        zm = 'ZM'
        zw = 'ZW'

    class BrandSafetyExcludedTopics:
        fb_instream_reels_non_partner_publishers = 'FB_INSTREAM_REELS_NON_PARTNER_PUBLISHERS'
        fb_reels_non_partner_publishers = 'FB_REELS_NON_PARTNER_PUBLISHERS'
        gaming = 'GAMING'
        instream_live = 'INSTREAM_LIVE'
        instream_non_partner_publishers = 'INSTREAM_NON_PARTNER_PUBLISHERS'
        news = 'NEWS'
        politics = 'POLITICS'
        religion_and_spirituality = 'RELIGION_AND_SPIRITUALITY'

    class BusinessRestrictionReason:
        banhammer = 'BANHAMMER'
        email_required = 'EMAIL_REQUIRED'
        none = 'NONE'

    class BusinessVerificationStatus:
        expired = 'EXPIRED'
        failed = 'FAILED'
        ineligible = 'INELIGIBLE'
        not_verified = 'NOT_VERIFIED'
        pending = 'PENDING'
        pending_need_more_info = 'PENDING_NEED_MORE_INFO'
        pending_submission = 'PENDING_SUBMISSION'
        rejected = 'REJECTED'
        revoked = 'REVOKED'
        verified = 'VERIFIED'

    class FlexSingleObjective:
        app_promotion = 'APP_PROMOTION'
        group_joins = 'GROUP_JOINS'
        instagram_performance = 'INSTAGRAM_PERFORMANCE'
        leads = 'LEADS'
        none = 'NONE'
        sales = 'SALES'
        traffic = 'TRAFFIC'

    class MarketingMessageEnablementStatus:
        marketing_message_eligible_optimization_disabled = 'MARKETING_MESSAGE_ELIGIBLE_OPTIMIZATION_DISABLED'
        marketing_message_eligible_optimization_enabled = 'MARKETING_MESSAGE_ELIGIBLE_OPTIMIZATION_ENABLED'
        marketing_message_ineligible = 'MARKETING_MESSAGE_INELIGIBLE'

    class ModeledReportingType:
        ios14_account = 'IOS14_ACCOUNT'
        none = 'NONE'

    class Segment:
        hair = 'HAIR'
        head = 'HEAD'
        null = 'NULL'
        tail = 'TAIL'
        torso = 'TORSO'

    class StoredBalanceStatus:
        new_user = 'NEW_USER'
        postpay = 'POSTPAY'
        prepay = 'PREPAY'
        standard = 'STANDARD'

    _field_types = {
        'account_controls': 'object',
        'account_currency_ratio_to_usd': 'float',
        'account_id': 'string',
        'account_status': 'int',
        'active_billing_date_preference': 'object',
        'activities': 'object',
        'ad_account_promotable_objects': 'object',
        'ad_column_sizes': 'object',
        'ad_limits_insights': 'object',
        'adcreatives': 'object',
        'addrafts': 'object',
        'adimages': 'object',
        'adlabels': 'object',
        'adrules_count_by_type': 'object',
        'adrules_history': 'object',
        'adrules_library': 'object',
        'ads': 'object',
        'ads_paused': 'bool',
        'ads_volume': 'object',
        'adsets': 'object',
        'adspaymentcycle': 'object',
        'adspixels': 'object',
        'adtrust_dsl': 'float',
        'advertisable_applications': 'object',
        'advideos': 'object',
        'age': 'float',
        'agencies': 'object',
        'agency_client_declaration': 'object',
        'agency_fee_config': 'object',
        'ai_generated_features_test_framework_enrolled': 'bool',
        'all_capabilities': 'list<string>',
        'all_payment_methods': 'object',
        'am_oneshop_settings': 'object',
        'amount_spent': 'string',
        'amount_spent_history': 'list<object>',
        'applications': 'object',
        'applied_publisher_block_lists': 'object',
        'archived_adgroup_count': 'int',
        'archived_campaign_count': 'int',
        'archived_campaign_group_count': 'int',
        'asset_feed_spec_from_existing_post': 'object',
        'asset_feed_spec_from_instagram_media': 'object',
        'asset_score': 'float',
        'assigned_partners': 'object',
        'attr_window_deprecation_group': 'string',
        'auth_flow_for_trust_tier_state': 'AuthFlowForTrustTierState',
        'authorized_country_for_political_ads': 'AuthorizedCountryForPoliticalAds',
        'automatic_creative_optimization_test_framework_enrolled': 'bool',
        'average_daily_campaign_budget': 'string',
        'average_daily_campaign_group_budget': 'string',
        'average_lifetime_campaign_budget': 'string',
        'average_lifetime_campaign_group_budget': 'string',
        'balance': 'string',
        'brand_safety_content_filter_levels': 'list<string>',
        'brand_safety_excluded_topics': 'list<BrandSafetyExcludedTopics>',
        'business': 'object',
        'business_ad_account_requests': 'object',
        'business_city': 'string',
        'business_country_code': 'string',
        'business_name': 'string',
        'business_restriction_reason': 'BusinessRestrictionReason',
        'business_state': 'string',
        'business_street': 'string',
        'business_street2': 'string',
        'business_verification_status': 'BusinessVerificationStatus',
        'business_zip': 'string',
        'businessprojects': 'object',
        'call_ads_ad_account_similar_advertiser_budget_recommendation': 'float',
        'call_ads_similar_advertiser_budget_recommendation': 'object',
        'campaign_group_with_cbo': 'object',
        'campaigns': 'object',
        'can_bypass_fs_check': 'bool',
        'can_create_brand_lift_study': 'bool',
        'can_pay_now': 'bool',
        'can_remove_payment_methods': 'bool',
        'can_repay_now': 'bool',
        'can_see_collaborative_ads_reporting': 'bool',
        'capabilities': 'list<string>',
        'connected_instagram_accounts': 'object',
        'cpas_campaign_default_budget': 'int',
        'cpas_campaign_group_default_budget': 'int',
        'created_time': 'mixed',
        'creation_packages': 'object',
        'ctwa_smb_enforcing_days_left': 'int',
        'ctx_advertiser_sabr_lifetime_duration_recommendation': 'int',
        'ctx_dfo_objective_defaults': 'object',
        'ctx_flexible_format_targeting': 'bool',
        'currency': 'string',
        'current_addrafts': 'object',
        'current_unbilled_spend': 'object',
        'current_unpaid_unrepaid_invoice': 'object',
        'custom_audience_info': 'object',
        'customaudiences': 'object',
        'customconversions': 'object',
        'customer_po_number': 'string',
        'daily_spend_limit': 'object',
        'dcaf': 'bool',
        'default_dsa_beneficiary': 'string',
        'default_dsa_payor': 'string',
        'default_unified_attribution_spec': 'list<object>',
        'default_values': 'object',
        'disable_reason': 'int',
        'domain_and_site_links': 'object',
        'dsa_recommendations': 'object',
        'dynamic_probation_dsl': 'float',
        'end_advertiser': 'int',
        'end_advertiser_name': 'string',
        'existing_customers': 'list<string>',
        'expired_funding_source_details': 'object',
        'extended_credit': 'object',
        'extended_credit_info': 'object',
        'extended_credit_invoice_group': 'object',
        'failed_delivery_checks': 'list<object>',
        'fb_entity': 'int',
        'flex_single_objective': 'FlexSingleObjective',
        'funding_source': 'int',
        'funding_source_details': 'object',
        'generatepreviews': 'object',
        'has_active_skan_campaign_groups': 'bool',
        'has_combo_cards_on_file': 'bool',
        'has_extended_credit': 'bool',
        'has_migrated_permissions': 'bool',
        'has_page_authorized_adaccount': 'bool',
        'has_personal_access': 'bool',
        'has_purchase_optimization_eligible_page': 'bool',
        'has_repay_processing_invoices': 'bool',
        'has_started_purchase_optimized_ctm_ad_within_1d': 'bool',
        'has_value_rule_set': 'bool',
        'id': 'string',
        'if_viewer_has_permission_to_advertise': 'bool',
        'incremental_conversion_optimization_ad_studies': 'list<object>',
        'instagram_accounts': 'object',
        'invoicing_emails': 'object',
        'ios_fourteen_campaign_limits': 'object',
        'is_attribution_spec_system_default': 'bool',
        'is_ba_skip_delayed_eligible': 'bool',
        'is_biz_migration_eligible': 'bool',
        'is_br_entity_account': 'bool',
        'is_business_allowed_to_advertise': 'bool',
        'is_business_verification_eligible': 'bool',
        'is_closed_by_advertiser_compromise_bot': 'bool',
        'is_collaborative_ads_ad_account': 'bool',
        'is_ctx_advertiser': 'bool',
        'is_direct_deals_enabled': 'bool',
        'is_disabled_umbrella': 'bool',
        'is_eligible_for_advantage_plus_creative_regulated_category': 'bool',
        'is_expanded_shopless_awpt_eligible': 'bool',
        'is_in_3ds_authorization_enabled_market': 'bool',
        'is_mi_billing_info_updated': 'bool',
        'is_mm_lite_api_enabled': 'bool',
        'is_new_advertiser': 'bool',
        'is_notifications_enabled': 'bool',
        'is_oba_opt_out': 'bool',
        'is_omnichannel_campaign_eligible': 'bool',
        'is_pageless_ctwa_eligible': 'bool',
        'is_pending_numbers_exposure_flag_enabled': 'bool',
        'is_personal': 'int',
        'is_pinless_debit_eligible': 'bool',
        'is_placement_soft_opt_out_enabled': 'bool',
        'is_prepay_account': 'bool',
        'is_retail_media_network': 'bool',
        'is_shopless_awpt_eligible': 'bool',
        'is_tax_id_required': 'bool',
        'is_tier_0': 'bool',
        'is_tier_0_full': 'bool',
        'is_tier_1': 'bool',
        'is_tier_restricted': 'bool',
        'is_update_timezone_currency_too_recently': 'bool',
        'is_user_allowed_to_advertise': 'bool',
        'is_using_higher_daily_flex_rate': 'bool',
        'is_value_rules_smart_default_on': 'bool',
        'is_wa_cloud_api_user': 'bool',
        'is_youth_ads_pao_basic_advertiser': 'bool',
        'is_youth_ads_pao_basic_advertiser_announcement_eligible': 'bool',
        'last_spend_time': 'int',
        'last_used_time': 'int',
        'liable_address': 'object',
        'liable_addresses': 'object',
        'live_video_advertiser_details': 'object',
        'marketing_message_enablement_status': 'MarketingMessageEnablementStatus',
        'marketing_messages_settings': 'object',
        'max_bid': 'object',
        'max_billing_threshold': 'object',
        'maybe_pac_internal_post_from_primary_post': 'string',
        'media_agency': 'int',
        'min_billing_threshold': 'object',
        'min_campaign_group_spend_cap': 'string',
        'min_daily_budget': 'int',
        'min_live_boosting_budget': 'int',
        'min_payment': 'object',
        'minimum_budgets': 'object',
        'modeled_reporting_type': 'ModeledReportingType',
        'moo_default_conversion_bid': 'int',
        'name': 'string',
        'next_bill_date': 'int',
        'offsite_pixels_tos_accepted': 'bool',
        'onbehalf_requests': 'object',
        'opportunity_score': 'float',
        'opportunity_score_weight': 'int',
        'owner': 'string',
        'owner_business': 'object',
        'page_authorized_country_for_political_ads': 'list<object>',
        'pages_in_authorizations': 'list<object>',
        'partner': 'int',
        'payment_options': 'object',
        'pending_billing_date_preference': 'object',
        'prepay_account_balance': 'object',
        'promotion_metadata': 'list<object>',
        'promotion_metadata_live_crawl': 'list<object>',
        'publisher_block_lists': 'object',
        'reachestimate': 'object',
        'reachfrequencypredictions': 'object',
        'recommendations': 'object',
        'rf_spec': 'object',
        'sales_segment_v2': 'string',
        'saved_audiences': 'object',
        'segment': 'Segment',
        'send_bill_to_address': 'object',
        'send_bill_to_addresses': 'object',
        'show_improved_boleto': 'bool',
        'show_sac_campaign_group_input': 'bool',
        'site_links_live_crawl': 'list<object>',
        'sold_to_address': 'object',
        'sold_to_addresses': 'object',
        'spend_cap': 'string',
        'spend_cap_history': 'list<object>',
        'spendlimits': 'object',
        'stored_balance_status': 'StoredBalanceStatus',
        'subscribed_apps': 'object',
        'targetingbrowse': 'object',
        'targetingsearch': 'object',
        'targetingsuggestions': 'object',
        'tax_country': 'string',
        'tax_exempt': 'bool',
        'tax_id': 'string',
        'tax_id_status': 'int',
        'tax_id_type': 'string',
        'timezone_id': 'int',
        'timezone_name': 'string',
        'timezone_offset_hours_utc': 'float',
        'tos_accepted': 'map<int, int>',
        'total_prepay_balance': 'object',
        'tracking': 'object',
        'transactions': 'object',
        'user_access_expire_time': 'int',
        'user_role': 'string',
        'user_settings': 'object',
        'user_tasks': 'list<string>',
        'user_tos_accepted': 'map<int, int>',
        'users': 'object',
        'value_rule_set': 'object',
        'viewable_business': 'object',
        'viewable_businesses': 'list<object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AuthFlowForTrustTierState'] = AdAccountGet.AuthFlowForTrustTierState.__dict__.values()
        field_enum_info['AuthorizedCountryForPoliticalAds'] = AdAccountGet.AuthorizedCountryForPoliticalAds.__dict__.values()
        field_enum_info['BrandSafetyExcludedTopics'] = AdAccountGet.BrandSafetyExcludedTopics.__dict__.values()
        field_enum_info['BusinessRestrictionReason'] = AdAccountGet.BusinessRestrictionReason.__dict__.values()
        field_enum_info['BusinessVerificationStatus'] = AdAccountGet.BusinessVerificationStatus.__dict__.values()
        field_enum_info['FlexSingleObjective'] = AdAccountGet.FlexSingleObjective.__dict__.values()
        field_enum_info['MarketingMessageEnablementStatus'] = AdAccountGet.MarketingMessageEnablementStatus.__dict__.values()
        field_enum_info['ModeledReportingType'] = AdAccountGet.ModeledReportingType.__dict__.values()
        field_enum_info['Segment'] = AdAccountGet.Segment.__dict__.values()
        field_enum_info['StoredBalanceStatus'] = AdAccountGet.StoredBalanceStatus.__dict__.values()
        return field_enum_info


