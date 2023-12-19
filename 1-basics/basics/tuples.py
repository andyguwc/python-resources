##################################################
# Tuple
##################################################

'''
Immutable
'''
# immutable
# use tuple as data records
# the order matters, can be either same or different data types, indexable, iterable, immutable (fixed length, fixed order)

# immutability
# elements can't be added or removed
# the order of elements can't be changed

# indexable
city = ("London", "UK", 87000)
city[0]


'''
Unpacking
'''

# In python automatically packed into a tuple
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# tuple assignment
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
city, _, population = ("London", "UK", 87000) # ignoring fields

# tuple unpacking
authors = [('a1','a2'),('b1','b2')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)

# unpacking tuple as arguments
def add(x, y):
    return x + y
z = (5,4)
print(add(*z))

# using * to grab excess items
a,b, *rest = range(5) # rest will be assigned [2,3,4]


'''
named tuple
'''

# namedtuple adds a layer to assign property names to the positional elements
# namedtuple is a function (class factory)
# using it to create a new class, and the class instance is a tuple
# namedtuple needs the following to generate a class
# - the class name we want to use
# - a sequence of field names we want to assign
# - the return value of the class to namedtuple will be a class

from collections import namedtuple

Point2D = namedtuple("Point2D", ["x", "y"])
Point2D = namedtuple("Point2D", "x y")
pt1 = Point2D(10, 20) # can be positional
pt2 = Point2D(x=10, y=20) # can use keyword

# can access data using field names
pt1.x, pt1.y


# https://pymotw.com/3/collections/namedtuple.html
# namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance dictionaries. Each kind of namedtuple is represented by its own class, which is created by using the namedtuple() factory function. The arguments are the name of the new class and a string containing the names of the elements.

# without using namedtuple, we have to implement a class with __repr__ method and the __eq__ method for comparison (Point(10, 20) == Point(10, 20))

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        else:
            return False

# Two parameters are required to create a named tuple: 
# - a class name and 
# - a list of field names, which can be given as an iterable of strings or as a single spacedelimited string.

from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

BlackjackCard = namedtuple('BlackjackCard', 'rank, suit, hard, soft')
    
# namedtuple is helpful for cases we need to name a fixed set of attributes
City = namedtuple('City', 'name country population coordinates')

# Data must be passed as positional arguments to the constructor (in contrast, the tuple constructor takes a single iterable).
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# can access fields by name or position
tokyo.population
tokyo[1]

Person = namedtuple('Person', 'name age')
bob = Person(name='Bob', age=20)
jane = Person(name='Jane', age=22)
print('Field by name:', jane.name)

for p in [bob, jane]:
    print('{} is {} years old'.format(*p))

# immutable
# Just like a regular tuple, a namedtuple is immutable. This restriction allows tuple instances to have a consistent hash value, which makes it possible to use them as keys in dictionaries and to be included in sets.


# assign values to Namedtuples
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records: 
        s = Stock(*rec)
        total += s.shares * s.price
    return total 

# note on using dict, namedtuple or class for book-keeping 
# Use namedtuple for lightweight, immutable data containers before you need the flexibility of a full class.
# Move your bookkeeping code to use multiple helper classes when your internal state dictionaries get complicated


# extracing to dictionary
Point2D = namedtuple("Point2D", "x y")
pt1 = Point2D(10, 20)
pt1._asdict() # {'x': 10, 'y': 20}

# using named tuples as a possible alternative to dictionaries
data_dict = dict(key1=100, key2=200, key3=300)
Data = namedtuple("Data", data_dict.keys())
d = Data(**data_dict)
getattr(d, "key1")


# convert a list of dictionaries

data_list = [
    {"key1": 1, "key2": 2},
    {"key1": 3, "key2": 4},
    {"key1": 5, "key2": 6, "key3": 7},
]

keys = {key for dict_ in data_list for key in dict_.keys()}

# sort the keys to keep the order
Struct = namedtuple("Struct", sorted(keys))
# Struct._fields ('key1', 'key2', 'key3')
# creating defaults
Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
Struct(key3=10)
result = [Struct(**dict_) for dict_ in dicts]


'''
docstrings and default values
'''
# docstring
Point2D = namedtuple("Point2D", "x y")
# Point2D.__doc__
# Point2D.x.__doc__,  Point2D.y.__doc__

Point2D.__doc__ = "Represents a 3D Cartesian coordinate"
Point2D.x.__doc__ = "x coordinate"

# default values
# 1. create an instance of the namedtuple with default values - the prototype, then create any additional instances using prototype._replace method

Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2")
v0 = Vector2D(0, 0, 0, 0) # default value
v1 = v0._replace(x1=10, y1=10, x2=20, y2=20)

# 2. Or using the __defaults__ property

def func(a, b=10, c=20):
    pass
func.__defaults__ # (10, 20)
# the __defaults__ property is writable and we can set it to an arbitrary tuple

Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2")
Vector2D.__new__.__defaults__ = (0, 0)




'''
subclassing namedtuple
'''
# modifying named tuples
# suppose want to modify the last element
*current, _ = pt1
pt2 = Point2D(*current, 30)

# extending a named tuple
Record = namedtuple("Record", "symbol year month day open high low")
new_fields = Record._fields + ("close", )
NewRecord = namedtuple("NewRecords", new_fields)


# since named tuples are built on top of regular python classes, 
# you can add methods to a namedtuple object 

Car = namedtuple('Car', 'color mileage')

class MyCarWithMethods(car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
        return '#000000' 

c = MyCarWithMethods('red', 1234)
>>> c.hexcolor()

# create hierarchies of namedtuples 
Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple(
    'ElectricCar', Car._fields + ('charge',))


'''
special attributes / methods
'''
# _fields
# The names of the fields passed to namedtuple to define the new class are saved in the _fields attribute.
Person = collections.namedtuple('Person', 'name age')
bob = Person(name='Bob', age=30)
print(bob._fields) # returns a tuple of fields ('name', 'age')

# _asDict() returns contents as an OrderedDict
Person = collections.namedtuple('Person', 'name age')
bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('As Dictionary:', bob._asdict())
# OrderedDict([('name', 'Bob'), ('age', 30)])

my_car._asdict()
# OrderedDict([('color', 'red'), ('mileage', 3812.4)])

json.dumps(my_car._asdict())
# '{"color": "red", "mileage": 3812.4}'

# _replace
# The _replace() method builds a new instance, replacing the values of some fields in the process. The replace method creates a shallow copy of a tuple and replace some fields
my_car._replace(color='blue')
# Car(color='blue', mileage=3812.4)

# Create new instances of a tuple from a sequence or iterable
Car._make(['red', 999])
# Car(color='red', mileage=999)

