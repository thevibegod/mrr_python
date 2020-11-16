import hmac
import hashlib
import time
import codecs
import requests

from mrr.exceptions import ApiCallException
from mrr.extras import Extras
from mrr.account import Account
from mrr.rig import Rig


class API:
    """ This class handles the work to talk to MRR's api
    """
    __api_key = ''
    __api_secret = ''
    __nonce_v = ''
    __root_url = 'https://www.miningrigrentals.com/api/v2'
    extras = None
    account = None
    rigs = None

    # Init class
    def __init__(self, api_key, api_secret):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.extras = Extras(self)
        self.account = Account(self)
        self.rigs = Rig(self)

    # get timestamp as nonce
    def __nonce(self):
        self.__nonce_v = '{:.10f}'.format(time.time() * 1000).split('.')[0]

    # generate signature
    def __signature(self, endpoint):
        self.__nonce()
        string = self.__api_key + self.__nonce_v + endpoint
        signature = hmac.new(codecs.encode(self.__api_secret), codecs.encode(string),
                             digestmod=hashlib.sha1).hexdigest()  # create signature
        return signature

    def __return_data(self, response):
        if not response.get('success'):
            raise ApiCallException(response['data'].get('message'))
        return response.get("data")

    def get(self, url, params=None):
        sign = self.__signature(url)
        resp = requests.get(self.__root_url + url,
                            headers={'x-api-sign': sign, 'x-api-key': self.__api_key, 'x-api-nonce': self.__nonce_v},
                            params=params)
        return self.__return_data(resp.json())

    def post(self, url, data):
        sign = self.__signature(url)
        resp = requests.post(self.__root_url + url,
                             headers={'x-api-sign': sign, 'x-api-key': self.__api_key, 'x-api-nonce': self.__nonce_v},
                             json=data)
        return self.__return_data(resp.json())

    def put(self, url, data):
        sign = self.__signature(url)
        resp = requests.put(self.__root_url + url,
                            headers={'x-api-sign': sign, 'x-api-key': self.__api_key, 'x-api-nonce': self.__nonce_v},
                            json=data)
        return self.__return_data(resp.json())

    def delete(self, url):
        sign = self.__signature(url)
        resp = requests.delete(self.__root_url + url,
                               headers={'x-api-sign': sign, 'x-api-key': self.__api_key, 'x-api-nonce': self.__nonce_v})
        return self.__return_data(resp.json())
