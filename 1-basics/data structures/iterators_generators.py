

##################################################
# Iteration
##################################################


# using iterator by next
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


'''
delegating iterator to __iter__()
'''
class Node:
    def __init__(self, value):
        self._value = value 
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    
    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
        return iter(self._children)

# example 
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

# Python’s iterator protocol requires __iter__() to return a special iterator object that
# implements a __next__() method to carry out the actual iteration.

##################################################
# Iterators and Generators
##################################################

'''
Iterators and Generators
'''

# iterable - an object which implements the __iter__() method (which returns an iterator)
# an iterator is an object with a next() method and a done() method 
# all iterators are iterables which generally just return themselves with __iter__()
# generator creates iterator using functions

# iter() create an iterator
# next() get next element in sequence
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

# for loop is a syntactic implementation for a while loop 
for item in iterable: 
    print(item)

# similar to 
# iterator = iterable.__iter__()

# while True: 
#     item = iterator.__next__()
#     print(item)


'''
Iterable vs.Iterator
'''

# python obtain iterators from iterables 

# iterables have an __iter__ method that instantiates a new iterator every time.
# Iterators implement a __next__ method that returns individual items, and an __iter__
# method that returns self.

s = 'ABC' # str 'ABC' is the iterable here
for char in s: # iterator behind the scenes
    print(char)

s = 'ABC'
it = iter(s) # build an iterator it from the iterable
while True: 
    try:
        print(next(it)) # call next on the iterator to obtain the next item 
    except StopIteration:
        del it
        break 

# classic iterator 
# iterator pattern
import re 
import reprlib 

RE_WORD = re.compile('\w+')
class Sentence: 
    def __init__(self, text):
        self.text = text
        self.words = RE_WORLD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)    
    
    # Sentence is iterable because it implements the __iter__ special method
    # which builds and returns a SentenceIterator
    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words # holds a reference to the list of words
        self.index = 0 
    
    def __next__(self): 
        try:
            word = self.words[self.index]
        except IndexError: # if no word at self.index, raise StopIteration
            raise StopIteration()
        self.index+=1
        return word 
    
    def __iter__(self): #implement the self.__iter__
        return self 


# alternative implementation
# use the yield (generator function) to replace the SentenceIterator class 
import re 
import reprlib 

RE_WORD = re.compile('\w+')


class Sentence: 
    def __init__(self, text):
        self.text = text 
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word in self.words: 
            yield word 
        return 


# another example 
# loop through each of the words in a string and output them with the first letter capitalized 
class CapitalIterable:
    def __init__(self, string):
        self.string = string 

    def __iter__(self):
        return CapitalIterator(self.string)
    
    
class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0 
    
    def __next__(self):
        if self.index = len(self.words):
            raise StopIteration()
    
        word = self.words[self.index]
        self.index += 1
        return word 
    
    def __iter__(self):
        return self 

# example utilizing the iterable 
iterable = CapitalIterable('the quick brown fox')
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break 


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

'''
__getitem__()
'''
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

'''
iterating in reverse 
'''

a = [1,2,3,4]
for x in reversed(a):
    print(x)

# print a file backwards 
f = open('somefile')
for line in reversed(list(f)):
    print(line, end='')

# reversed iteration can be customozed on user defined classes with the __reversed__() method
class Countdown:
    def __init__(self, start):
        self.start = start 
    
    # forward iterator 
    def __iter__(self):
        n = self.start 
        while n > 0:
            yield n 
            n -= 1

    # reverse iterator 
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n 
            n += 1

'''
Stacking Iterators 
'''
# stacking generators together 
# yield acts as a kind of producer while for loop acts as a data consumer 
import os 
import fnmatch 
import gzip
import bz2
import re 

def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree
    '''
    for path, dirlist, filelist is os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time 
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f 
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together
    '''
    for it in iterators:
        yield from it 

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines 
    '''
    pat = re.compile(pattern)
    for line in lines: 
        if pat.search(line):
            yield line 

lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)



''' 
yield 
'''

# best practice use yield results instead of append to list 

def index_word_iter(text):
    if text:
        yield 0 
    for index, letter in enumerate(text):
        if letter == '':
            yield index+1 
# the iterator returned by the call can be converted to list 
result = list(index_word_iter(text_data))

# bad implementation using list 
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ‘ ‘:
            result.append(index + 1)
    return result


# the presence of the yield statement turns a function into a generator 
# customize an iteration pattern 
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x 
        x += increment 

# yield from 
from collections import Iterable 

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x 

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

# yield from flatten(x) is the same as for i in flatten(x): yield i 
n 


# using yield as generator expressions
import sys
inname, outname = sys.argv[1:3]

# filter for specific patterns
def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')

with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)


'''
slice of an iterator 
'''
# use the itertools.isslice() function for taking slices of iterators and generators 

def count(n):
    while True: 
        yield n 
        n += 1

c = count(0)
import itertools 
for x in itertools.islice(c, 10, 20):
    print(x)

# want everything beyond the first three items 
# for x in itertools.islice(c, 3, None):



