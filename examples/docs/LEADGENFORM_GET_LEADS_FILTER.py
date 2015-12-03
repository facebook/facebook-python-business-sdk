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

from examples.docs import fixtures

leadgen_form_id = fixtures.get_leadgen_form().get_id()

# _DOC oncall [raven]
# _DOC open [LEADGENFORM_GET_LEADS_FILTER]
# _DOC vars [leadgen_form_id]
from facebookads.objects import LeadgenForm
import datetime

yesterday = datetime.date.today() - datetime.timedelta(1)
timestamp = yesterday.strftime("%s")

form = LeadgenForm(leadgen_form_id)
leads = form.get_leads(params={
    'filtering': [{
        'field': 'time_created',
        'operator': 'GREATER_THAN',
        'value': timestamp,
    }],
})
# _DOC close [LEADGENFORM_GET_LEADS_FILTER]
