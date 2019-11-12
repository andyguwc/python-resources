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

##################################################
# Requests
##################################################
# Example Request
import requests 

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
'name1' : 'value1',
'name2' : 'value2'
}

# Extra headers
headers = {
'User-agent' : 'none/ofyourbusiness',
'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# Decoded text returned by the request
text = resp.text

# A notable feature of requests is how it returns the resulting response content from a
# request. As shown, the resp.text attribute gives you the Unicode decoded text of a request. However, if you access resp.content, you get the raw binary content instead.
# On the other hand, if you access resp.json, then you get the response content interpreted as JSON.

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
upload content
'''
import requests
url = 'http://httpbin.org/post'
files = { 'file': ('data.csv', open('data.csv', 'rb')) }
r = requests.post(url, files=files)



##################################################
# Event Driven I/O
##################################################
