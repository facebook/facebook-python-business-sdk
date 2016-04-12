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

class ReachFrequencyPredictionMixin:
    def reserve(
        self,
        prediction_to_release=None,
        reach=None,
        budget=None,
        impression=None,
    ):
        params = {
            self.Field.prediction_id: self.get_id_assured(),
            self.Field.prediction_id_to_release: prediction_to_release,
            self.Field.budget: budget,
            self.Field.reach: reach,
            self.Field.impression: impression,
            self.Field.action: self.Action.reserve,
        }
        # Filter out None values.
        params = dict((k, v) for k, v in params.items() if v is not None)

        response = self.get_api_assured().call(
            'POST',
            (self.get_parent_id_assured(), self.get_endpoint()),
            params=params,
        )

        return self.__class__(response.body(), self.get_parent_id_assured())

    def cancel(self):
        params = {
            self.Field.prediction_id: self.get_id_assured(),
            self.Field.action: self.Action.cancel,
        }
        self.get_api_assured().call(
            'POST',
            (self.get_parent_id_assured(), self.get_endpoint()),
            params=params,
        )
        return self
