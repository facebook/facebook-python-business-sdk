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

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from facebook_business.exceptions import FacebookBadObjectError
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject

class AdImageMixin:
    @classmethod
    def remote_create_from_zip(cls, filename, parent_id, api=None):
        api = api or FacebookAdsApi.get_default_api()
        open_file = open(filename, 'rb')
        response = api.call(
            'POST',
            (parent_id, cls.get_endpoint()),
            files={filename: open_file},
        )
        open_file.close()

        data = response.json()

        objs = []
        for image_filename in data['images']:
            image = cls(parent_id=parent_id)
            image.update(data['images'][image_filename])
            image[cls.Field.id] = '%s:%s' % (
                parent_id[4:],
                data['images'][image_filename][cls.Field.hash],
            )
            objs.append(image)

        return objs

    def get_node_path(self):
        return (self.get_parent_id_assured(), self.get_endpoint())

    def _set_data(self, data):
        """
            `data` may have a different structure depending if you're creating
            new AdImages or iterating over existing ones using something like
            AdAccount.get_ad_images().
            While reading existing images, _set_data from AbstractCrudObject
            handles everything correctly, but we need to treat the
            remote_create case.
            remote_create sample response:
            {
              "images": {
                "8cf726a44ab7008c5cc6b4ebd2491234": {
                  "hash":"8cf726a44ab7008c5cc6b4ebd2491234",
                  "url":"https://fbcdn-photos-a.akamaihd.net/..."
                }
              }
            }
            Sample response when calling act_<ACT_ID>/adimages, used internally
            by AdAccount.get_ad_images():
            {
              "data": [
                {
                  "hash": "181b88e3cdf6464af7ed52fe488fe559",
                  "id": "1739564149602806:181b88e3cdf6464af7ed52fe488fe559"
                }
              ],
              "paging": {
                "cursors": {
                  "before": "MTczOTU2NDE0OTYwMjgwNjoxODFiODh==",
                  "after": "MTczOTU2NDE0OTYwMjgwNjoxODFiODhl=="
                }
              }
            }
        """

        if 'images' in data:
            _, data = data['images'].popitem()

            for key in map(str, data):
                self._data[key] = data[key]

                # clear history due to the update
                self._changes.pop(key, None)

            self._data[self.Field.id] = '%s:%s' % (
                self.get_parent_id_assured()[4:],
                self[self.Field.hash],
            )

            return self
        else:
            return AbstractCrudObject._set_data(self, data)

    def remote_create(
        self,
        batch=None,
        failure=None,
        files=None,
        params=None,
        success=None,
        api_version=None,
    ):
        """Uploads filename and creates the AdImage object from it.
        It has same arguments as AbstractCrudObject.remote_create except it
        does not have the files argument but requires the 'filename' property
        to be defined.
        """
        if not self[self.Field.filename]:
            raise FacebookBadObjectError(
                "AdImage required a filename to be defined.",
            )
        filename = self[self.Field.filename]
        with open(filename, 'rb') as open_file:
            return_val = AbstractCrudObject.remote_create(
                self,
                files={filename: open_file},
                batch=batch,
                failure=failure,
                params=params,
                success=success,
                api_version=api_version,
            )
        return return_val

    def get_hash(self):
        """Returns the image hash to which AdCreative's can refer."""
        return self[self.Field.hash]

    def remote_read(
        self,
        batch=None,
        failure=None,
        fields=None,
        params=None,
        success=None,
        api_version=None,
    ):
        if self[self.__class__.Field.id]:
            _, image_hash = self[self.__class__.Field.id].split(':')
            account = AdAccount(fbid=self.get_parent_id_assured())
            params = {
                'hashes': [
                    image_hash,
                ],
            }
            images = account.get_ad_images(fields=fields, params=params)
            if images:
                self._set_data(images[0]._data)
