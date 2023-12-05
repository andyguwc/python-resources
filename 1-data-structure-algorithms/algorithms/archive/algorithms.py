# Built in Atomic Data Types
# int, float, bool

# Built in Collection Data Types

# List Operations
# [] indexing
# + concatenation 
# [:] slicing
# in membership

# List Methods 
alist.append(item) # adds new item to the end of list
alist.insert(i, item)
alist.pop() # removes the last element
alist.pop(i) # removes the ith element
alist.sort() # modifies a list to be sorted
del alist[i] # deletes the item in the ith position
alist.index(item) # returns the index of the first occurence of item


list(range(10)) # range(5,10) starts at 5 and goes up to but not including 10. range(5,10,2) performs similarly but skips by twos (again, 10 is not included).


# String Methods
astring.count(item) # returns the number of occurences of item in string
astring.lower() # a string in all lowercase
astring.ljust(w) # string left adjusted in a field of size w
astring.find(item) # returns the index of the first occurence of item


# List if Mutable and String is Immutable
myList = [1,3,True, 6.5]
myList[0] = 2**10

# Tuple is like a list but immutable

# Sets do not allow duplicates
in # set membership
len # returns length
& # only if in both sets
- # from the first not in the second
union
intersection

# Dictionary
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}

phoneext={'david':1410,'brad':1137}
list(phoneext.keys())
list(phoneext.items())
list(phoneext.values())


# Input and Output
print("Hello", "World")
print("%s is %d years old" % (aName, age)) # print("%s is %d years old." % (aName, age))
# d,i integer; u unsigned integer; f floating point; s String

# Control Structures
counter = 1
while counter <= 5:
	print("Hello World")
	counter +=1

for item in [1,2,3,4,5]:
	print(item)

for item in range(5):
	print(item**2)

if n<0:
	print("sorry negative")
else:
	print(math.sqrt(n))

sqlist = []
for x in range(1,11):
	sqlist.append(x*x)

sqlist = [x*x for x in range(1,11) if x%2 !=0] 


# Exception Handling

 try:
 	print(math.sqrt(anumber))
 except:
 	print("Bad Value for square root")
 	print("Using absolute value instead")
 	print(math.sqrt(abs(anumber)))

if aNumber < 0:
	raise RuntimeError("you can't have a negative number")
else:
	print(math.sqrt(aNumber))


try: 
	print(math.sqrt(anumber))
except:
	print("bad value for square root")
	print(math.sqrt(abs(anumber)))
# Defining Functions

def square(n):
	return n**2


# Defining Classes
# Fraction Class

class Fraction:
	def __init__(self, bottom, top):
		self.num = top
		self.den = bottom 
	
	def show(self):
		print
class Fraction:
	def __init__(self, bottom, top):
		self.num = top
		self.den = bottom

    def show(self):
    	print(self.num,"/",self.den) 

    myf = Fraction(3,5)
    myf.show()
    print(myf)

    # overrides the string method
    def __str__(self):
    	return str(self.num)+"/"+str(self.den)

    # overrides the add method
    def __add__(self, otherFraction):
    	newnum = self.num*otherFraction.den + self.den*otherFraction.num
    	newden = self.den * otherFraction.den
    	common = gcd(newnum, newden)
    	return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
    	firstnum = self.num*other.den
    	secondnum = other.num*other.num
    	return firstnum == secondnum 


    # Inheritance
    class LogicGate:
    	def __init__(self,n):
    		self.label = n
    		self.output = None

    	def getLabel(self):
    		return self.label

    	def getOutput(self):
    		self.output = self.performGateLogic()
    		return self.output

    	class BinaryGate(LogicGate):

	    def __init__(self,n):
	        LogicGate.__init__(self,n)
	        self.pinA = None
	        self.pinB = None

	    def getPinA(self):
	        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

	    def getPinB(self):
	        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))


# Big O Algorithm Analysis 

# f(n)	Name
# 1	 Constant
# logn	Logarithmic
# n	Linear
# nlogn	Log Linear
# n2  Quadratic
# n3  Cubic
# 2n  Exponential


