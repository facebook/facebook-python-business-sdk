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

from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative

import itertools
from batch_utils import generate_batches
from simple_create import api

def create_multiple_website_clicks_ads(
    account,

    name,
    country,

    titles,
    bodies,
    urls,
    image_paths,

    optimization_goal,
    pixel_id,
    billing_event,
    bid_amount,
    daily_budget=None,
    lifetime_budget=None,
    start_time=None,
    end_time=None,

    age_min=None,
    age_max=None,
    genders=None,

    campaign=None,
    status=AdSet.Status.paused,
):
    # Check for bad specs
    if daily_budget is None:
        if lifetime_budget is None:
            raise TypeError(
                'One of daily_budget or lifetime_budget must be defined.'
            )
        elif end_time is None:
            raise TypeError(
                'If lifetime_budget is defined, end_time must be defined.'
            )

    # Create campaign
    if campaign:
        campaign = Campaign(fbid=campaign)[Campaign.Field.id]
    else:
        campaign = Campaign(parent_id=account)
        campaign[Campaign.Field.name] = name + ' Campaign'
        campaign[Campaign.Field.objective] = \
            Campaign.Objective.conversions
        campaign[Campaign.Field.status] = \
            Campaign.Status.active if not status \
            else Campaign.Status.paused
        campaign.remote_create()
        campaign = campaign[AdSet.Field.id]

    # Create ad set
    ad_set = AdSet(parent_id=account)
    ad_set[AdSet.Field.campaign_id] = campaign
    ad_set[AdSet.Field.name] = name + ' AdSet'
    ad_set[AdSet.Field.optimization_goal] = optimization_goal
    ad_set[AdSet.Field.promoted_object] = {
        'pixel_id': pixel_id,
        'custom_event_type': 'COMPLETE_REGISTRATION'

    }
    ad_set[AdSet.Field.billing_event] = billing_event
    ad_set[AdSet.Field.bid_amount] = bid_amount

    if daily_budget:
        ad_set[AdSet.Field.daily_budget] = daily_budget
    else:
        ad_set[AdSet.Field.lifetime_budget] = lifetime_budget
    if end_time:
        ad_set[AdSet.Field.end_time] = end_time
    if start_time:
        ad_set[AdSet.Field.start_time] = start_time
    targeting = {}
    targeting[Targeting.Field.geo_locations] = {
        'countries': [country]
    }
    if age_max:
        targeting[Targeting.Field.age_max] = age_max
    if age_min:
        targeting[Targeting.Field.age_min] = age_min
    if genders:
        targeting[Targeting.Field.genders] = genders
    ad_set[AdSet.Field.targeting] = targeting

    ad_set.remote_create()

    # Upload the images first one by one
    image_hashes = []
    for image_path in image_paths:
        img = AdImage(parent_id=account)
        img[AdImage.Field.filename] = image_path
        img.remote_create()
        image_hashes.append(img.get_hash())

    ADGROUP_BATCH_CREATE_LIMIT = 10
    ad_groups_created = []

    def callback_failure(response):
        raise response.error()

    # For each creative permutation
    for creative_info_batch in generate_batches(
        itertools.product(titles, bodies, urls, image_hashes),
        ADGROUP_BATCH_CREATE_LIMIT
    ):
        api_batch = api.new_batch()

        for title, body, url, image_hash in creative_info_batch:
            # Create the ad
            ad = Ad(parent_id=account)
            ad[Ad.Field.name] = name + ' Ad'
            ad[Ad.Field.adset_id] = ad_set[AdSet.Field.id]
            ad[Ad.Field.creative] = {
                AdCreative.Field.title: title,
                AdCreative.Field.body: body,
                AdCreative.Field.object_url: url,
                AdCreative.Field.image_hash: image_hash,
            }
            ad[Ad.Field.status] = status

            ad.remote_create(batch=api_batch, failure=callback_failure)
            ad_groups_created.append(ad)

        api_batch.execute()

    return ad_groups_created


def create_website_clicks_ad(
    account,

    name,
    country,

    title,
    body,
    url,
    image_path,

    optimization_goal,
    pixel_id,
    billing_event,
    bid_amount,
    daily_budget=None,
    lifetime_budget=None,
    start_time=None,
    end_time=None,

    age_min=None,
    age_max=None,
    genders=None,

    campaign=None,
    status=AdSet.Status.paused,
):
    for ad in create_multiple_website_clicks_ads(
        account=account,

        name=name,
        country=country,

        titles=[title],
        bodies=[body],
        urls=[url],
        image_paths=[image_path],

        optimization_goal=optimization_goal,
        pixel_id=pixel_id,
        billing_event=billing_event,
        bid_amount=bid_amount,
        daily_budget=daily_budget,
        lifetime_budget=lifetime_budget,
        start_time=start_time,
        end_time=end_time,

        age_min=age_min,
        age_max=age_max,
        genders=genders,

        campaign=campaign,
        status=Ad.Status.paused,
    ):
        return ad
