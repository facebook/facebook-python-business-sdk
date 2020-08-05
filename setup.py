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

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

this_dir = os.path.dirname(__file__)
readme_filename = os.path.join(this_dir, 'README.md')
requirements_filename = os.path.join(this_dir, 'requirements.txt')

PACKAGE_NAME = 'facebook_business'
PACKAGE_VERSION = '8.0.0'
PACKAGE_AUTHOR = 'Facebook'
PACKAGE_AUTHOR_EMAIL = ''
PACKAGE_URL = 'https://github.com/facebook/facebook-python-business-sdk'
PACKAGE_DOWNLOAD_URL = \
    'https://github.com/facebook/facebook-python-business-sdk/tarball/' + PACKAGE_VERSION
PACKAGES = [
    'facebook_business',
    'facebook_business.test',
    'facebook_business.utils',
    'facebook_business.adobjects',
    'facebook_business.adobjects.helpers',
    'facebook_business.adobjects.serverside',
]
PACKAGE_DATA = {
    'facebook_business': ['*.crt'],
    'facebook_business.test': ['*.jpg']
}
PACKAGE_LICENSE = 'LICENSE.txt'
PACKAGE_DESCRIPTION = 'Facebook Business SDK'

with open(readme_filename) as f:
    PACKAGE_LONG_DESCRIPTION = f.read()

with open(requirements_filename) as f:
    PACKAGE_INSTALL_REQUIRES = [line[:-1] for line in f]

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    author=PACKAGE_AUTHOR,
    author_email=PACKAGE_AUTHOR_EMAIL,
    url=PACKAGE_URL,
    download_url=PACKAGE_DOWNLOAD_URL,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    license=PACKAGE_LICENSE,
    description=PACKAGE_DESCRIPTION,
    long_description=PACKAGE_LONG_DESCRIPTION,
    install_requires=PACKAGE_INSTALL_REQUIRES,
    long_description_content_type="text/markdown",
)
