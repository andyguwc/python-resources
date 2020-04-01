from requests import Session
from streamlink.plugin.api import useragents


def _parse_keyvalue_list(val):
    for keyvalue in val.split(";"):
        try:
            key, value = keyvalue.split("=", 1)
            yield key.strip(), value.strip()
        except ValueError:
            continue 


class HTTPSession(Session):
    def __init__(self, *args, **kwargs):
        Session.__init__(self, *args, **kwargs)

        if self.headers['User-Agent'].startswith('python-requests'):
            self.headers['User-Agent'] = useragents.FIREFOX 
        
        self.timeout = 20.0 

    @classmethod 
    def determine_json_encoding(cls, sample):
        nulls_at = [i for i, j in enumerate(bytearray(sample[:4])) if j == 0]
        if nulls_at == [0, 1, 2]:
            return "UTF-32BE"
        elif nulls_at == [0, 2]:
            return "UTF-16BE"
        elif nulls_at == [1, 2, 3]:
            return "UTF-32LE"
        elif nulls_at == [1, 3]:
            return "UTF-16LE"
        else:
            return "UTF-8"

    # in order to do something like http.json ...
    # class method can be used both by class and by instance
    @classmethod 
    def json(cls, res, *args, **kwargs):
        """Parses JSON from a response"""
        if res.encoding is None:
            res.encoding = cls.determine_json_encoding(res.content[:4])
        return parse_json(res.text, *args, **kwargs)
    
    @classmethod 
    def xml(cls, res, *args, **kwargs):
        return parse_xml(res.text, *args, **kwargs)
    
    def parse_cookies(self, cookies, **kwargs):
        for name, value in _parse_keyvalue_list(cookies):
            self.cookies.set(name, value, **kwargs)
    
    def parse_headers(self, headers):
        """Parses a semi-colon delimited list of headers.

        Example: foo=bar;baz=qux
        """
        for name, value in _parse_keyvalue_list(headers):
            self.headers[name] = value

    def parse_query_params(self, cookies, **kwargs):
        """Parses a semi-colon delimited list of query parameters.

        Example: foo=bar;baz=qux
        """
        for name, value in _parse_keyvalue_list(cookies):
            self.params[name] = value

    def resolve_url(self, url):
        """Resolves any redirects and returns the final URL."""
        return self.get(url, stream=True).url    

    def request(self, mthod, url, *args, **kwargs):
        headers = kwargs.pop("headers", {})
        exception = kwargs.pop("exception", PluginError)
        params = kwargs.pop("params", {})
        raise_for_status = kwargs.pop("raise_for_status", True)


        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = Session.request(self, method, url, 
                                      headers=headers,
                                      params=params,
                                      timeout=timeout,
                                      proxies=proxies,
                                      *args, **kwargs)
                if raise_for_status and res.status_cide not in acceptable_status:
                    res.raise_for_status()
                break 
            except KeyboardInterrupt:
                raise 
            except Exception as err: 
                if retries >= total_retries:
                    err = exception("Unable to open URL: {url} ({err})".format(url=url,
                                                                               err=rerr))
                    err.err = rerr
                    raise err
                retries +=1
                delay = min(retry_max_backoff,
                            retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)
        
        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res 