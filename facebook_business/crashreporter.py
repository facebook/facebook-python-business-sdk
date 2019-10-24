import sys
from facebook_business.api import FacebookRequest
from facebook_business.session import FacebookSession
from facebook_business.api import FacebookAdsApi

class CrashReporter(object):

    reporter_instance = None

    def __init__(self, app_id, excepthook):
        self.__app_id = app_id
        self.__excepthook = excepthook

    @classmethod
    def enable(cls):
        if cls.reporter_instance == None:
            api = FacebookAdsApi.get_default_api()
            cls.reporter_instance = cls(api._session.app_id, sys.excepthook)
            sys.excepthook = cls.reporter_instance.__exception_handler
            print('CrashReporter: Enabled\n')

    @classmethod
    def disable(cls):
        if cls.reporter_instance != None:
            # Restore the original excepthook
            sys.excepthook = cls.reporter_instance.__excepthook
            cls.reporter_instance = None
            print('CrashReporter: Disabled')

    def __exception_handler(self, etype, evalue, tb):
        if etype:
            print('CrashReporter: Crashes detected!')
            # TODO :check if it is cause by SDK and send API request
        else:
            print('CrashReporter: No crashes detected.')

        self.__forward_exception(etype, evalue, tb)

    def __forward_exception(self, etype, evalue, tb):
        self.__excepthook(etype, evalue, tb)
