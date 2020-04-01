import logging 
import os 
import requests 
from requests.exceptions import HTTPError
import time 
from .common import (
    get_base_url,
    get_data_url,
    get_credentials,
    get_api_version,
)

from .entity import (
    Account, AccountConfigurations, AccountActivity,
    Asset, Order, Position, BarSet, Clock, Calendar,
)
from . import polygon

logger = logging.getLogger(__name__)

class RetryException(Exception):
    pass 

class APIError(Exception):
    """Represents API related error
    error.status_code will have status code 
    """
    def __init__(self, error, http_error=None):
        super().__init__(error['message'])
        self._error = error 
        self._http_error = http_error

    @property 
    def code(self):
        return self._error['code']
    
    @property 
    def status_code(self):
        http_error = self._http_error
        if http_error is not None and hasattr(http_error, 'response'):
            return http_error.response.status_code
    
    @property 
    def request(self):
        if self._http_error is not None:
            return self._http_error.request 
    
    @property 
    def response(self):
        if self._http_error is not None:
            return self._http_error.response 
    

class REST(object):
    def __init__(
        self,
        key_id = None,
        secret_key = None,
        base_url = None,
        api_version = None,
        oauth = None
    ):
        # move the get credentials to the common (utils) which lookup env variables
        self._key_id, self._secret_key, self._oauth = get_credentials(
            key_id, secret_key, oauth)
        # use the input first if not fall back to default
        self._base_url = base_url or get_base_url()
        self._api_version = get_api_version(api_version)
        self._session = requests.Session()
        self._retry = int(os.environ.get('APCA_RETRY_MAX', 3))
        self._retry_wait = int(os.environ.get('APCA_RETRY_WAIT', 3))
        self._retry_codes = [int(o)for o in os.environ.get(
            'APCA_RETRY_CODES', '429,504').split(',')]
        self.polygon = polygon.REST(
            self._key_id, 'staging' in self._base_url)
    
    def _request(
        self, 
        method,
        path, 
        data=None,
        base_url=None,
        api_version=None 
    ):

        base_url = base_url or self._base_url
        version = api_version if api_version else self._api_version
        url = base_url + '/' + version + path
        # initialize headers
        headers = {}
        if self._oauth:
            headers['Authorization'] = 'Bearer '+self.oauth 
        else:
            headers['APCA-API-KEY-ID'] = self._key_id
            headers['APCA-API-SECRET-KEY'] = self._secret_key
        opts = {
            'headers': headers
            'allow_redirects': False
        }

        # passing in the data
        # can be params string or body depends on if the request is GET or not 
        # note that requests library supports to send both data={'key':'value'} or json={'key':'value'} (the library serializes it)

        if method.upper() == 'GET':
            opts['params'] = data  
        
        else:
            opts['json'] = data 
        
        # retry functionality
        # basically do a loop and call _one_request every time 
        retry = self._retry
        if retry < 0:
            retry = 0
        while retry >= 0:
            try: 
                # the one_request will raise RetryException in the case of response status code 429
                return self._one_request(method, url, opts, retry)
            except RetryException:
                retry_wait = self._retry_wait
                logger.warning(
                    'sleep {} seconds and retrying {} '
                    '{} more time(s)...'.format(
                        retry_wait, url, retry))
                time.sleep(retry_wait)
                retry -= 1
                continue 

    # request just needs the url, method, and the headers, etc. are in the opts kwargs
    def _one_request(self, method, url, opts, retry):
        """
        Perform one request, possibly raising RetryException in the case
        the response is 429. Otherwise, if error text contain "code" string,
        then it decodes to json object and returns APIError.
        Returns the body json in the 200 status.
        """
        retry_codes = self._retry_codes
        resp = self._session.request(method, url, **opts)
        try:
            resp.raise_for_status()
        except HTTPError as http_error:
            # retry if hit limit 
            if resp.status_code in retry_codes and retry >0:
                raise RetryException()
            if 'code' in resp.text:
                error = resp.json()
                if 'code' in error:
                    raise APIError(error, http_error)
            else:
                raise 
        if resp.text != '':
            return resp.json() # returns a dictionary 
        return None 
    
    # now define other methods to wrap around the self._request
    def get(self, path, data=None):
        return self._request('GET', path, data)
    
    def post(self, path, data=None):
        return self._request('POST', path, data)
    
    def patch(self, path, data=None):
        return self._request('PATCH', path, data)

    def delete(self, path, data=None):
        return self._request('DELETE', path, data)
    
    def list_orders(self, status=None, limit=None, after=None, until=None,
                    direction=None, params=None):
        """
        Get a list of orders 
        """
        if params is None:
            params = dict()
        if limit is not None:
            params['limit'] = limit 
        if after is not None:
            params['after'] = after 
        if until is not None:
            params['until'] = until
        if direction is not None:
            params['direction'] = direction
        if status is not None:
            params['status'] = status
        resp = self.get('/orders', params)
        return [Order(o) for o in resp]
    
    def submit_order(self, symbol, qty, side, type, time_in_force,
                     limit_price=None, stop_price=None, client_order_id=None,
                     extended_hours=None):
        '''Request a new order'''
        params = {
            'symbol': symbol,
            'qty': qty,
            'side': side,
            'type': type,
            'time_in_force': time_in_force,
        }
        if limit_price is not None:
            params['limit_price'] = limit_price
        if stop_price is not None:
            params['stop_price'] = stop_price
        if client_order_id is not None:
            params['client_order_id'] = client_order_id
        if extended_hours is not None:
            params['extended_hours'] = extended_hours
        resp = self.post('/orders', params)
        return Order(resp)
    
    