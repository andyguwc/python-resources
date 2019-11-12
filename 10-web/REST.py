##################################################
# REST
##################################################

'''
REST & CRUD
'''

# A REST server will often support CRUD operations via the following
# five essential use cases:

# • Create: We'll use an HTTP POST request to create a new object and a URI
# that provides class information only. A path such as //host/app/blog/
# might name the class. The response could be a 201 message that includes a
# copy of the object as it was finally saved. The returned object information
# may include the URI assigned by the RESTful server for the newly created
# object or the relevant keys to construct the URI. A POST request is expected to
# change the RESTful resources by creating something new.

# • Retrieve – Search: This is a request that can retrieve multiple objects. We'll
# use an HTTP GET request and a URI that provides search criteria, usually in
# the form of a query string after the ? character. The URI might be //host/
# app/blog/?title="Travel 2012-2013". Note that GET never makes a
# change to the state of any RESTful resources.

# • Retrieve – Instance: This is a request for a single object. We'll use an HTTP
# GET request and a URI that names a specific object in the URI path. The URI
# might be //host/app/blog/id/. While the response is expected to be a
# single object, it might still be wrapped in a list to make it compatible with a
# search response. As this response is GET, there's no change in the state.

# • Update: We'll use an HTTP PUT request and a URI that identifies the object
# to be replaced. The URI might be //host/app/blog/id/. The response
# could be a 200 message that includes a copy of the revised object. Clearly,
# this is expected to make a change to the RESTful resources. There are good
# reasons to use other status responses than 200. We'll stick to 200 for our
# examples here.

# • Delete: We'll use an HTTP DELETE request and a URI that looks like //host/
# app/blog/id/. The response could be a simple 204 NO CONTENT without
# providing any object details in the response.


# choosing a representation
# several places to provide the representation
# - We can use a part of a query string, https://host/app/class/id/?form=XML.
# - We can use a part of the URI: https://host/app;XML/class/id/. In this
# example, we've used a sub-delimiter for the application to identify the
# required representation. The app;XML syntax names the application, app, and
# the format, XML.
# - We can use the fragment identifier, https://host/app/class/id/#XML.
# - We can provide it in a header. The Accept header, for example, can be used
# to specify the representation.


'''
server
'''
# For robust, high-performance, secure operations, common practice is to build on a server
# such as Apache httpd or the nginx.

# One widely used interface between web servers and Python is the WSGI

# Each WSGI application must have this API: result = application(environ, start_response)
# The environ variable must be dict with environmental information. The start_
# response function must be used to start preparing a response to the client; this is
# how the response status code and headers are sent. The return value must be an
# iterable over strings; that is, the body of the response.


