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
Create, delete and list custom audiences
Requires: the Facebook Python Ads SDK
https://github.com/facebook/facebook-python-ads-sdk
"""

from facebook_business import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
import argparse
import json
import os
import pprint
import sys

pp = pprint.pprint

this_dir = os.path.dirname(__file__)
config_filename = os.path.join(this_dir, 'config.json')

### Setup session and api objects
config_file = open(config_filename)
config = json.load(config_file)
config_file.close()

auth_info = (
    config['app_id'],
    config['app_secret'],
    config['access_token'])

FacebookAdsApi.init(*auth_info)

### Get account from config file
my_account = AdAccount(config['act_id'])

def ListCustomAudiences(**kwargs):
    audiences = my_account.get_custom_audiences(fields=[
        CustomAudience.Field.name,
        CustomAudience.Field.description])
    if audiences:
        print(">>> Account")
        print(my_account[CustomAudience.Field.id])
        print(">>> Audiences")

    for audience in audiences:
        print(audience[CustomAudience.Field.id] + ': ' +
              audience[CustomAudience.Field.name])


def DeleteCustomAudience(audience_id):
    audience = CustomAudience(audience_id)
    print('Deleting audience id ' + audience[CustomAudience.Field.id])
    return audience.api_delete()


def CreateCustomAudience(name, description=None, f=None, datatype='email'):
    params = {
        CustomAudience.Field.name: name,
        CustomAudience.Field.subtype: CustomAudience.Subtype.custom,
        CustomAudience.Field.customer_file_source: CustomAudience.CustomerFileSource.user_provided_only,
    }
    audience = my_account.create_custom_audience(fields=[], params=params)
    print('Created custom audience id ' + audience.get_id_assured())

    if description:
        audience = audience.api_update(fields=[], params={CustomAudience.Field.description: description})
        print("Update description to : " + audience.api_get(fields=[CustomAudience.Field.description])[CustomAudience.Field.description])
    if f and datatype:
        LoadCustomAudience(audience, f, datatype)



def LoadCustomAudience(audience, f, datatype, schema=None, app_ids=None):
    # File format is one type per file (ie email), and one entry per line
    if datatype == 'email':
        schema = CustomAudience.Schema.email_hash
    elif datatype == 'phone':
        schema = CustomAudience.Schema.phone_hash
    elif datatype == 'mobile_id':
        schema = CustomAudience.Schema.mobile_advertiser_id
    elif datatype == 'uid':
        schema = CustomAudience.Schema.uid
    else:
        sys.exit("[ERROR] invalid datatype " + datatype)

    print('Adding users to audience using ' + str(schema))
    data = [line.strip() for line in f]
    r = audience.add_users(schema, data, app_ids=app_ids)
    pp(r._body)


if __name__ == '__main__':
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='Facebook Custom Audiences')
    exgroup = parser.add_mutually_exclusive_group(required=True)
    exgroup.add_argument('-l', '--list', action='store_true',
                         help='list audiences')
    exgroup.add_argument('-d', '--delete', type=int, metavar='id',
                         help='delete audience')
    exgroup.add_argument('-c', '--create', metavar='name',
                         help='create a new audience')

    create_group = parser.add_argument_group('Audience creation')
    create_group.add_argument('--file', type=argparse.FileType('rb'),
                              help='text file to read from')
    create_group.add_argument('--datatype', choices=['email', 'phone', 'uid',
                              'mobile_id'], default='email',
                              help="data type in file (defaults to email)")
    create_group.add_argument('--description', help="(optional) description")
    create_group.add_argument('--app_id', help="required for datatype uid")
    parser.add_argument('--adaccount', metavar='id',
                        help='ad account in format act_xxx')

    args = parser.parse_args()
    vargs = vars(args)
    # list all custom audiences for account
    if args.list:
        ListCustomAudiences(**vars(args))
    # delete custom audience <id>
    elif args.delete:
        DeleteCustomAudience(str(vargs['delete']))
    # create custom audience, name required, description and data file optional
    elif args.create:
        CreateCustomAudience(args.create, args.description, args.file,
                             args.datatype)
