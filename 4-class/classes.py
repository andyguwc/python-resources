##################################################
# Classes
##################################################
# an object has a state and a collection of methods that it can perform
# the state is stored in instance variables

# benefits - write manageable and maintable code 
# student = Student() - creating a new instance of a Student class 


# contructor 
class Point:
    """ Point class for representing and manipulating x, y coordinates"""
    def __init__(self):
        """Create a point at the origin"""
        self.x = 0
        self.y = 0
    
p = Point() # instantiate an object of type Point - i.e. a combination of making a new object and get settings initialized for the default settings
q = Point() # make a second point

# adding parameters to the Constructor
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX # assigned to state of the object, in the instance variables x and y
        self.y = initY
p = Point(7,6)

# all methods defined in a class that operate on objects of that class will have self as their first parameter. 
# Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distanceFromOrigin(self):
        return ((self.x**2)+(self.y**2))**0.5

    # an alternative is to define the function outside the object as distance(point1, point2)
    def distance(self, point2):
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(7,6)
print(p.getX())
print(p.getY())

# special printing method 
# __str__
class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

# instances as return values

class Point: 
    # ...
    # return the midpoint 
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

# sorting lsit of instances

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple",5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)

# class variable vs instance variable
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    printed_rep = "*" # this is a class variable the same across all instances 
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def graph(self):

print(Point.printed_rep) # calling class attribute directly




# what is the data you want to deal with 
# what will one instance of the class represent
# what information should each instance have as instance variables
# what instance methods should each instance have 

'''
Inheritance
'''

# specify just the differences in the new inherited class
# class variable sounds starts out with the string "Meow" instead of the string "mrrp", and there is a new method chasing_rats

class HighSchoolStudent(Student):
    school_name = 'new high school'

    def get_name(self):
        original_value = super().get_name()

# class SubClass(BaseClass)
# base class __init__() is not called if overwritten, unless define init as super().__init__()

# super() used to call method on base class

class SimpleList:
    def __init__(self, items):
        self._items = items
    
    def add(self, item):
        self._items.append(item)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def sort(self):
        self._items.sort()
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "Simplelist({!r})".format(self._items)

class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()
    
    def add(self, item):
        super().add(item)
        self.sort()
    
    def __repr__(self):
        return "SortedList({!r})".format(list(self))

# isinstance() determines if an object is of a specified type
# also returns true if subclass of the type
isinstance('hello', str)

# issubclass()
# determines if one type is a subclass of another

# multiple inheritance
# define class with more than one base class 
class SubClass(Base1, Base2):
    pass
# subclass inherit methods of all bases 
# if a class defines no intializer, then only the init from the first base class is called
# __bases__ a tuple of base classes 
# method resolution order 
SortedList.__mro__ # to print out the method resolution order 


# super()
# given a method resolution order and a class C, super gives you an object which resolves method using only the part which comes after C
# super() returns a proxy object which routes method calls
super(base-class, derived-class) 
# instance bound proxy
super(class, instance-of-class)

# object model
# the ultimate base class of every class object 
NoBaseClass.__bases__
dir(object) # outputs ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# polymorphism
# use objects of different types through a common interface
# determined at the time of use 

