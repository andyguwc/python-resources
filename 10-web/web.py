

##################################################
# Web Frameworks 
##################################################

# Broadly speaking, a web framework consists of a set of libraries and a main handler
# within which you can build custom code to implement a web application (i.e., an
# interactive website providing a client interface to code running on a server). Most
# web frameworks include patterns and utilities to accomplish at least the following:

# URL routing
# - Match an incoming HTTP request to a particular Python function (or callable).

# Handling Request and Response objects
# - Encapsulate the information received from or sent to a user’s browser.

# Templating
# - Inject Python variables into HTML templates or other output, allowing programmers
# to separate an application’s logic (in Python) from the layout (in the template).

# Development web service for debugging
# - Run a miniature HTTP server on development machines to enable rapid development;
# often automatically reloading server-side code when files are updated.

'''
Django vs. Flask
'''
# Django is a “batteries included” web application framework and is an excellent choice
# for creating content-oriented websites. By providing many utilities and patterns out
# of the box, Django aims to make it possible to build complex, database-backed web
# applications quickly while encouraging best practices in code that uses it.

# Flask is a microframework for Python, and is an excellent choice for building smaller
# applications, APIs, and web services. Rather than aiming to provide everything you
# could possibly need, Flask implements the most commonly used core components of
# a web application framework, like URL routing, HTTP request and response objects,
# and templates.

# If you use Flask, it is up to you to choose other components for your application, if
# any. For example, database access or form generation/validation are not built into
# Flask. This is great, because many web applications don’t need those features. If yours
# do, there are many available extensions, such as SQLAlchemy for a database, or
# pyMongo for MongoDB and WTForms for forms

# https://flask.palletsprojects.com/en/1.1.x/tutorial/



##################################################
# Requests
##################################################

# https://realpython.com/python-requests/
# https://requests.readthedocs.io/en/master/user/advanced/#request-and-response-objects

'''
example request
'''

# Example Request
import requests 

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
params = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=params, headers=headers)
# A notable feature of requests is how it returns the resulting response content from a
# request. As shown, the resp.text attribute gives you the Unicode decoded text of a request. However, if you access resp.content, you get the raw binary content instead.
# On the other hand, if you access resp.json, then you get the response content interpreted as JSON.

'''
query string and message body 
'''
# query string 
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
# the URL has been correctly encoded 
# >>> print(r.url) 
# https://httpbin.org/get?key2=value2&key1=value1

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# can also pass in a list of items as value
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
# >>> print(r.url)
# https://httpbin.org/get?key1=value1&key2=value2&key2=value3

# request headers 
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)


'''
post and put methods 
'''
# post, put and patch pass their data through the message body rather than query string
# pass in the payload in the data parameter
# data takes a dict, a list of tuples, bytes, or file-like object 
requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})


# sometimes API accepts JSON-encoded POST data
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))


# uploading content
import requests
url = 'http://httpbin.org/post'
files = { 'file': ('data.csv', open('data.csv', 'rb')) }
r = requests.post(url, files=files)

# set content_type and headers explicitly
url = 'https://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
requests.post(url, files=files)


'''
response parameters
'''

# status code 
if response.status_code == 200:
    print("success")
elif response.status_code == 404:
    print('Not found')

# content 
# the response in bytes
response.content 

# Decoded text returned by the request
response.text
# can provide an encoding before accessing text
response.encoding = 'utf-8'
response.text 

# to get a dictionary from the json 
response.json()
# better option than json.loads(response.text)

# returns a dictionary so you can access values in the object by key 

# response headers 
# gives you the content type etc. 
response.headers['content-type']


'''
inspecting requests (prepared requests)
'''
# when making a request, the requests library prepares the request before sending it to the server
# like validating headers and serializing json content 

# >>> response = requests.post('https://httpbin.org/post', json={'key':'value'})
# >>> response.request.headers['Content-Type']
# 'application/json'
# >>> response.request.url
# 'https://httpbin.org/post'
# >>> response.request.body
# b'{"key": "value"}'

# if you want to do extra processing before sending a request, do below 

from requests import Request, Session 

s= Session()
req = Request('GET', url, data=data, headers=headers)
prepped = s.prepare_request(req)
# or use prepped = req.prepare() 
# do something with prepped.body 
prepped.body = 'change something'
# do something with prepped.headers 
prepped.headers['new-header'] = 'new-value'
resp = s.send(prepped, 
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)



'''
session
'''
# If you need to fine-tune your control over how requests are being made or improve the performance of your requests, you may need to use a Session instance directly.
# Sessions are used to persist parameters across requests. For example, if you want to use the same authentication across multiple requests, you could use a session:

import requests
from getpass import getpass

# By using a context manager, you can ensure the resources used by
# the session will be released after use
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('example_url')

# You can inspect the response just like you did before
print(response.headers)
print(response.json())


# session has all the methods of the main Requests API
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')


# session can also be used to provide default data to the request methods 
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'}) 
# both the x-test previously and the x-test-2 headers are set 
# The method-level parameters override session parameters.
s.get('http://example.org', headers={'x-test-2': 'value'})


headers = {'x-test': 'true'}
auth = ('user', 'pass')


with requests.session(auth=auth, headers=headers) as c:

    # both 'x-test' and 'x-test2' are sent
    c.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# Any dictionaries that you pass to a request method will be merged with the session-level values that are set. The method-level parameters override session parameters.



'''
sample hook wrapper 
'''


'''
retry 
'''