def anagramSolution1(s1,s2):
	alist = list(s2)
	pos1 = 0
	stillOK = True
	while pos1 < len(s1) and stillOK:
		pos2 = 0
		found = False
		while pos2 < len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				found = True
			else pos2 +=1

		if found:
			alist[pos2] = None
		else:
			stillOK = False
		pos1+=1

	return stillOK

print(anagramSolution1('abcd','dcba'))


# To analyze this algorithm, we need to note that each of the n characters in s1 will cause an iteration through up to n characters in the list from s2. Each of the n positions in the list will be visited once to match a character from s1. 

# Sort and compare 
def anagramSolution2(s1, s2):
	alist1 = list(s1)
	alist2 = list(s2)
	alist1.sort()
	alist2.sort()
	pos = 0
	matches = True
	while pos < len(alist1) and matches:
		if alist1[pos] == alist2[pos]:
			pos+=1
		else:
			matches = False
	return matches

print(anagramSolution2('abcde','edcba'))

# Two count counters 
def anagramSolution4(s1, s2):
	c1 = [0]*26
	c2 = [0]*26
	for i in range(len(s1)):
		pos = ord(s1[i]) - ord('a')
		c1[pos]+=1
	for i in range(len(s2)):
		pos = ord(s2[i]) - ord('a')
		c2[pos]+=1
	pos = 0 
    matches = True
	while i<= len(c2) and matches:
		if(c1[pos] == c2[pos]):
			pos +=1
		else matches = False
	return matches 

# Dictionaries 

# copy - O(n)
# get - O(1)
# set - O(1)
# delete - O(1)


# Linear Structures
# Once an item is added, it stays in that position relative to the other elements that came before and came after it. Collections such as these are often referred to as linear data structures.

# Stack 
# Last In First Out
# Order of insertion is the reverse of the order of removal


# Stack Operations
s.isEmpty()
s.push(4)
s.push('dog')
s.peek()
s.push(True)
s.size()
s.pop()


# Implement Stack Using List
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)



