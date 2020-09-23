################################################
# Error Checking and Exception Handling
################################################

'''
raise
'''
# exception error: syntatically correct python code results in an error
# use raise to throw an error when a certain condition occurs 
x = 10 
if x > 5: 
    raise Exception('x should to exeed 5. Value of x was: {}'.format(x))


def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin to delete')
    if not store.has_product(product_id):
        raise ValueError('Unknown product_id')

    stre.get_product(product_id).delete()


# class that only takes even numbers
class EvenOnly(list):
    def append(self, interger):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


'''
type of errors
'''

IndexError # unknown index for iteration type
KeyError # missing key in a mapping type
ValueError 
ZeroDivisionError

BaseException
    SystemExit
    KeyboardInterrupt
    Exception
        StopIteration
        AssertionError


# exception payloads
try:
    median([])
except ValueError as e:
    # print out the payload
    print('Payload', e.args)
    print(str(e))

# using the exception payload
try:
    result = divide(x, y)
except ValueError as e: 
    print('Payload', e.args)
    print(str(e)) # an alternative
else:
    print('Result is %.1f' % result)



'''
try except else finally 
'''
# try: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
# except: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
# else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
# finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. 

try:
    # run this code
    linux_interaction()
except AssertionError as error: 
    # execute this when there is an exception 
    print(str(error))
else:
    # no exceptions. run this
    print('Executing the else clause')
finally:
    # always run this code 
    print('Cleaning up, irrespective of any exceptions.')

try:
    f = open(filename, 'r')
except OSError:
    print("file could not be opened for read")
else:
    print("number of lines", sum(1 for line in f))
    f.close()


# accessing error mesages
try:
    # some code
except Exception as e:
    # some code
    print("Exception occured: {}".format(e))


# example handling 
try:
    choice = randome.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" %(e.__class__.__name__))

else: 
    print("this code is called if no exception")
finally:
    print("this cleanup code is always called")


def load_json_key(data, key):
    try:
        result_dict = json.loads(data) # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]


# raise ValueError so when other functions use it can write except statement
# better than the alternative of returning None
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e: 
        raise ValueError('Invalid Inputs') from e 

# using the ValueError returned above 
try:
    result = divide(x, y)
except ValueError: 
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)


# without using else
def login(self, username, password):
    try:
        user = self.users[username]
    except KeyError:
        raise InvalidUsername(username)

    if not user.check_password(password):
        raise InvalidPassword(username, user)

    user.is_logged_in = True
    return True


'''
continue
'''

# continue 
# always specify an exception type
while True:
    try:
        #
    except ValueError: 
        continue # this just ignores the error and continues

# standard exception hierarchy
# IndexError
# KeyError
# IndexError and KeyError are subclasses of LookupError


'''
multiple exceptions
'''

# If you can handle different exceptions all using a single block of code, they can be
# grouped together in a tuple like this

# example: remove_url() will be called if any of the listed exceptions occurs
try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)

# if need to handle other exceptions differently 
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)    


'''
custom exceptions
'''
# always define an exception
# just define new exceptions as classes which inherit from Exception 
# Generally, you’ll want to either derive your custom exceptions from the root Exception
# class or the other built-in Python exceptions like ValueError or
# TypeError—whicever feels appropriate.

class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class NameTooShortError(ValueError):
    pass 

# Now we have a “self-documenting” NameTooShortError exception
# type that extends the built-in ValueError class.
def validate(name):
    if len(name) < 10: 
        raise NameTooShortError(name)

# can define a base validation error so only need one catch 
# instead of lots of if else statements

class BaseValidationError(ValueError):
    pass 

class NameTooShortError(BaseValidationError):
    pass 

class NameTooLongError(BaseValidationError):
    pass 

try:
    validate(name)
except BaseValidationError as err: 
    handle_validate_err(err)


# Example

# note - make sure you call Exception.__init__() with all of the passed arguments
class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text) # message forwarded to base class for storage
        self._sides = tuple(sides)
    
    @property
    def sides(self):
        return self._sides
    
    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)
    
    def __repr__(self):
        return "TriangleError({!r},{!r}".format(self.args[0], self._sides)


def triangle_area(a,b,c):
    sides = sorted((a,b,c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal Triangle", sides)
    p = (a+b+c)/2
    a = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return a


'''
chaining exceptions
'''

# chaining exceptions
# implicit chaining - during handling of one exception, another one occurred. Implented using the __context__
# explicit chaining 

# tracebacks
# records of the function stacks 
__traceback__ 

import traceback 

def inclination(dx, dy):
    try:
        dx + dy
    except ZeroDivisionError as e:
        raise InclinationError('Some custom error') from e

def main():
    try:
        inclination(0,5)
    except InclinationError as e:
        print(e.__traceback__)
        traceback.print(e.__traceback__)
        s = traceback.format_tb(e.__traceback__)
        print(s)

# assertions for monitoring program invariants (should always be true)
assert condition , message # optional error string to print if condition is False

def func():
    if:
        # 
    elif:
        #
    else:
        assert False, "This should never happen"

# class invariants

# assertions are for checking function implementations
# shouldn't use it for validating client inputs, instead should just raise errors
# use assertions for checking preconditions and postconditions
assert(all(len(line)<=line_length for line in result.splitlines())


# minimize upfront testing 

# The following is often what's done:
try:
    found = value in some_argument
except TypeError:
    if not isinstance(some_argument, collections.abc.Container):
        warnings.warn( "{0!r} not a Container".format(some_argument) )
    raise


'''
explicit vs. implicit checking
'''

class Card: 
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit 
    
    # explicit checking here
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank < other.rank 
    
    # implicit using try: except
    
    def __le__(self, other):
        try: 
            return self.rank <= other.rank
        except AttributeError:
            raise NotImplemented
        
class Table:
    def __init__(self):
        self.deck = Deck()
    
    def get_hand(self):
        try: 
            self.hand = Hand(d.pop(), d.pop())
        except IndexError:
            self.deck = Deck()
            return self.get_hand()


'''
retry
'''

def fetch_streams_with_retry(plugin, interval, count):
    """Attempts to fetch streams repeatedly
       until some are returned or limit hit."""

    try:
        streams = fetch_streams(plugin)
    except PluginError as err:
        log.error(u"{0}".format(err))
        streams = None

    if not streams:
        log.info("Waiting for streams, retrying every {0} "
                 "second(s)".format(interval))
    attempts = 0

    while not streams:
        sleep(interval)

        try:
            streams = fetch_streams(plugin)
        except FatalPluginError:
            raise
        except PluginError as err:
            log.error(u"{0}".format(err))

        if count > 0:
            attempts += 1
            if attempts >= count:
                break

    return streams


'''
assertions
'''
def modules_three(n):
    r = n % 3
    if r == 0:
        print("multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:
        assert r == 2, "Remainder is not 2"
        print("Remainder 2")
