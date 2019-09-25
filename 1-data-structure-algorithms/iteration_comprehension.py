##################################################
# Iteration
##################################################

for name in ['a','b','c']:
    print(name)

# accumulator pattern
nums = [1,2,3,4]
res = 0
for w in nums:
    res = res + w 
print(res)

# traversal
for counter, item in enumerate(['a','b','c']):
    print(counter, item)

for n in range(len(fruit)):
    print(n, fruit[n])


# enumeration
# return an iterable. using for loop then index, value
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# while loop
def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """
    theSum  = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

# break and continue
while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?")

print("We are done with the while loop.")

# continue is the other keyword that can control the flow of iteration. Using continue allows the program to immediately “continue” with the next iteration. 
# The program will skip the rest of the iteration, recheck the condition, and maybe does another iteration depending on the condition set for the while loop.

for name in student_names:
    if name == "mark":
        print('found him'+name)
        break
    print("currently testing "+name)

for name in student_names:
    if name == "bort":
        continue # continue to the next iteration
        print("found him"+name)
    print("currently testing"+name)


##################################################
# List Comprehensions & Maps
##################################################
'''
Comprehensions
'''
l = [i*2 for i in range(10)]
d = {i: i*2 for i in range(10)}

# multi-input comprehensions

# nested comprehensions
vals = [[y*3 for y in range(x)] for x in range(10)]

# list comprehensions do everything map and filter functions do 
symbols = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

'''
Cartesian Product 
'''

[(x,y) for x in range(5) for y in range(3)]

tshirts = [(color, size) for color in colors for size in sizes]


'''
Generator Expressions
'''

# To initialize tuples, arrays, and other types of sequences, you could also start from a
# listcomp, but a genexp saves memory because it yields items one by one using the iterator
# protocol instead of building a whole list just to feed another constructor.

# Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than
# brackets.

tuple(ord(symbol) for symbol in symbols)


colors = ['black', 'white']
sizes = ['S','M','L']
# using a generator expression saves the expense of building a list of a lot of items
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)




'''
map()
'''
# map - apply a function to every element in a sequence, production a new sequence
# returns a map object, it only produces values as it's needed 
map(ord, 'the quick brown') # ord is the mapping function
list(map(ord, 'the quick brown')) # use list for use a for loop 

# multiple input sequences 
# map can accept any number of input sequences 
map(func, a, b, c) 
def combine(size, color, animal):
    return '{} {} {}'.format(size, color, animal)
list(map(combine, sizes, colors, animals))

# filter
# apply a function to each element in a sequence, constructing a new sequence with the elements for which the function returns True
filter(is_odd, [1,2,3,4,5])
positives = filter(lambda x:x>0, [1,-5,0,2])

# reduce 
# apply a function to the elements of a sequence, reducing them to a single value 
from functools import reduce
import operator
reduce(operator.add, [1,2,3])

# multiply function to print out intermediate results
def mul(x, y):
    print('mul {} {}'.format(x, y))
    return x*y
reduce(mul, range(1,10))

# map and filter functions 
list(map(factorial, range(6)))
[factorial(n) for n in range(6)]

list(map(factorial, filter(lambda n: n%2, range(6))))
[factorial(n) for n in range(6) if n%2]

# Anonymous Functions 

 

##################################################
# Iterators and Generators
##################################################

'''
Iterators and Generators
'''

# iterable - an object which implements the __iter__() method

# iterables are objects that can return one of their elements a time
# iterator is an object that is a stream of data (implements the iterable protocols amd __next__ method)
# generator creates iterator using functions

# iter() create an iterator
# next() get next elment in sequence
# stopIteration signal the end of the sequence

def my_range(x):
    i =0
    while i <x:
        yield i
        i+=1

for n in my_range(4):
    print(n)

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

iterable = ['a','b','c']
iterator = iter(iterable)
next(iterator) # prints 'a'
next(iterator) # prints 'b'

# stateful iterator functions

def distinct(iterable):
    """return unique item by eliminating duplicates
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items = [1,2,3,4]
    for item in distinct(items):
        print(item)

# alternative, __getitem__ which works for consecutive integers
class AlternateIterable:
    def __init__(self):
        self.data=[1,2,3]
    def __getitem__(self, idx):
        return self.data[idx]

# extended iter()
iter(callable, sentinel) #callable that takes zero arguments, sentinel - iteration stops when callable produces this value

import random
class Sensor:
    def __iter__(self):
        return self
    def __next__(self):
        return random.random()

sensor = Sensor()
timestamps = iter(datetime.datetime.now, None)