class Printer:
	def __init__(self, ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask != None:
			self.timeRemaining -=1
			if self.timeRemaining <=0:
				self.currentTask = None

	def busy(self):
		if self.currenTask != None:
			return True
		else:
			return False

	def startNext(self,newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages()*60/self.pagerate



# Dequeue - Double Ended Queue
# Add Rear
# Add Front - front is to the right of the list

Dequeue() # empty
addFront(item)
addRear(item)
removeFront(item)
removeRear(item)
isEmpty()
size()

class Dequeue:
	def __init__(self):
		self.items = []

	def addRear(self, item):
		self.items.insert(item,0)

	def addFront(self, item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

# Palindrome - string that reads the same forward and backward 

from pythonds.basic.dequeue import Dequeue
def palchecker(aString):
	chardeque = Dequeue()
	for i in aString: 
		charDeque.addRear(ch)
	stillEqual = True
	while chardeque.size()> 1 and stillEqual:
		first = chardeque.removeFront()
		last = chardeque.removeRear()
		if first != last:
			stillEqual = False
	return stillEqual 

# def palchecker(aString):
# 	if len(aString) <=1:
# 		return True
# 	else:
# 		return aString[0] == aString[-1] and palchecker(aString[1:-1])
	
# Lists
List()
add(item)
remove(item)
search(item)
isEmpty()
size()
append(item)
index(item)
insert(pos,item) # add a new item at position pos
pop()
pop(pos) # remove and return the item at position pos


# LinkedLists

# Location on the first item of the list is explicitly speified. The first item will tell us the second item, etc.

# Node Class - each node will hold a reference to the next node and the list item itself

class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext


class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	# easiest place to add the new node is at the front. Existing items will be linked to this new item
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	# linkedin list traversal
	# sytematically visits every node
	def size(self):
		current=self.head
		count = 0
		while current != None:
			count+= 1
			current = current.getNext()
		return count

	# search method 
	# use a boolean variable called found to remember whether we have located the item 
	def search(self,item):
		current= self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else: 
				previous = current 
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())


# Ordered Linked List Abstract data type
OrderedList() # creates a new ordered list that is empty
add(item) # add a new item to the list making sure order is preserved
remove(item) # removes the item from the list
search(item) # searches for the item on the list
isEmpty() # whether the list is empty
size() # returns the number of items
index(item) # returns the position of the item
pop() # remove and return the last item
pop(pos) # remove and return the item at position pos


# Implementing an Ordered List
class OrderedList:
	def __init__(self):
		self.head = None

	def search(self, item):
		found = False
		stop = False
		current = self.head
		while current !=None and not found and not stop:
			if current.getData() == item:
				found = True
			elif:
				current.getData() > item:
				stop = True
			else:
				current = current.getNext()

		return found 

	def add(self, item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData()>item:
				stop = True
			else:
				previous = current 
				current = current.getNext()

		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)


# Recursion
def listsum(numList):
	if len(listsum) == 1:
		return numList[0]
	else:
		return numList[0] + listsum(numList[1:])

# Have a base case
# change its state and move towards base case
# Call itself, recursively
def toStr(n, base):
	convertString = '0123456789ABCDEF'
	if n<base:
		return convertString[n]
	else:
		return toStr(n//base, base) + convertString[n%base]

# Impementing is based on a stack frame

# Dynamic Programming

# Recursive
def recMC(coinValueList, change):
	minCoins = change
	if change in coinValueList:
		return 1
	else:
		for i in [c for c in coinValueList if c <= change]:
			numCoins = 1+ recMC(coinValueList, change-i)
			if numCoins < minCoins:
				minCoins = numCoins
	return minCoins

# Dynamic Programming
# Store the results for the minimum number of coins in a table when we find them. Then before we compute a new minimum, we first check the table to see if a result is already known. 
# If there is already a result in the table, we use the value from the table rather than recomputing.
def dpMakeChange(coinValueList,change,minCoins):
	for cents in range(change+1):
		coinCount = cents
		for j in [c for c in coinValueList if c<cents]:
			if minCoins[cents-j]+1 < coinCount:
				coinCount=minCoins[cents-j]+1
		minCoins[cents]= coinCount
	return minCoins[change]


# Use Print Coins method

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
	for cents in range(change+1):
		coinCount = cents
		newCoin = 1
		for j in [c for c in coinValueList if c<cents]:
			if minCoins[cents-j]+1 < coinCount:
				coinCount= minCoins[cents-j]+1
				newCoin = j
		coinsUsed[cents] = newCoin
		minCoins[cents] = coinCount
	return minCoins[change]

def printCoins(coinUsed, change):
	coin = change
	while coin > 0:
		thisCoin = coinUsed[coin]
		print(thisCoin)
		coin = coin - thisCoin


# Sorting and Searching

def sequentialSearch(list, item):
	isFound = False
	pos = 0
	while pos < len(list) and not isFound:
		if list[pos]== item:
			isFound = True
		else:
			pos+=1
	return isFound

def sequntialSearch(list,item):
	isFound = False
	pos = 0 
	while pos < len(list) and not isFound:
		if list[pos] == item:
			isFound = True
		else: 
			pos+=1
	return isFound 

# Binary Search

# divide and conquer
def binarySearch(list, item):
	first = 0
	last = len(list)-1
	found = False

	while first < last and not found:
		midpoint = (first+last)//2
		if list[midpoint] == item:
			found = True
		else:
			if list[midpoint] < item:
				first = midpoint+1
			else:
				last = midpoint-1

# recursive version
def binarySearch(list, item):
	if len(list) = 0:
		return False 
	else:
		mid = len(list)//2
		if list[i] == item:
			isFound = True
	    elif list[i] < item:
			return binarySearch(list[:mid], item)
		else list[i] > item:
		    return binarySearch(list[mid:], item)

# Hashing

# a data structure to be searched in O(1) time
# hasing table - collection of items stored in a way to make it easier to find them later
# load factor = number of items / table size
# two or more items in the same slot - collision

# Collision Resolution
# when two items are hashed to the same slot
# Linear Probing - open addressing - find the next open slot or address in the hash table
# rehash(pos)=(pos+skip)%sizeoftable
# Problem with linear probin is clustering - i.e. if many collisions occur at the same hash value
# Quadratic Probing - where the skip values are quadratic series
# Chaining - as more and more items hash to the same location, the difficulty of searching for the item in the collection increases



# Implementing Map Data Type
# Store key data pairs
Map()
put(key, val)
get(key)
del
len()
in 

# Use two lists to implement the Map data type
# One list, called slots, will hold the key items and a parallel list, called data, will hold the data values. 
class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None]*self.size
		self.data = [None]*self.size

	def put(self, key, data):
		hashvalue = self.hashfunction(key, len(self.slots))
		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data
			else:
				nextslot = self.rehash(hashvalue, len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot, len(self.slots))

				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else:
					self.data[nextslot] = data
	
	def hashfunction(self,key,size):
		return key%size

    def rehash(self,oldhash,size):
    	return (oldhash+1)%size



# Sorting

# Bubble sort
# pass number start as n-1, and descreases to 0
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


# Quick Sort
# Use divide and conquer just like mergesort but without the need for more storage
# We begin by incrementing leftmark until we locate a value that is greater than the pivot value. We then decrement rightmark until we find a value that is less than the pivot value. 
# At this point we have discovered two items that are out of place with respect to the eventual split point.

def quickSort(alist):
	quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, left, right):
	pivot = alist[left]
	i = left
	j = right 
	while i<j:
		if alist[i] > pivot and alist[j]< pivot:
			alist[i], alist[j] = alist[j], alist[i]
			i++
			j--
		elif alist[i] <= pivot: 
			i++
		else alist[j] >= pivot:
			j--
	alist[i], alist[left] = alist[left], alist[i]
	quickSortHelper(alist,left,i-1)
	quickSortHelper(alist,i,right)


# official solution 
def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


# Trees
# Implement trees using lists
# Implement using classes and references
# As a recursive data structure 

# node
# Edge connects nodes
# root - only node in the tree that has no incoming edges
# Leaf node
# level 

# If each node in the tree has a maximum of two children, we say that the tree is a binary tree.

# A tree is either empty or consists of a root and zero or more subtrees, each of which is also a tree. 
# The root of each subtree is connected to the root of the parent tree by an edge. 


# Representation
# List of Lists
myTree = ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
     ]

