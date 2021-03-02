##################################################
# Urllib
##################################################

'''
Urllib basics
'''
# https://pymotw.com/3/urllib.parse/index.html

# return value form urlparse() is a ParseResult object that acts like a tuple

from urllib.parse import urlparse

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print(parsed)
# ParseResult(scheme='http', netloc='netloc', path='/path',params='param', query='query=arg', fragment='frag')
# based on namedtuple, so can extract attributes

print(parsed.path)


'''
joining
'''
from urllib.parse import urljoin

print(urljoin('http://www.example.com/path/file.html',
              'anotherfile.html'))


'''
encode
'''
from urllib.parse import urlencode

query_args = {
    'q': 'query string',
    'foo': 'bar',
}
encoded_args = urlencode(query_args)
print('Encoded:', encoded_args)


'''
urllib.request
'''
from urllib import request

response = request.urlopen('http://localhost:8080/')
headers = response.info()
data = response.read().decode('utf-8')
print(data)


from urllib import request

response = request.urlopen('http://localhost:8080/')
for line in response:
    print(line.decode('utf-8').rstrip())


'''
encoding arguments
'''
from urllib import parse
from urllib import request

query_args = {'q': 'querying string', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args)

url = 'http://localhost:8080/?' + encoded_args
print(request.urlopen(url).read().decode('utf-8'))


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


