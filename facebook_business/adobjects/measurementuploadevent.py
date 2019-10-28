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

class MeasurementUploadEvent(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isMeasurementUploadEvent = True
        super(MeasurementUploadEvent, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        aggregation_level = 'aggregation_level'
        conversion_end_date = 'conversion_end_date'
        conversion_start_date = 'conversion_start_date'
        event_status = 'event_status'
        id = 'id'
        lookback_window = 'lookback_window'
        match_universe = 'match_universe'
        partner = 'partner'
        timezone = 'timezone'
        upload_tag = 'upload_tag'

    class AggregationLevel:
        daily = 'DAILY'
        none = 'NONE'
        weekly = 'WEEKLY'

    class EventStatus:
        cancelcompleted = 'CANCELCOMPLETED'
        canceled = 'CANCELED'
        completed = 'COMPLETED'
        failed = 'FAILED'
        started = 'STARTED'
        uploaded = 'UPLOADED'

    class LookbackWindow:
        days30 = 'DAYS30'
        days45 = 'DAYS45'
        days60 = 'DAYS60'
        days90 = 'DAYS90'

    class MatchUniverse:
        full = 'FULL'
        pii = 'PII'
        pixel = 'PIXEL'

    class Timezone:
        tz_africa_accra = 'TZ_AFRICA_ACCRA'
        tz_africa_cairo = 'TZ_AFRICA_CAIRO'
        tz_africa_casablanca = 'TZ_AFRICA_CASABLANCA'
        tz_africa_johannesburg = 'TZ_AFRICA_JOHANNESBURG'
        tz_africa_lagos = 'TZ_AFRICA_LAGOS'
        tz_africa_nairobi = 'TZ_AFRICA_NAIROBI'
        tz_africa_tunis = 'TZ_AFRICA_TUNIS'
        tz_america_anchorage = 'TZ_AMERICA_ANCHORAGE'
        tz_america_argentina_buenos_aires = 'TZ_AMERICA_ARGENTINA_BUENOS_AIRES'
        tz_america_argentina_salta = 'TZ_AMERICA_ARGENTINA_SALTA'
        tz_america_argentina_san_luis = 'TZ_AMERICA_ARGENTINA_SAN_LUIS'
        tz_america_asuncion = 'TZ_AMERICA_ASUNCION'
        tz_america_atikokan = 'TZ_AMERICA_ATIKOKAN'
        tz_america_belem = 'TZ_AMERICA_BELEM'
        tz_america_blanc_sablon = 'TZ_AMERICA_BLANC_SABLON'
        tz_america_bogota = 'TZ_AMERICA_BOGOTA'
        tz_america_campo_grande = 'TZ_AMERICA_CAMPO_GRANDE'
        tz_america_caracas = 'TZ_AMERICA_CARACAS'
        tz_america_chicago = 'TZ_AMERICA_CHICAGO'
        tz_america_costa_rica = 'TZ_AMERICA_COSTA_RICA'
        tz_america_dawson = 'TZ_AMERICA_DAWSON'
        tz_america_dawson_creek = 'TZ_AMERICA_DAWSON_CREEK'
        tz_america_denver = 'TZ_AMERICA_DENVER'
        tz_america_detroit = 'TZ_AMERICA_DETROIT'
        tz_america_edmonton = 'TZ_AMERICA_EDMONTON'
        tz_america_el_salvador = 'TZ_AMERICA_EL_SALVADOR'
        tz_america_guatemala = 'TZ_AMERICA_GUATEMALA'
        tz_america_guayaquil = 'TZ_AMERICA_GUAYAQUIL'
        tz_america_halifax = 'TZ_AMERICA_HALIFAX'
        tz_america_hermosillo = 'TZ_AMERICA_HERMOSILLO'
        tz_america_iqaluit = 'TZ_AMERICA_IQALUIT'
        tz_america_jamaica = 'TZ_AMERICA_JAMAICA'
        tz_america_la_paz = 'TZ_AMERICA_LA_PAZ'
        tz_america_lima = 'TZ_AMERICA_LIMA'
        tz_america_los_angeles = 'TZ_AMERICA_LOS_ANGELES'
        tz_america_managua = 'TZ_AMERICA_MANAGUA'
        tz_america_mazatlan = 'TZ_AMERICA_MAZATLAN'
        tz_america_mexico_city = 'TZ_AMERICA_MEXICO_CITY'
        tz_america_montevideo = 'TZ_AMERICA_MONTEVIDEO'
        tz_america_nassau = 'TZ_AMERICA_NASSAU'
        tz_america_new_york = 'TZ_AMERICA_NEW_YORK'
        tz_america_noronha = 'TZ_AMERICA_NORONHA'
        tz_america_panama = 'TZ_AMERICA_PANAMA'
        tz_america_phoenix = 'TZ_AMERICA_PHOENIX'
        tz_america_port_of_spain = 'TZ_AMERICA_PORT_OF_SPAIN'
        tz_america_puerto_rico = 'TZ_AMERICA_PUERTO_RICO'
        tz_america_rainy_river = 'TZ_AMERICA_RAINY_RIVER'
        tz_america_regina = 'TZ_AMERICA_REGINA'
        tz_america_santiago = 'TZ_AMERICA_SANTIAGO'
        tz_america_santo_domingo = 'TZ_AMERICA_SANTO_DOMINGO'
        tz_america_sao_paulo = 'TZ_AMERICA_SAO_PAULO'
        tz_america_st_johns = 'TZ_AMERICA_ST_JOHNS'
        tz_america_tegucigalpa = 'TZ_AMERICA_TEGUCIGALPA'
        tz_america_tijuana = 'TZ_AMERICA_TIJUANA'
        tz_america_toronto = 'TZ_AMERICA_TORONTO'
        tz_america_vancouver = 'TZ_AMERICA_VANCOUVER'
        tz_america_winnipeg = 'TZ_AMERICA_WINNIPEG'
        tz_asia_amman = 'TZ_ASIA_AMMAN'
        tz_asia_baghdad = 'TZ_ASIA_BAGHDAD'
        tz_asia_bahrain = 'TZ_ASIA_BAHRAIN'
        tz_asia_bangkok = 'TZ_ASIA_BANGKOK'
        tz_asia_beirut = 'TZ_ASIA_BEIRUT'
        tz_asia_colombo = 'TZ_ASIA_COLOMBO'
        tz_asia_dhaka = 'TZ_ASIA_DHAKA'
        tz_asia_dubai = 'TZ_ASIA_DUBAI'
        tz_asia_gaza = 'TZ_ASIA_GAZA'
        tz_asia_hong_kong = 'TZ_ASIA_HONG_KONG'
        tz_asia_ho_chi_minh = 'TZ_ASIA_HO_CHI_MINH'
        tz_asia_irkutsk = 'TZ_ASIA_IRKUTSK'
        tz_asia_jakarta = 'TZ_ASIA_JAKARTA'
        tz_asia_jayapura = 'TZ_ASIA_JAYAPURA'
        tz_asia_jerusalem = 'TZ_ASIA_JERUSALEM'
        tz_asia_kamchatka = 'TZ_ASIA_KAMCHATKA'
        tz_asia_karachi = 'TZ_ASIA_KARACHI'
        tz_asia_kathmandu = 'TZ_ASIA_KATHMANDU'
        tz_asia_kolkata = 'TZ_ASIA_KOLKATA'
        tz_asia_krasnoyarsk = 'TZ_ASIA_KRASNOYARSK'
        tz_asia_kuala_lumpur = 'TZ_ASIA_KUALA_LUMPUR'
        tz_asia_kuwait = 'TZ_ASIA_KUWAIT'
        tz_asia_magadan = 'TZ_ASIA_MAGADAN'
        tz_asia_makassar = 'TZ_ASIA_MAKASSAR'
        tz_asia_manila = 'TZ_ASIA_MANILA'
        tz_asia_muscat = 'TZ_ASIA_MUSCAT'
        tz_asia_nicosia = 'TZ_ASIA_NICOSIA'
        tz_asia_omsk = 'TZ_ASIA_OMSK'
        tz_asia_qatar = 'TZ_ASIA_QATAR'
        tz_asia_riyadh = 'TZ_ASIA_RIYADH'
        tz_asia_seoul = 'TZ_ASIA_SEOUL'
        tz_asia_shanghai = 'TZ_ASIA_SHANGHAI'
        tz_asia_singapore = 'TZ_ASIA_SINGAPORE'
        tz_asia_taipei = 'TZ_ASIA_TAIPEI'
        tz_asia_tokyo = 'TZ_ASIA_TOKYO'
        tz_asia_vladivostok = 'TZ_ASIA_VLADIVOSTOK'
        tz_asia_yakutsk = 'TZ_ASIA_YAKUTSK'
        tz_asia_yekaterinburg = 'TZ_ASIA_YEKATERINBURG'
        tz_atlantic_azores = 'TZ_ATLANTIC_AZORES'
        tz_atlantic_canary = 'TZ_ATLANTIC_CANARY'
        tz_atlantic_reykjavik = 'TZ_ATLANTIC_REYKJAVIK'
        tz_australia_broken_hill = 'TZ_AUSTRALIA_BROKEN_HILL'
        tz_australia_melbourne = 'TZ_AUSTRALIA_MELBOURNE'
        tz_australia_perth = 'TZ_AUSTRALIA_PERTH'
        tz_australia_sydney = 'TZ_AUSTRALIA_SYDNEY'
        tz_europe_amsterdam = 'TZ_EUROPE_AMSTERDAM'
        tz_europe_athens = 'TZ_EUROPE_ATHENS'
        tz_europe_belgrade = 'TZ_EUROPE_BELGRADE'
        tz_europe_berlin = 'TZ_EUROPE_BERLIN'
        tz_europe_bratislava = 'TZ_EUROPE_BRATISLAVA'
        tz_europe_brussels = 'TZ_EUROPE_BRUSSELS'
        tz_europe_bucharest = 'TZ_EUROPE_BUCHAREST'
        tz_europe_budapest = 'TZ_EUROPE_BUDAPEST'
        tz_europe_copenhagen = 'TZ_EUROPE_COPENHAGEN'
        tz_europe_dublin = 'TZ_EUROPE_DUBLIN'
        tz_europe_helsinki = 'TZ_EUROPE_HELSINKI'
        tz_europe_istanbul = 'TZ_EUROPE_ISTANBUL'
        tz_europe_kaliningrad = 'TZ_EUROPE_KALININGRAD'
        tz_europe_kiev = 'TZ_EUROPE_KIEV'
        tz_europe_lisbon = 'TZ_EUROPE_LISBON'
        tz_europe_ljubljana = 'TZ_EUROPE_LJUBLJANA'
        tz_europe_london = 'TZ_EUROPE_LONDON'
        tz_europe_luxembourg = 'TZ_EUROPE_LUXEMBOURG'
        tz_europe_madrid = 'TZ_EUROPE_MADRID'
        tz_europe_malta = 'TZ_EUROPE_MALTA'
        tz_europe_moscow = 'TZ_EUROPE_MOSCOW'
        tz_europe_oslo = 'TZ_EUROPE_OSLO'
        tz_europe_paris = 'TZ_EUROPE_PARIS'
        tz_europe_prague = 'TZ_EUROPE_PRAGUE'
        tz_europe_riga = 'TZ_EUROPE_RIGA'
        tz_europe_rome = 'TZ_EUROPE_ROME'
        tz_europe_samara = 'TZ_EUROPE_SAMARA'
        tz_europe_sarajevo = 'TZ_EUROPE_SARAJEVO'
        tz_europe_skopje = 'TZ_EUROPE_SKOPJE'
        tz_europe_sofia = 'TZ_EUROPE_SOFIA'
        tz_europe_stockholm = 'TZ_EUROPE_STOCKHOLM'
        tz_europe_tallinn = 'TZ_EUROPE_TALLINN'
        tz_europe_vienna = 'TZ_EUROPE_VIENNA'
        tz_europe_vilnius = 'TZ_EUROPE_VILNIUS'
        tz_europe_warsaw = 'TZ_EUROPE_WARSAW'
        tz_europe_zagreb = 'TZ_EUROPE_ZAGREB'
        tz_europe_zurich = 'TZ_EUROPE_ZURICH'
        tz_indian_maldives = 'TZ_INDIAN_MALDIVES'
        tz_indian_mauritius = 'TZ_INDIAN_MAURITIUS'
        tz_num_timezones = 'TZ_NUM_TIMEZONES'
        tz_pacific_auckland = 'TZ_PACIFIC_AUCKLAND'
        tz_pacific_easter = 'TZ_PACIFIC_EASTER'
        tz_pacific_galapagos = 'TZ_PACIFIC_GALAPAGOS'
        tz_pacific_honolulu = 'TZ_PACIFIC_HONOLULU'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'upload_event'

    # @deprecated api_create is being deprecated
    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.adobjects.business import Business
        return Business(api=self._api, fbid=parent_id).create_upload_event(fields, params, batch, success, failure, pending)

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MeasurementUploadEvent,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'aggregation_level': 'aggregation_level_enum',
            'conversion_end_date': 'string',
            'conversion_start_date': 'string',
            'event_status': 'event_status_enum',
            'lookback_window': 'lookback_window_enum',
            'match_universe': 'match_universe_enum',
            'partner': 'string',
            'timezone': 'timezone_enum',
            'upload_tag': 'string',
        }
        enums = {
            'aggregation_level_enum': MeasurementUploadEvent.AggregationLevel.__dict__.values(),
            'event_status_enum': MeasurementUploadEvent.EventStatus.__dict__.values(),
            'lookback_window_enum': MeasurementUploadEvent.LookbackWindow.__dict__.values(),
            'match_universe_enum': MeasurementUploadEvent.MatchUniverse.__dict__.values(),
            'timezone_enum': MeasurementUploadEvent.Timezone.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MeasurementUploadEvent,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'aggregation_level': 'string',
        'conversion_end_date': 'string',
        'conversion_start_date': 'string',
        'event_status': 'string',
        'id': 'string',
        'lookback_window': 'string',
        'match_universe': 'string',
        'partner': 'Business',
        'timezone': 'string',
        'upload_tag': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AggregationLevel'] = MeasurementUploadEvent.AggregationLevel.__dict__.values()
        field_enum_info['EventStatus'] = MeasurementUploadEvent.EventStatus.__dict__.values()
        field_enum_info['LookbackWindow'] = MeasurementUploadEvent.LookbackWindow.__dict__.values()
        field_enum_info['MatchUniverse'] = MeasurementUploadEvent.MatchUniverse.__dict__.values()
        field_enum_info['Timezone'] = MeasurementUploadEvent.Timezone.__dict__.values()
        return field_enum_info


