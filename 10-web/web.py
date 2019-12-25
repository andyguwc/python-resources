
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



'''
sample hook wrapper 
'''


'''
retry 
'''


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



##################################################
# Working with JSON Data 
##################################################

'''
working with JSON Data
'''





##################################################
# Urllib
##################################################

'''
GET Request
'''
from urllib import request, parse 

# Base URL being accessed 
url = 'http://httpbin.org/get'

# dictionary of query params 
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# make a GET request and read the response 
u = request.urlopen(url+'?'+querystring)
resp = u.read()


'''
POST Request
'''
# encode the query parameters and supply as an optional argument to urlopen()

from urllib import request, parse
# Base URL being accessed
url = 'http://httpbin.org/post'
# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}
# Encode the query string
querystring = parse.urlencode(parms)
# Make a POST request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()

'''
HEADER
'''
# If you need to supply some custom HTTP headers in the outgoing request such as a
# change to the user-agent field, make a dictionary containing their value and create a Request instance and pass it to urlopen() like this
from urllib import request, parse 

# Extra Headers 
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)

# make a request and read the response 
u = request.urlopen(req)
resp = u.read()
