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

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ProductCatalogDiagnosticGroup(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProductCatalogDiagnosticGroup, self).__init__()
        self._isProductCatalogDiagnosticGroup = True
        self._api = api

    class Field(AbstractObject.Field):
        affected_channels = 'affected_channels'
        affected_features = 'affected_features'
        diagnostics = 'diagnostics'
        error_code = 'error_code'
        number_of_affected_items = 'number_of_affected_items'
        severity = 'severity'
        subtitle = 'subtitle'
        title = 'title'
        type = 'type'

    class AffectedChannels:
        business_inbox_in_messenger = 'business_inbox_in_messenger'
        shops = 'shops'
        test_capability = 'test_capability'
        universal_checkout = 'universal_checkout'
        us_marketplace = 'us_marketplace'

    class AffectedFeatures:
        augmented_reality = 'augmented_reality'
        checkout = 'checkout'

    class Severity:
        must_fix = 'MUST_FIX'
        opportunity = 'OPPORTUNITY'

    class Type:
        attributes_invalid = 'ATTRIBUTES_INVALID'
        attributes_missing = 'ATTRIBUTES_MISSING'
        category = 'CATEGORY'
        checkout = 'CHECKOUT'
        image_quality = 'IMAGE_QUALITY'
        low_quality_title_and_description = 'LOW_QUALITY_TITLE_AND_DESCRIPTION'
        policy_violation = 'POLICY_VIOLATION'
        shops_visibility_issues = 'SHOPS_VISIBILITY_ISSUES'

    class Severities:
        must_fix = 'MUST_FIX'
        opportunity = 'OPPORTUNITY'

    class Types:
        attributes_invalid = 'ATTRIBUTES_INVALID'
        attributes_missing = 'ATTRIBUTES_MISSING'
        category = 'CATEGORY'
        checkout = 'CHECKOUT'
        image_quality = 'IMAGE_QUALITY'
        low_quality_title_and_description = 'LOW_QUALITY_TITLE_AND_DESCRIPTION'
        policy_violation = 'POLICY_VIOLATION'
        shops_visibility_issues = 'SHOPS_VISIBILITY_ISSUES'

    _field_types = {
        'affected_channels': 'list<AffectedChannels>',
        'affected_features': 'list<AffectedFeatures>',
        'diagnostics': 'list<Object>',
        'error_code': 'int',
        'number_of_affected_items': 'int',
        'severity': 'Severity',
        'subtitle': 'string',
        'title': 'string',
        'type': 'Type',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AffectedChannels'] = ProductCatalogDiagnosticGroup.AffectedChannels.__dict__.values()
        field_enum_info['AffectedFeatures'] = ProductCatalogDiagnosticGroup.AffectedFeatures.__dict__.values()
        field_enum_info['Severity'] = ProductCatalogDiagnosticGroup.Severity.__dict__.values()
        field_enum_info['Type'] = ProductCatalogDiagnosticGroup.Type.__dict__.values()
        field_enum_info['Severities'] = ProductCatalogDiagnosticGroup.Severities.__dict__.values()
        field_enum_info['Types'] = ProductCatalogDiagnosticGroup.Types.__dict__.values()
        return field_enum_info


