##################################################
# Tuple
##################################################

'''
Tuple
'''
# use tuple as data records 


# In ptyhon automatically packed into a tuple
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# Slice Operator
singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
fruit = "banana"
print(fruit[:3])

# Concatenation and Repitition
fruit = ["a", "b", "c"]
print([1,2]+[3,4])
print([0]*4)

# tuple assignment 
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)


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
# https://pymotw.com/3/collections/namedtuple.html
# namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance dictionaries. Each kind of namedtuple is represented by its own class, which is created by using the namedtuple() factory function. The arguments are the name of the new class and a string containing the names of the elements.

# Two parameters are required to create a named tuple: 
# - a class name and 
# - a list of field names, which can be given as an iterable of strings or as a single spacedelimited string.

from collections import namedtuple

Card = collections.namedtuple('Card', ['rank', 'suit'])

BlackjackCard = namedtuple('BlackjackCard', 'rank, suit, hard, soft')
    
# namedtuple is helpful for cases we need to name a fixed set of attributes
City = namedtuple('City', 'name country population coordinates')

# Data must be passed as positional arguments to the constructor (in contrast, the tuple constructor takes a single iterable).
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# can access fields by name or position
tokyo.population
tokyo[1]

Person = collections.namedtuple('Person', 'name age')
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


'''
subclassing namedtuple
'''
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

