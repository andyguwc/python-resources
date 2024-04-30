
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

even_squares = [x * x for x in range(10)
                if x % 2 == 0] 

values = [expression 
          for item in collection 
          if condition]


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
multiple levels
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)
# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# if you want to square the value in each cell of a two-dimensional matrix.
squared = [[x**2 for x in row] for row in matrix]
print(squared)
# >>> [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

[(x, y) for x in range(10) for y in range(x)]
# same thing as before
result = []
for x in range(10):
    for y in range(x):
        result.append((x, y))


'''
Generator Expressions
'''

# To initialize tuples, arrays, and other types of sequences, you could also start from a
# listcomp, but a genexp saves memory because it yields items one by one using the iterator
# protocol instead of building a whole list just to feed another constructor.

# When processing one item at a time, we only need the current object stored in memory at any one moment. But when we create a container, all the
# objects have to be stored in that container before we start processing them.

# Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than
# brackets.

tuple(ord(symbol) for symbol in symbols)


# cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['S','M','L']
# using a generator expression saves the expense of building a list of a lot of items
# generator expressions
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)


'''
map()
'''
# map - apply a function to every element in a sequence, producing a new sequence
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
# returns lazy iterable, needs to apply list to evaluate
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

# reduce 
# repeatedly apply a function to the elements of a sequence, reducing them to a single value 
from functools import reduce 
import operator 
reduce(operator.add, [1,2,3,4,5])
# takes an optional default value 
values = [1,2,3]
reduce(operator.add, values, 0)
 


