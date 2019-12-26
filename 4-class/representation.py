##################################################
#  Object Representations (repr)
##################################################

'''
repr vs. str 
'''
# As you know, we implement the special methods __repr__ and __str__ to support
# repr() and str().

# repr()
# Return a string representing the object as the developer wants to see it.
# produces an unambiguous string representation of an object
# exactness more important - good for debugging and logging 
# usually the text you would type for recreateing the instance 
__repr__() 


# str()
# Return a string representing the object as the user wants to see it.
# intended for clients
# readable, human-friendly output 
# if do not define str(), the defaul falls to repr()
__str__() 


class Point2D:
    def __init__(self, x, y):
        self.x=x
        self.y=y 
    # for use print('the circle is centered at {}.'.format(p))
    def __str__(self):
        return '({},{})'.format(self.x, self.y)
    
    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)


# Specifically, the special !r formatting code indicates that the
# output of __repr__() should be used instead of __str__(), the default

# >>> p = Pair(3, 4)
# >>> print('p is {0!r}'.format(p))
# p is Pair(3, 4)
# >>> print('p is {0}'.format(p))
# p is (3, 4)


# format options 
__format__

# customized formatting 
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day 
    
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)
    



class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x=float(x)
        self.y=float(y)
    
    # makes unpacking work 
    # implement via generator expression
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        # interpolating the components with {!r} to get their repr
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
        bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))


def __repr__(self):
    return "{__class__.__name__}(suit={suit!r}, rank={rank!r}". \
                format(__class__=self.__class__, **self.__dict__)

def __str__(self):
    return "{rank}{suit}".format(**self.__dict__)


''' 
format
'''
# The format() built-in function and the str.format() method delegate the actual formatting
# to each type by calling their .__format__(format_spec) method

# The format() method of a string can also access these methods. When we
# use {!r} or {!s} formatting, we're requesting __repr__() or __str__(),
# respectively.


# '1 BRL = {rate:0.2f} USD'.format(rate=brl)

from datatime import datetime 
now = datetime.now()
format(now, '%H:%M:%S')
"It's now {:%I:%M %p}".format(now)
"{0:06.4f}" # 06.4f is the format specification that applies to item 0 of the argument list to be formatted 

# def format 
def __format__(self, fmt_spec=''):
    components = (format(c, fmt_spec) for c in self)
    return '({},{})'.format(*components)

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
    
    @property
    def x(self):
        return self.__x 
    
    @property 
    def y(self):
        return self.__y 
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
# nested format
for hand, count in statistics.items():
    print("{hand}{count:{width}d}".format(hand=hand, count=count,width=wiwdth))

'''
Saving Space with __slots__ class attribute
'''
# If you are dealing with millions of instances with few attributes, the
# __slots__ class attribute can save a lot of memory, by letting the interpreter store the
# instance attributes in a tuple instead of a dict.

class Vector2d:
    __slots__ = ('__x', '__y')
    typecode = 'd'
    # methods follow 