def BinaryTree(r):
	return [r, [],[]]

def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t)>1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root


def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


# Representing as Nodes and References

class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t


# Using Stack and Trees

# So we can go back to the node
# Whenever we want to descend to a child of the current node, we first push the current node on the stack. 
# When we want to return to the origin of the current node, we pop the parent off the stack.

# Visit the nodes - traversal
# preorder, inorder, postorder
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# https://runestone.academy/runestone/static/fopp/Debugging/intro-DebuggingGeneral.html
# Debugging 
# Start small and keep adding small pieces to it to make it working
# Test the codes on a range of inputs - in particular boundary conditions
# Syntax, runtime, semantic errors

# ParseError, TypeError, NameError
# if type error, try print(x, type(x))

# Python Modules
# Standard library containing definitions and statements other programs can use. Functions imported as part of the module live in their own namespace
# For example can write unittests using the module unittests
# import morecode
# from morecode import f1

import random
prob = random.random()
result = prob * 5
print(result)


# List and Strings
# https://runestone.academy/runestone/static/fopp/Sequences/TheSliceOperator.html
fruit = "banana"
print(fruit[:3])
print(fruit[3:])

# List i mutable while String and Tuples are immutable
# List element deletion 
a = ['one', 'two', 'three']
del a[1]



# Slicing
[n:m]  # The slice operator returns the part of the string starting with the character at index n and go up to but not including the character at index m

# Concatenation and Repetition 
+ # concatenates print([1,2]+[3,4])
* # repeats a number of times 
# These operators create new lists

# Count and Index
# Count returns how many times xx appears
a = "I have had an apple on my desk before!"
print(a.count("e"))

# Index returns the leftmost index for xx
print(music.index("m"))

# An error occurs if not in the string

# Split and Joining Strings
song = "The rain in Spain..."
wds = song.split()
wds = song.split("a")
print(wds)


# The inverse of the split method is join. You choose a desired separator string, (often called the glue) and join the list with the glue between each of the elements.
print("***".join(wds))
print("".join(wds))

for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")

for achar in "Go Spot Go":
    print(achar)

