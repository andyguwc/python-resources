# https://github.com/gtalarico/airtable-python-wrapper/blob/master/airtable/airtable.py
import sys
import requests 
from collections import OrderedDict
import posixpath 
import time 
import json 
from six.moves.urllib.parse import unquote, quote

from .auth import AirtableAuth
from .params import AirtableParams

try:
    IS_IPY = sys.implementation.name == "ironpython"
except AttributeError:
    IS_IPY = False


class Airtable:
    VERSION = "v0"
    API_BASE_URL = "https://api.airtable.com/"
    API_LIMIT = 1.0 / 5  # 5 per second
    API_URL = posixpath.join(API_BASE_URL, VERSION)

    def __init__(self, base_key, table_name, api_key=None):
        session = requests.Session()
        session.auth = AirtableAuth(api_key=api_key)
        self.session = session 
        self.table_name = table_name
        url_safe_table_name = quote(table_name, safe="")
        self.url_table = posixpath.join(self.API_URL, base_key, url_safe_table_name)
    
    def _process_params(self, params):
        """
        Process params names or values as needed using filters
        """
        new_params = OrderedDict()
        for param_name, param_value in sorted(params.items()):
            param_value = params[param_name]
            ParamClass = AirtableParams._get(param_name)
            new_params.update(ParamClass(param_value).to_param_dict())
        return new_params

    # this is a typical way of process responses 
    # do the response.raise_for_status() and if attempt to get error message from response
    def _process_response(self, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            err_msg = str(exc)

            try:
                error_dict = response.json()
            # attempt to get error message from response
            except json.decoder.JSONDecodeError:
                pass 
            else: 
                if "error" in error_dict:
                    err_msg += " [Error: {}]".format(error_dict["error"])
            raise requests.exceptions.HTTPError(err_msg)
        else:
            return response.json()
    
    def record_url(self, record_id):
        return posixpath.join(self.url_table, record_id)

    def _request(self, method, url, params=None, json_data=None):
        response = self.session.request(method, url, params=params, json=json_data)
        return self._process_response(response)
    
    def _get(self, url, **params):
        processed_params = self._process_params(params)
        return self._request("get", url, params=processed_params)
    
    def _post(self, url, json_data):
        return self._request("post", url, json_data=json_data)

    def _put(self, url, json_data):
        return self._request("put", url, json_data=json_data)

    def _patch(self, url, json_data):
        return self._request("patch", url, json_data=json_data)

    def _delete(self, url):
        return self._request("delete", url)

    # iterating get records 
    def get(self, record_id):
        """retrieves a record by id
        """
    
    def get_iter(self, **options):
        """record restriver iterator 
        Returns iterator with lists in batches
        """
        offset=None
        while True:
            data = self._get(self.url_table, offset=offset, **options)
            records = data.get('records', [])
            time.sleep(self.API_LIMIT)
            yield records 
            offset = data.get("offset")
            if not offset:
                break 
    
    def get_all(self, **options):
        all_records = []
        for records in self.get_iter(**options):
            all_records.extend(records)
        return all_records 

    
