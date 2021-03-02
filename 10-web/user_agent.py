
##################################################
# User Agent
##################################################

# https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/

'''
user agent definition
'''
# To rotate user agents in Python here is what you need to do

# Collect a list of User-Agent strings of some recent real browsers.
# Put them in a Python List.
# Make each request pick a random string from this list and send the request with the ‘User-Agent’ header as this string.

# A user agent is a string that a browser or application sends to each website you visit. A typical user agent string contains details like – the application type, operating system, software vendor, or software version of the requesting software user agent. Web servers use this data to assess the capabilities of your computer, optimizing a page’s performance and display. User-Agents are sent as a request header called “User-Agent”.

# User-Agent: Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>

# Below is the User-Agent string for Chrome 83 on Mac Os 10.15

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36


'''
change user agent
'''
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

r = requests.get('http://httpbin.org/headers',headers=headers)
pprint(r.json())


# sending a full set of headers
# otherwise stopped by a anti scraping tools

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
    "Dnt": "1", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
  }

r = requests.get("http://httpbin.org/headers",headers=headers)
pprint(r.json())


'''
full script
'''

import requests
import random
from collections import OrderedDict

headers_list = [
    # Firefox 77 Mac
     {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
]

ordered_headers_list = []
for headers in headers_list:
    h = OrderedDict()
    for header, value in headers.items():
        h[header] = value
    ordered_headers_list.append(h)

url = 'https://httpbin.org/headers'
for i in range(1,4):
    headers = random.choice(headers_list)
    r = requests.Session()
    r.headers = headers

    response = r.get(url)
    print("Request #%d\nUser-Agent Sent:%s\n\nHeaders Recevied by HTTPBin:"%(i,headers['User-Agent']))
    print(response.json())
    print("-------------------")