# The anatomy of the accumulation pattern includes:
# initializing an “accumulator” variable to an initial value (such as 0 if accumulating a sum)
# iterating (e.g., traversing the items in a sequence)
# updating the accumulator variable on each iteration (i.e., when processing each item in the sequence)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)


# For loop
# Use enumerator to have an automatic counter
for counter, item in enumerate(['apple', 'pear', 'apricot', 'cherry', 'peach']):
    print(counter, item)

# Printing intermediate results 
w = range(10)

tot = 0
for num in w:
    print(num, tot)
    tot += num
print(tot)

# Operators

print('p' in 'apple') # True
print('i' in 'apple') # False

# Aliasing

# Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:
# Best way to copy is to clone the list using slice operator
b = a[:] 

# List Methods - Mutating and Non-mutating methods
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)


# Method	Parameters	Result	Description
# append	item	mutator	Adds a new item to the end of a list
# insert	position, item	mutator	Inserts a new item at the position given
# pop	none	hybrid	Removes and returns the last item
# pop	position	hybrid	Removes and returns the item at position
# sort	none	mutator	Modifies a list to be sorted
# reverse	none	mutator	Modifies a list to be in reverse order
# index	item	return idx	Returns the position of first occurrence of item
# count	item	return ct	Returns the number of occurrences of item
# remove	item	mutator	Removes the first occurrence of item


# append vs. concatenate
origlist = [45,32,88]
origlist.append("cat")
origlist = origlist + ["cat"]



s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)


# Accumulator Pattern

# What sequence will you iterate through as you accumulate a result? It could be a range of numbers, the letters in a string, or some existing list that you have just as a list of names.
# What type of value will you accumulate? If your final result will be a number, your accumulator will start out with a number and always have a number even as it is updated each time. 
# Similarly, if your final result will be a list, start with a list. If your final result will be a string, you’ll probably want to start with a string; one other option is to accumulate a list of strings and then use the .join() method at the end to concatenate them all together.



##############################################
# Working with Data Files
##############################################

open(filename,'r')	# Open a file called filename and use it for reading. This will return a reference to a file object.
open(filename,'w')	# Open a file called filename and use it for writing. This will also return a reference to a file object.
filevariable.close() # File use is complete.

# File Reading Methods
write filevar.write(astring)	# Add astring to the end of the file. filevar must refer to a file that has been opened for writing.
read(n)	filevar.read()	# Reads and returns a string of n characters, or the entire file as a single string if n is not provided.
readline(n)	filevar.readline()	# Returns the next line of the file with all text up to and including the newline character. If n is provided as a parameter than only n characters will be returned if the line is longer than n. Note the parameter n is not supported in the browser version of Python, and in fact is rarely used in practice, you can safely ignore it.
readlines(n) filevar.readlines()	# Returns a list of strings, each representing a single line of the file. If n is not provided then all lines of the file are returned. If n is provided then n characters are read but n is rounded up so that an entire line is returned. Note Like readline readlines ignores the parameter n in the browser.


# Open New Lines
olypmicsfile = open("olypmics.txt","r")

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()

# Find the files 
# If your file and your Python program are in the same directory you can simply use the filename.
open('data1.txt','r')

# If your file and your Python program are in different directories, however, then you need to specify a path. 
open('../myData/data2.txt','r')

open('/Users/joebob01/myFiles/allProjects/myData/data2.txt','r')


# Using With for Files
# Context manager, equivalent to just having ...close() at the end
with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
# continue on with other code



# Reading Text Files 
fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4


filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])


# Read from CSV

fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))


olympians = [("John Aalberg", 31, "Cross Country Skiing"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv","w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


# Dictionary 
# Start with empty dictionary and add key-value pairs 
dict = {}
dict['a'] = 'b'

mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])

# del statement removes key value pair from the dictionary
del inventory['pears']
inventory['pear'] = 0 # dictionary is mutable

# Dictionary methods
# keys(), values(), items()

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)


print(list(inventory.values()))
print(list(inventory.items()))

for k in inventory:
    print("Got",k,"that maps to",inventory[k])

# Because dictionaries are mutable, you need to be aware of aliasing (as we saw with lists). 
# Whenever two variables refer to the same dictionary object, changes to one affect the other.

