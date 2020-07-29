# coding=utf-8
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

import pycountry
import re

# defined regex for normalization of data
location_excluded_chars = re.compile(r"[0-9.\s\-()]")
isocode_included_chars = re.compile(r"[^a-z]")
email_pattern = re.compile("(^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+$)")
md5_pattern = re.compile(r"^[a-f0-9]{32}$");
sha256_pattern = re.compile(r"^[a-f0-9]{64}$");

class Normalize(object):


    @staticmethod
    def normalize_field(field, data):
        """Computes the normalized value for the given field type and data.

        :param field: The field name that is being normalized.
        :param data: The data that is being normalized.
        :return: Normalized value.
        :rtype: str
        """
        if field is None:
            raise TypeError('Field Type must be passed for Normalization')
        if data is None or len(data) == 0:
            return None

        normalized_data = data.lower().strip()
        if Normalize.is_already_hashed(normalized_data):
            return normalized_data

        if field == "em":
            normalized_data = Normalize.validate_email(normalized_data)

        elif field == "ct":
            # Remove numbers, space and period character
            normalized_data = location_excluded_chars.sub("", normalized_data)

        elif field == "zp":
            normalized_data = re.sub(r"\s","", normalized_data)
            normalized_data = normalized_data.split("-")[0]

        elif field == "st":
            # Remove numbers, space and period character
            normalized_data = location_excluded_chars.sub("", normalized_data)

        elif field == "country":
            # Remove any non-alpha characters from the data
            normalized_data = isocode_included_chars.sub("", normalized_data)
            if not Normalize.is_valid_country_code(normalized_data):
                raise TypeError("Invalid format for country:'" + data + "'.Please follow ISO 2-letter ISO 3166-1 standard for representing country. eg: us")

        elif field == "currency":
             # Remove any non-alpha characters from the data
            normalized_data = isocode_included_chars.sub("", normalized_data)
            if len(normalized_data) != 3:
                raise TypeError("Invalid format for currency:'" + data + "'.Please follow ISO 3-letter ISO 4217 standard for representing currency. Eg: usd")

        elif field == "ph":
            # Remove spaces and parenthesis within phone number
            normalized_data = re.sub(r"[\s\-()]", "", normalized_data)

            # Removes the starting + and leading two 0's
            normalized_data = re.sub(r"^\+?0{0,2}", "", normalized_data)

            international_number = Normalize.is_international_number(normalized_data)

            if international_number is not None:
                return international_number

        return normalized_data

    """
    Validates the email field for RFC 5322
    :param token: The email token that is being validates.
    :return: validated email value.
    :rtype: str
    """
    @staticmethod
    def validate_email(email):
        result = email_pattern.match(email)
        if result is None:
            raise TypeError('Invalid email format for the passed email:' + email + '.Please check the passed email format.')
        return email

    """
    Checks if the given data is already hashed by MD5 or SHA256 Hash
    :param data: The token that is being checked for hashed.
    :return: boolean representing the {md5/sha256} hash state of the token.
    :rtype: bool
    """
    @staticmethod
    def is_already_hashed(data):
        md5_match = md5_pattern.match(data)
        sha256_match = sha256_pattern.match(data)
        if md5_match is None and sha256_match is None:
            return False
        return True

    @staticmethod
    def is_international_number(phone_number):

        # Removes the + and leading two 0's
        phone_number = re.sub(r"^\+?0{0,2}", "", phone_number);

        if phone_number.startswith('0'):
            return None

        # International Phone number with country calling code.
        international_number_regex = re.compile(r'^\d{1,4}\(?\d{2,3}\)?\d{4,}$')

        return international_number_regex.match(phone_number).group()

    """
    Checks if the given country code is present in the ISO list
    :param country code: The code that is being checked for presence.
    :return: boolean indicating whether country code is valid.
    :rtype: bool
    """
    @staticmethod
    def is_valid_country_code(country_code):
        country_data = pycountry.countries.get(alpha_2=country_code.upper())
        return country_data is not None
