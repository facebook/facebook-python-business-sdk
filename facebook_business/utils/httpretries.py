from __future__ import print_function, unicode_literals, absolute_import

__author__ = 'pasha-r'

from requests.packages.urllib3.util.retry import Retry


def retry_policy(total=None, connect=3, read=3, redirect=2):
    retries = Retry(total=total, connect=connect,
                    read=read, redirect=redirect)
    return retries
