# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# ============================================================================
# Get Lift Study Results Example
# ============================================================================
#
# This example shows how to retrieve a Conversion Lift Study (CLS) and its
# results using the Facebook Business SDK.
#
# Prerequisites:
#   1. Create a Meta App and retrieve your App ID and App Secret.
#      - Go to https://developers.facebook.com/apps/ and select your app.
#      - App ID is at the top of the dashboard.
#      - App Secret is under Settings > Basic (click "Show" to reveal).
#
#   2. Generate a System User access token with permissions:
#      ads_management, ads_read, business_management.
#      - Go to Business Manager > Business Settings > Users > System Users.
#      - Assign your Meta App (Add Assets > Applications).
#      - Click "Generate Token" and select the permissions above.
#
#   3. Install dependencies:
#      pip install facebook-business pandas
# ============================================================================

import json
import pandas as pd
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adstudy import AdStudy

# --- Configuration -----------------------------------------------------------
APP_ID = '<YOUR_APP_ID>'
APP_SECRET = '<YOUR_APP_SECRET>'
ACCESS_TOKEN = '<YOUR_ACCESS_TOKEN>'
STUDY_ID = '<YOUR_STUDY_ID>'

# --- Initialize the SDK ------------------------------------------------------
FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN)

# --- Retrieve Study dates ----------------------------------------------------
study = AdStudy(STUDY_ID)
study_data = study.api_get(fields=[
    AdStudy.Field.name,
    AdStudy.Field.start_time,
    AdStudy.Field.end_time,
])
print("Study:", study_data.get('name'))
print("Start:", study_data.get('start_time'))
print("End:  ", study_data.get('end_time'))

# --- Retrieve Study cells (treatment / control) ------------------------------
cells = list(study.get_cells())
print("\nCells:", cells)

# --- Retrieve objectives and parse results ------------------------------------
objectives = study.get_objectives(fields=['id', 'results'])

all_results = []
for objective in objectives:
    for result_string in objective.get('results', []):
        data = json.loads(result_string)
        data['study_start_time'] = study_data.get('start_time')
        data['study_end_time'] = study_data.get('end_time')
        data['objective_id'] = objective.get('id')
        all_results.append(data)

df = pd.DataFrame(all_results)
print("\nResults:")
print(df.head())