# if wanted to modify and keep the original, use the copy() method
acopy = opposites.copy()


# Accumulator pattern in dictionary

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")

f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
	if c not in letter_counts:
		letter_counts[c] = 0 
	letter_counts[c]+=1


# Decoding a function

# Print is for people. Remember that slogan. Printing has no effect on the ongoing execution of a program. It doesn’t assign a value to a variable. It doesn’t return a value from a function call.


# Side Effects for Mutable Objects
# Instead of modifying a global variable inside a function, pass the global variable’s value in as a parameter, and set that global variable to be equal to a value returned from the function
# https://runestone.academy/runestone/static/fopp/Functions/PassingMutableObjects.html

# Tuples

# In ptyhon automatically packed into a tuple
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# Unpacking
# When a tuple is assigned to a collection of variable names separated by commas, the tuple is unpacked and the separate values are assigned to each of the variables.

https://runestone.academy/runestone/static/fopp/MoreAboutIteration/ThewhileStatement.html

# Optional Parameters
# initial = 7
def f(x, y =3, z=initial):
	print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

# Function Object
# lambda arguments: expression

print(lambda x: x-2) # function object
print((lambda x: x-2)(6)) # returned value from the function

def last_char(s):
    return s[-1]
last_char = (lambda s: s[-1])

print("This is a sentence".replace("s", "").replace("t", ""))

# Sorting
# Sorted vs. Sort
# Note that the sort method does not return a sorted version of the list. In fact, it returns the value None. But the list itself has been modified. This kind of operation that works by having a side effect on the list can be quite confusing.
# The function sorted rather than the method sort. Because it is a function rather than a method, it is invoked on a list by passing the list as a parameter inside the parentheses, rather than putting the list before the period. More importantly, sorted does not change the original list. Instead, it returns a new list.

L3 = sorted(L2)
print(L3)

L2.sort()
print(L2)
print(L2.sort())  #return value is None


# Sorting in dictionary

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)



x = [[1,2,3]], [4,5,6]]
y = list(x) # makes a shallow copy 

x.append(['new sublist'])
>>> x
x = [[1,2,3]], [4,5,6], ['new sublist']]
y = [[1,2,3]], [4,5,6]]

# Deep Copy



# Test Cases
# For example, before writing a function, write a few test cases that check that it returns an object of the right type and that it returns the correct values when invoked on particular inputs.

# Unit Tests
# In larger software projects, the set of test cases, called unit tests, can be run every time a change is made to the code base. This can help to identify situations where a change in code in one place breaks the correct operation of some other code. 

# Return a value. For these, you will write return value tests.
# Modify the contents of some mutable object, like a list or dictionary. For these you will write side effect tests.

# Puts x and y into output z, then you could write a test as test.testEqual(f(x, y), z). Or, to give a more concrete example, if you have a function square, you could have a test case test.testEqual(square(3), 9)

# It is important to have at least one test for each equivalence class of inputs. For example both positive and negative inputs
# Semantic errors are often caused by improperly handling the boundaries between equivalence classes. The boundary for this problem is zero. It is important to have a test at each boundary.
# Possible paths for testing conditionals and loops

# Testing optional parameters

import test
test.testEqual(sorted([1, 7, 4]), [1, 4, 7])
test.testEqual(sorted([1, 7, 4], reverse=True), [7, 4, 1])

# If you write unit tests before doing the incremental development, you will be able to track your progress as the code passes more and more of the tests. Alternatively, you can write additional tests at each stage of incremental development.
try:
   <try clause code block>
except <ErrorType>:
   <exception handler code block>

# when the error is encountered, the rest of the try block is skipped and the exception block is executed

# The reason to use try/except is when you have a code block to execute that will sometimes run correctly and sometimes not, depending on conditions you can’t foresee at the time you’re writing the code.
try:
    extract_data(d)
except KeyError:
    skip_this_one(d)


ImportError
SyntaxError
TypeError


# Object Oriented Programming
# In object-oriented programming the focus is on the creation of objects which contain both data and functionality together. Usually, each object definition corresponds to some object or concept in the real world and the functions that operate on that object correspond to the ways real-world objects interact.