# practical example 
# define a retry exception which request function will raise if certain status_codes are met 
# the request with retry will retry multiple times, each time calling the request if retry exception is raised
class RetryException(Exception):
    pass


class ExampleAPIWrapper():
    # ...
    def __init__(self):
        pass 
    
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
        headers = {}
        if self._oauth:
            headers['Authorization'] = 'Bearer ' + self._oauth
        else:
            headers['APCA-API-KEY-ID'] = self._key_id
            headers['APCA-API-SECRET-KEY'] = self._secret_key
        opts = {
            'headers': headers,
            # Since we allow users to set endpoint URL via env var,
            # human error to put non-SSL endpoint could exploit
            # uncanny issues in non-GET request redirecting http->https.
            # It's better to fail early if the URL isn't right.
            'allow_redirects': False,
        }
        if method.upper() == 'GET':
            opts['params'] = data
        else:
            opts['json'] = data

        retry = self._retry
        if retry < 0:
            retry = 0
        while retry >= 0:
            try:
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

    def _one_request(self, method, url, opts, retry):
        '''
        Perform one request, possibly raising RetryException in the case
        the response is 429. Otherwise, if error text contain "code" string,
        then it decodes to json object and returns APIError.
        Returns the body json in the 200 status.
        '''
        retry_codes = self._retry_codes
        resp = self._session.request(method, url, **opts)
        try:
            resp.raise_for_status()
        except HTTPError as http_error:
            # retry if we hit Rate Limit
            if resp.status_code in retry_codes and retry > 0:
                raise RetryException()
            if 'code' in resp.text:
                error = resp.json()
                if 'code' in error:
                    raise APIError(error, http_error)
            else:
                raise
        if resp.text != '':
            return resp.json()
        return None


'''
error handling
'''
# using raise_for_status()
# so we don't need to check status code each time in an if statement 

import requests 
from requests.exceptions import HTTPError

try: 
    response = requests.get(url)
    response.raise_for_status()

except HTTPError as http_err:
    print('http error occurred {}'.format(http_err))

except Exception as err:
    print('other error occurred {}'.format(err))

else:
    print('Success')


'''
authentication
'''

import requests
resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user','password'))

'''
cookies
'''

# Pass HTTP cookies from one request to the next
import requests

# First request
resp1 = requests.get(url)

# Second request with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)


'''
stream
'''

# By default, when you make a request, the body of the response is downloaded immediately. 
# You can override this behaviour and defer downloading the response body until you access the Response.content attribute with the stream parameter:

tarball_url = 'https://github.com/psf/requests/tarball/master'
r = requests.get(tarball_url, stream=True)

# At this point only the response headers have been downloaded and the connection remains open, hence allowing us to make content retrieval conditional:
if int(r.headers['content-length']) < TOO_LONG:
  content = r.content
  ...
# You can further control the workflow by use of the Response.iter_content() and Response.iter_lines() methods
# iter_lines()
import json
import requests

r = requests.get('https://httpbin.org/stream/20', stream=True)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines():
    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line))

# iter_content()

with open(filename, 'wb') as fd: 
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)


# stream uploads 

with open('massive-body', 'rb') as f: 
    requests.post('http://some.url/streamed', data=f)



'''
Custom Authentication
'''
# Requests allows you to use specify your own authentication mechanism.
# Any callable which is passed as the auth argument to a request method will have the opportunity to modify the request before it is dispatched.
# Authentication implementations are subclasses of requests.auth.AuthBase, and are easy to define. Requests provides two common authentication scheme implementations in requests.auth: HTTPBasicAuth and HTTPDigestAuth.
# Let’s pretend that we have a web service that will only respond if the X-Pizza header is set to a password value. Unlikely, but just go with it.

from requests.auth import AuthBase

class PizzaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r
# Then, we can make a request using our Pizza Auth:

# >>> requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
# <Response [200]>

# Practical Example https://github.com/gtalarico/airtable-python-wrapper/blob/e85e61b5872a9d8adcf1f1f6348eb1381fa448cc/airtable/auth.py#L25
class AirtableAuth(requests.auth.AuthBase):
    def __init__(self, api_key=None):
        """
        Authentication used by Airtable Class
        Args:
            api_key (``str``): Airtable API Key. Optional.
                If not set, it will look for
                enviroment variable ``AIRTABLE_API_KEY``
        """
        try:
            self.api_key = api_key or os.environ["AIRTABLE_API_KEY"]
        except KeyError:
            raise KeyError(
                "Api Key not found. Pass api_key as a kwarg \
                            or set an env var AIRTABLE_API_KEY with your key"
            )

    def __call__(self, request):
        auth_token = {"Authorization": "Bearer {}".format(self.api_key)}
        request.headers.update(auth_token)
        return request




##################################################
# Web Servers
##################################################

# Nginx
# Nginx (pronounced “engine-x”) is a web server and reverse proxy11 for HTTP,
# SMTP, and other protocols. It is known for its high performance, relative simplicity,
# and compatibility with many application servers (like WSGI servers). It also
# includes handy features like load balancing,12 basic authentication, streaming,
# and others. Designed to serve high-load websites, Nginx is gradually becoming
# quite popular.

# WSGI servers
# Gunicorn (Green Unicorn)
# Gunicorn is the recommended choice for new Python web applications—a pure-
# Python WSGI server used to serve Python applications. Unlike other Python web
# servers, it has a thoughtful user interface and is extremely easy to use and configure.
# Gunicorn has sane and reasonable defaults for configurations. However,
# some other servers, like uWSGI, are tremendously more customizable (but therefore
# are much more difficult to effectively use).

