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

'''
type of errors
'''
IndexError
KeyError 
ValueError
ZeroDivisionError

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
    print(error)
else:
    # no exceptions. run this
    print('Executing the else clause')
finally:
    # always run this code 
    print('Cleaning up, irrespective of any exceptions.')


# accessing error mesages
try:
    # some code
except Exception as e:
    # some code
    print("Exception occured: {}".format(e))


# never let exceptions pass silently
# the except clause needs specified exception 

try:
    print('abc')
except:
    pass 


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

# using the exception payload
try:
    result = divide(x, y)
except ValueError as e: 
    print('Payload', e.args)
    print(str(e)) # an alternative
else:
    print('Result is %.1f' % result)


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
# just define new exceptions as classes which inherit from Exception 

class NetworkError(Exception):
    pass
class HostnameError(NetworkError):
    pass


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