# To be more specific, we say that an object has a state and a collection of methods that it can perform. 
# The state of an object represents those things that the object knows about itself. The state is stored in instance variables.

# instance variables x and y
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

p = Point(7,6)


# Adding Other Methods
# A method behaves like a function but it is invoked on a specific instance.

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


p = Point(7,6)
print(p.getX())
print(p.getY())


# Pass Objects as arguments and parameters

# Print Method - converting an object as a String
__str__ # for special methods

# Can also return instances as return values
class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)


# Sorting Lists of Instances
L = ["Cherry", "Apple", "Blueberry"]

print(sorted(L, key=len))
#alternative form using lambda, if you find that easier to understand
print(sorted(L, key= lambda x: len(x)))

# When each item is the list is an instance of the class, need to make a function to take instance as an input and output a number
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)

# Class variables and instance variables
# Note that there is an assignment to the variable printed_rep on line 4. It is not inside any method. That makes it a class variable. It is accessed in the same way as instance variables. For example, on line 16, there is a reference to self.printed_rep. If you change line 4, you have it print a different character at the x,y coordinates of the Point in the graph.

# Thinking about classes and instances

# What is the data you want to deal with
# What will one instance of your class represent? In other words, which sort of new thing in your program should have fancy functionality?
# What information should each instance have as instance variables? This is related to what an instance represents
# Each instance represents one < song > and each < song > has an < artist > and a < title > as instance variables.” Or, “Each instance represents a < Tweet > and each < Tweet > has a < user (who posted it) > and < a message content string > as instance variables.”

# What instance methods should each instance have? What should each instance be able to do? 
# What should the printed version of an instance look like? 



# Testing Classes
# To test a user-defined class, you will create test cases that check whether instances are created properly, and you will create test cases for each of the methods as functions, by invoking them on particular instances and seeing whether they produce the correct return values and side effects, especially side effects that change data stored in the instance variables.
# To test whether the class constructor (the __init__) method is working correctly, create an instance and then make tests to see whether its instance variables are set correctly. 

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
	
import test

#testing class constructor (__init__ method)
p = Point(3, 4)
test.testEqual(p.y, 4)
test.testEqual(p.x, 3)

#testing the distance method
p = Point(3, 4)
test.testEqual(p.distanceFromOrigin(), 5.0)

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
test.testEqual(p.x, 1)
test.testEqual(p.y, 7)


from random import randrange

class Pet():
	def __init__(self, name="Kitty"):
		self.name = name
		self.hunger = randrange()
		self.sounds = self.sounds[:]



# Class Inheritance
# You just want to override a few things without having to reimplement everything they’ve done.
from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

# Here's the new definition of class Cat, a subclass of Pet.
class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
    sounds = ['Meow']

    def chasing_rats(self):
        return "What are you doing, Pinky? Taking over the world?!"


# Invoke Superclass Methodology
from random import randrange

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

d1 = Dog("Astro")

d1.feed()

# Update Init Method 
class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

b1 = Bird('tweety', 5)
b1.teach("Polly wanna cracker")
b1.hi()


# Map function
# map takes two arguments, a function and a sequence. The function is the mapper that transforms items. It is automatically applied to each item in the sequence. You don’t have to initialize an accumulator or iterate with a for loop at all.
# map can refer to a function by name or use lambda expression 


things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))


def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

# Filter function
# filter takes two arguments, a function and a sequence. The function takes one item and return True if the item should. It is automatically called for each item in the sequence. You don’t have to initialize an accumulator or iterate with a for loop.
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))



# alternative to do filter and map using list comprehension
[<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]

[x*x for x in range(10) if x%2 ==0]



def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

# Zip
# One more common pattern with lists, besides accumulation, is to step through a pair of lists (or several lists), doing something with all of the first items, then something with all of the second items, and so on. 

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)


L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]

# https://github.com/donnemartin/system-design-primer

# https://github.com/donnemartin/system-design-primer#real-world-architectures



# To learn more about
# dictionary with no initiation 
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

# sort vs. sorted

# loop through and print out those which have bad cumulative properties (i.e. count copies <2)

# argument unpacking
zip * # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
# In place 

# https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

# p142 python notes

# CRUD Operations - created, retrieve, update, delete




