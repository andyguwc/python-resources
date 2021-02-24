##############################################
# Arrays
##############################################

# Print
print("%d. %s appears %d times." % (i, key, wordBank[key]))


# ArrayList and Resizable Arrays
# ArrayList ia dynamic resizing (from Java), the amortized cost is O(1)
# Work backwards at how many elements we copy at each capacity increase. 
# When we increase array to K elements, the array was previously half the size, so we need to copy K/2 elements. Therefore the total number of copies are N/2+N/4+..+1 = O(N)


# Array Tips:
# Write values from the back
# Instead of deleting (which requires all things to move left) consider overwriting it
# When dealing with integers encoded by an array, process the digits from the back
# 2D Arrays, use parallel logic for rows and columns 


[] # indexing - Access an element of a sequence
+  # concatenation - Combine sequences together
*  # repetition - Concatenate a repeated number of times
in # memberhsip - Ask whether an item is in a sequence (O(n) time complexity)
len # length, ask the number of items in the sequence
[:] # slicing, Extract a part of a sequence

# Basic Operations/Methods
alist.append(item) # Adds a new item to the end of a list
alist.insert(i,item) # Inserts an item at the ith position in a list
alist.pop() # Removes and returns the last item in a list
alist.pop(i) # Removes and returns the ith item in a list
alist.sort() # Modifies a list to be sorted
alist.reverse() # Modifies a list to be in reverse order
del alist[i] # Deletes the item in the ith position
alist.index(item) # Returns the index of the first occurrence of item
alist.count(item) # Returns the number of occurrences of item
alist.remove(item) # Removes the first occurrence of item


# list.append is a method that modifies the existing list. It doesn't return a new list -- it returns None, like most methods that modify the list. Simply do aList.append('e') and your list will get the element appended.
list(range(10,1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]

A.reverse() # in place
reversed(A) # returns an iterator 
print(list(reversed([2,3,4])))

A.sort() # in place
sorted(A) # returns a copy

del A[i:j] # removes the slice 

A = [1,6,3,4,5,2,7]
A[2:4] # [3,4]
A[2:] # [3,4,5,2,7]
A[-3:] # [5,2,7]
A[::-1] # reversed list  [7,2,5,4,3,6,1]
A[k:] + A[:k] # rotates A by K to the left

# initiate minimum
float('inf')
import sys
INT_MAX = sys.maxsize  

INT_MIN = -sys.maxsize-1# sys.maxint

# List Comprehension

# List comprehension
# A list comprehension consists of: 1) an input sequence 2) an iterator over input sequence 3) logical condition over iterator 4) an expression that yields the elements

sqlist = []
for x in range(1,11):
    sqlist.append(x**2)
sqlist=[x*x for x in range(1,11) if x%2 != 0]


# List comprehension supports multiple level of looping 
A = [1,3]
B = ['a','b']
[(x,y) for x in A for y in B] # creates [(1,'a'),(1,'b'),(3,'a'),(3,'b')]

# 2D Array Looping
A = [[1,2,3],[4,5,6]] 
# The 
[[x**2 for x in row] for row in A] # yields [[1,4,9], [16,2,5,36]]


print ([ch for ch in "".join(['cat','dog','rabbit'])])
print ([word[i] for word in ['cat','dog','rabbit'] for i in range(len(word))])



# Enumerate
for counter, value in enumerate(some_list):
    print(counter, value)

# Extend
# extend(): Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in it’s argument.

my_list = ['geeks', 'for'] 
another_list = [6, 0, 4, 1] 
my_list.extend(another_list) 
print my_list 

# Zip
# The purpose of zip() is to map the similar index of multiple containers so that they can be used just as a single entity.

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 


# using zip() to map values 
mapped = zip(name, roll_no, marks) 

The zipped result is : {('Shambhavi', 3, 60), ('Astha', 2, 70),
('Manjeet', 4, 40), ('Nikhil', 1, 50)}


zip # which takes two or more sequences and returns a new sequence of tuples, where each tuple contains a single value from each sequence.

contents = "Some file contents"
file = open("filename", "w")
file.write(contents)
file.close()


# Zip
# One more common pattern with lists, besides accumulation, is to step through a pair of lists (or several lists), doing something with all of the first items, then something with all of the second items, and so on. 

L1, L2, L3 = [3, 4, 5], [1, 2, 3], []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]


# Reduce
# performaing operations on a list and return a result
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4]) # Output: 1*2*3*4 = 24


# Instantiate 2D Array
[[1,2,4], [2,3,1]]

# Iterator and Next 
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Default 
x = next(mylist, "orange")

# A major difference between lists and strings is that lists can be modified while strings cannot. 
# This is referred to as mutability. Lists are mutable; strings are immutable.

'''
Shallow Copy and Deep Copy
'''


# A shallow copy means constructing a new collection object and then
# populating it with references to the child objects found in the original.
# In essence, a shallow copy is only one level deep. The copying process
# does not recurse and therefore won’t create copies of the child objects
# themselves.
# A deep copy makes the copying process recursive. It means first constructing
# a new collection object and then recursively populating it
# with copies of the child objects found in the original.

B=A
B=list(A) # a shallow copy

copy.copy(A) 
copy.deepcopy(A)

import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
xs[1][0] = 'X'
>>> xs
[[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
>>> zs
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy
xs[1][0] = 'X'
>>> xs
[[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new sublist']]
>>> ys
[[1, 2, 3], ['X', 5, 6], [7, 8, 9]]



# Filter
# filter creates a list of elements for which a function returns true.

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)



# Two Phases - Forward and Backward 


# Dutch National Flag Problem
# Take an Array A and index i, rearranges the elements that all elements less than A[i] (the pivot) appear first, followed by elements equal to pivot followed by elements greater than pivot

# solve by running two iterations. Group elements smaller than pivot then larger than pivot
def dutch_flag_partition(pivot_index, A):
	pivot = A[pivot_index]
	# First Pass group elements smaller than pivot
	smaller = 0
	for i in range(len(A)):
		if A[i] < pivot:
			A[i], A[smaller] = A[smaller], A[i]
			smaller +=1

	# Second Pass: group elements larger than pivot
	larger = len(A)-1
	for i in reversed(range(len(A))):
		if A[i]< pivot:
			break
		elif A[i]>pivot:
			A[i], A[larger] = A[larger], A[i]
			larger -=1

# Another solution 
# Maintain four subarrays: bottom (smalle than pivot), middle (equal to pivot), unclassified, top (greater)
def dutch_flag_partition(pivot_index, A):
	pivot = A[pivot_index]
	# bottom A[:smaller]
	# middle A[smaller:equal]
	# unclassified A[equal:larger]
	# top A[larger:]
	smaller, equal, larger = 0, 0, len(A)
	while equal < larger:
		if A[equal] < pivot:
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller, equal = smaller+1, equal+1
		elif A[equal] == pivot:
			equal+=1
		else:
			larger-=1
			A[equal], A[larger] = A[larger], A[equal]


# Buy and Sell A Stock Twice 
# Take an array denoting the daily stock price, and returns the maximum profit that could be made by buying and selling one stock twice 
# Approach: Run Two Phases - forward to find price difference then backward to find second sell difference
# For forward phase - keep track of max profit and the min price so far 
def buy_and_sell_stock_twice(prices):
	# Forward phase, record the maximum profit if we sell on that day
	max_total_profit, min_price_so_far = 0, float('inf')
	first_buy_sell_profits = [0]*len(prices)
	for i, price in enumerate(prices):
		min_price_so_far = min(min_price_so_far, price)
		max_total_profit = max(max_total_profit, price - min_price_so_far)
		first_buy_sell_profits[i] = max_total_profit

	# Backward phase, find the maximum profit if we make the second buy on that day
	max_price_so_far = float('-inf')
	for i, price in reversed(list(enumerate(prices[1:],1))):
		max_price_so_far = max(max_price_so_far,price)
		max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i-1])
	return max_total_profit


# Keeping a Boolean Array to Encode the Candidates

# Return All primes up to and including n 
def generate_primes(n):
	primes = []
	# is_prime[p] represents if p is prime or not. Initially set to true. Then eliminate nonprimes
	is_prime = [False, False] + [True]*(n-1)
	for p in range(2, n+1):
		if is_prime[p]:
			primes.append(p)
			for i in range(p, n+1, p):
				is_prime[i] = False
	return primes

# Similarly keep an array to mark if the element has been applied with the change

# Apply a permutation to an array
# Give an array A of n elements and a permutation P, apply P to A

# Key insight is permutation is several rounds of cyclic moves. And the way to tell if that round is over is overwriting permutation as negative 
def apply_permutation(perm, A):
	for i in range(len(A)):
		next = i
		while perm[next]>=0:
			A[i], A[perm[next]] = A[perm[next]], A[i]
			temp = perm[next]
			perm[next] -= len(perm) # indicates the move has performed
			next = temp
	# restore the perm
	perm[:] = [a+len(perm) for a in perm] 



# Compute the next iteration



# Slicing
# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/

def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    M, N = len(haystack), len(needle)
    for i in range(M - N + 1):
        if haystack[i : i + N] == needle:
            return i
    return -1


# Two Pointer Technique
# For example, swapping the elements - one from first the other from the last element and continue until they meet
def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    if len(s) <=1:
        return s
    start = 0
    end = len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start +=1
        end -=1

# Two sum
def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)<=1:
            return None
        left = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]== target:
                return [left+1, right+1]
            if numbers[left]+numbers[right]<target:
                left+=1
            if numbers[left]+numbers[right]>target:
                right-=1


# Reorder entries so that the even entries appear first. Do that in place without allocating additional storage
# Have two pointer, next_even, and next_odd. Partition the array into three parts, even, unclassified, and odd
def even_odd(A):
	next_even, next_odd = 0, len(A)-1
	while next_even < next_odd:
		if A[next_even]%2==0:
			next_even+=1
		else:
			A[next_even], A[next_odd] = A[next_odd], A[next_even]
			next_odd -= 1


# Two Pointer Scenario
# one is still used for the iteration while the second one always points at the position for next addition

# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1173/
def removeDuplicates(self, A):
    if not A:
        return 0

    last = 0
    for i in xrange(len(A)):
        if A[last] != A[i]:
            last += 1
            A[last] = A[i]
    return last + 1





# Array Rotate by K
# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
# https://www.geeksforgeeks.org/array-rotation/


# Takes an input array of digits encoding a nonnegative decimal integer D and updates the array to represent integer D+1
# Solution: iterate from right to left and propogates carries

def plus_one(A):
	A[-1]+=1
	for i in reversed(range(1,len(A))):
		if A[i] != 10:
			break
		A[i] =0
		A[i-1] +=1
	if A[0]==10:
		# a carry out need one more digit to store the result
		A[0]=1
		A.append(0)
	return A




# Reverse Words
def reverseWords(self, s):
        return ' '.join(reversed(s.split()))


def reverseWords(self, s):
    reversed_words = [word[::-1] for word in s.split(' ')]
    return ' '.join(reversed_words)


def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first = 0 # first zero location
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[first], nums[i] = nums[i], nums[first]
                first+=1


# 2D Array
# If valid Sudoku
def is_valid_sudoku(partial_assignment):
	# return true if subarray contains any duplicates otherwise false 
	def has_duplicate(block):
		block = list(filter(lambda x: x!=0, block))
		return len(block) != len(set(block))
	n = len(partial_assignment)
	if any(
		has_duplicate([partial_assignment[i][j] for j in range(n)]) or
		has_duplicate([partial_assignment[j][i] for j in range(n)])
		for i in range(n)):
		return False 

	# check region constraints
	region_size = int(math.sqrt(n))
	return all(not has_duplicate([
		partial_assignment[a][b]
		for a in range(region_size*I, region_size*(I+1))
		for b in range(region_size*J, region_size*(J+1))
		]) for I in range(region_size) for J in range(region_size)
	)

# Spiral Ordering 
# Writing the 2D in spiral order
# Iterate on circles - different offsets
def matrix_in_spiral_order(square_matrix):
	def matrix_layer_in_clockwise(offset):
		if offset == len(square_matrix) - offset -1:
			spiral_ordering.append(square_matrix[offset][offset])
			return
		spiral_ordering.extend(square_matrix[offset][offset:-1-offset])
		spiral_ordering.extend(
			list(zip(*square_matrix))[-1-offset][offset:-1-offset])
		spiral_ordering.extend(
			square_matrix[-1-offset][-1-offset:offset:-1]
			)
		spiral_ordering.extend(
			list(zip(*square_matrix))[offset][-1-offset:offset:-1])

		spiral_ordering = []
		for offset in range((len(square_matrix)+1)//2):
			matrix_layer_in_clockwise(offset)
		return spiral_ordering


# Anther solution with four directions

def matrix_in_spiral_order(square_matrix):

	SHIFT = ((0,1),(1,0),(0,-1),(-1,0))
	direction = x= y = 0
	spiral_ordering = []

	for _ in range(len(square_matrix)**2):
		spiral_ordering.append(square_matrix[x][y])
		square_matrix[x][y] = 0
		next_x, next_y = x+SHIFT[direction][0], y+SHIFT[direction][1]
		if (next_x not in range(len(square_matrix)) or next_y not in range(len(square_matrix)) or square_matrix[next_x][next_y]==0):
			direction = (direction+1) & 3
			next_x, next_y = x+ SHIFT[direction][0], y+ SHIFT[direction][1]
		x, y = next_x, next_y
	return spiral_ordering



# Generate Pascal Rows
def generate_pascal_triangles(n):
	result= [[1]*(i+1) for i in range(n)]
	for i in range(n):
		for j in range(1,i):
			result[i][j] = result[i-1][j-1]+result[i-1][j]
	return result


####### Patterns - Sliding Windows ########


# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any subarray of size ‘k’.

def max_sub_array_of_size_k(k, arr):
  max_sum , window_sum = 0, 0
  window_start = 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]  # subtract the element going out
      window_start += 1  # slide the window ahead
  return max_sum


# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

def smallest_subarray_with_given_sum(s, arr):
  window_sum = 0
  min_length = math.inf
  window_start = 0

  for window_end in range(0, len(arr)):
    window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start + 1)
      window_sum -= arr[window_start]
      window_start += 1
  if min_length == math.inf:
    return 0
  return min_length



# Given a string, find the length of the longest substring in it with no more than K distinct characters.

def longest_substring_with_k_distinct(str, k):
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k:
      left_char = str[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
  return max_length


##############################################
# Strings
##############################################

# String Methods
astring.count(item) # returns the number of occurences of item in string
astring.lower() # a string in all lowercase
astring.ljust(w) # string left adjusted in a field of size w
astring.find(item) # returns the index of the first occurence of item


## all function
## ~ operator: s[~i] for i in [0, len(s)-1] is s[-(i+1)]
def is_palindromic(s):
	return all(s[i] == s[~i] for i in range(len(s)//2))


# strip function
s.strip()
string = '@@@@Geeks for Geeks@@@@@'
# Strip all '@' from begining and ending 
print(string.strip('@'))

# split and join

','.join(('dog', 'cat')) 
''.join(('dog', 'cat')) # return 'dogcat'

'Euclid, Gauss'.split('') # return ['Euclid', ' Gauss']


# Format - string substitution
'Name {name}, Rank {rank}'.format(name='ABC', rank = 3)

str = "This article is written in {}"
print (str.format("Python"))



# String is immutable. s= s[:] simply creates a new array of characters that is then assigned back to s. Updating mutable string 

# convert between int and str
str(n)
int(s)


# Replace and Remove
# Replace each 'a' by 2 'd', and delete each entry containing a 'b'. Input is a string s and size

# solution: first with a forward iteration, we remove 'b' and count the number of 'a'. Then we iterate backwards by replacing 'a' by two 'd'

def replace_and_remove(size,s):
	# forward iteration, skip b
	write_idx, a_count = 0,0
	for i in range(size):
		if s[i] != 'b':
			s[write_idx] = s[i]:
			write_idx+=1
		if s[i] == 'a':
			a_count+=1

	# backward iteration: replacing a with dd from the back
	cur_idx = write_idx-1
	write_idx = a_count-1
	final_size = write_idx+1
	while cur_idx >=0:
		if s[cur_idx]=='a':
			s[write_idx-1:write_idx+1] = 'dd'
			write_idx-=2
		else:
			s[write_idx] = s[cur_idx]
			write_idx-=1
		cur_idx-=1
	return final_size 

# Look and Say Problem 
# n iterations, each depending on previous one. 
# append result if certain criteria met
def look_and_say(n):
	def next_number(s):
		result, i = [], 0
		while i < len(s):
			count = 1
			while i+1 < len(s) and s[i]==s[i+1]:
				i+=1
				count+=1
			result.append(str(count)+s[i])
			i+=1
		return ''.join(result)
	s='1'
	for _ in range(n):
		s = next_number(s)
	return s



# Decoding and Encoding
# 'aaabcc' is '3a1b2c'
# Mix digits and characters 

def decoding(s):
	count, result = 0, []
	for c in s:
		if c.isdigit():
			count=count*10+int(c)
		else:
			result.append(c*count) # append count copies of c to result 
			count=0
	return ''.join(result)

def encoding(s):
	result, count = [], 1
	for i in range(1, len(s)+1):
		if i == len(s) or s[i] != s[i-1]:
			# found new character so write the count of previous character
			result.append(str(count)+s[i-1])
			count =1
		else:
			count+=1
	return ''.join(result)



# Compute all IP Addresses
# basically dividing a string of numbers into 4 parts each of which is between 0 and 255
# Prune the combinations as early as possible

def get_valid_ip_address(s):
	def is_valid_part(s):
		return len(s)==1 or (s[0]!='0' and int(s)<=255)

	result, parts = [], [None]*4
	for i in range(1, min(4, len(s))):
		parts[0] = s[:i]
		if is_valid_part(parts[0]):
			for j in range(1, min(len(s)-i,4)):
				parts[1] = s[i:i+j]
				if is_valid_part(parts[1]):
					for k in range(1, min(len(s)-i-j, 4)):
						parts[2], parts[3] = s[i+j:i+j+k], s[i+j+k:]
						if is_valid_part(parts[2]) and is_valid_part(parts[3]):
							result.append('.'.join(parts))



################################################
# Linked Lists
################################################

# Costs: Inserting and Deleting O(1), while obtaining kth element takes O(n) 
# Unlike the array, we are not able to access a random element in a singly-linked list in constant time. 
# If we want to get the ith element, we have to traverse from the head node one by one. It takes us O(N) time on average to visit an element by index, where N is the length of the linked list.

# The basic building block for the linked list implementation is the node. Each node object must hold at least two pieces of information. First, the node must contain the list item itself. We will call this the data field of the node. 
# In addition, each node must hold a reference to the next node.


class ListNode:
	def __init__(self, data=0, next_node=None):
		self.data = data
		self.next = next_node


# Linked List Methods: search, insert, delete
def search_list(L, key):
	while L and L.data != key:
		L = L.next
	return L

def insert_after(node, new_node):
	new_node.next = node.next
	node.next = new_node

def delete_after(node):
	node.next = node.next.next 


# Implement Traversal, Insertion, Deletion / Analyze Complexity

# Use a dummy head to avoid checking for empty lists

# Can often use two iterators, one advancing quicker than the other



# Implement Linked List
# https://leetcode.com/problems/design-linked-list/

# Implement these functions in your linked list class:

# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.



class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1

# Two Pointer Technique
# Detect LinkedList cycle: fast runner and slow runner will catch up


# Find half way

slow=fast=L
while fast and fast.next:
	fast, slow = fast.next.next, slow.next


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Intersection of Linked Lists
# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0); dummy.next=head
        p1=p2=dummy
        for i in range(n): p1=p1.next
        while p1.next:
            p1=p1.next; p2=p2.next
        p2.next=p2.next.next
        return dummy.next

# 1. Always examine if the node is null before you call the next field. Getting the next node of a null node will cause the null-pointer error. For example, before we run fast = fast.next.next, we need to examine both fast and fast.next is not null.
# 2. Carefully define the end conditions of your loop. Run several examples to make sure your end conditions will not result in an endless loop. And you have to take our first tip into consideration when you define your end conditions.


# Remove Elements

def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head 
        it = res
        while it:
            nextit = it.next
            while nextit and nextit.val == val:
                nextit = nextit.next
            it.next = nextit
            it = nextit
        return res.next



    # recursion
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next
          
# Reverse Linked List

def reverse_list(head):
    new_head = None  # this is where we build the reversed list (reusing the existing nodes)
    while head:
        temp = head  # temp is a reference to a node we're moving from one list to the other
        head = temp.next  # the first two assignments pop the node off the front of the list
        temp.next = new_head  # the next two make it the new head of the reversed list
        new_head = temp
    return new_head

# Shorter version
def reverse_list(head):
    new_head = None
    while head:
        head.next, head, new_head = new_head, head.next, head 
    return new_head


# Reverse Sublist
# first iterate until the start of the sublist then start the reversing process
def reverse_sublist(L, start, finish):
	dummy_head = sublist_head = ListNode(0,L)
	for _ in range(1, start)
	sublist_head = sublist_head.next

	# reverse sublist
	sublist_iter = sublist_head.next
	for _ in range(finish-start):
		temp = sublist_iter.next
		sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
	return dummy_head.next




# Palindrome
# Have a fast pointer essentially at the middle. Then reverse the second half. Compare first half to second half
def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    def reverse_list(head):
        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head # look Ma, no temp vars!
        return new_head
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    first_half, second_half = head, reverse_list(slow)
    while first_half and second_half:
        if first_half.val != second_half.val:
            return False
        first_half, second_half = first_half.next, second_half.next
    return True 


# Doubly Linked List

# Easy to get previous element to delete

# https://www.geeksforgeeks.org/doubly-linked-list/

# Singly vs. Doubly Linked List
# They are similar in many operations:

# Both of them are not able to access the data at a random position in constant time.
# Both of them are able to add a new node after given node or at the beginning of the list in O(1) time.
# Both of them are able to delete the first node in O(1) time.
# But it is a little different to delete a given node (including the last node).

# In a singly linked list, it is not able to get the previous node of a given node so we have to spend O(N) time to find out the previous node before deleting the given node.
# In a doubly linked list, it will be much easier because we can get the previous node with the "prev" reference field. So we can delete a given node in O(1) time.



# Merge LinkedList
# Using recursion

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            l3 = l1
            l3.next = self.mergeTwoLists(l1.next, l2)
        else:
            l3 = l2
            l3.next = self.mergeTwoLists(l1, l2.next)
        return l3        

# Traversing the two lists, choosing the node with the smaller value to continue 
def mergeTwoLists(self,l1,l2):
	dummy_head = tail = ListNode()
	while l1 and l2:
		if l1.data < l2.data:
			tail.next, l1, = l1, l1.next
		else:
			tail.next, l2 = l2, l2.next
		tail = tail.next

	# Append remaining nodes
	tail.next = l1 or l2
	return dummy_head.next 



# Add two Numbers
# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/

# As opposed two length solution http://jelices.blogspot.com/2014/05/leetcode-python-add-two-numbers.html

def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next


# another shorter solution

def addTwoNumbers(self, l1, l2):
	curr = dummey_head = ListNode()
	carry = 0
	while l1 or l2 or carry:
		val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
		l1=l1.next if l1 else None
		l2 =l2.next if l2 else None
		curr.next = ListNode(val%10)
		carry, curr = val//10, curr.next
    return dummy_head = next 


def has_cycle(head):
	fast = slow = head
	while fast and fast.next and fast.next.next:
		slow, fast = slow.next, fast.next.next
		if slow is fast:
			slow = head
			while slow is not fast:
				slow, fast = slow.next, fast.next
			return slow
	return None



# Insert Into a Cyclic Sorted List
# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1226/

def insert(self, node, x):
    # write your code here
    n = ListNode(x)
    if node is None:
        n.next = n
        return n
    prev, curr = node, node.next
    while curr != node:
        if prev.val <= x and curr.val >= x:
            break
        if prev.val > curr.val and (prev.val < x or curr.val > x):
            break
        curr, prev = curr.next, prev.next
    prev.next = n
    n.next = curr
    return node


# Test for overlapping lists - nodes with lists common to both
def overlapping_no_cycle_lists(L1, L2):
	def length(L):
		length = 0
		while L:
			length+=1
			L = L.next
		return length
	L1_len, L2_len = length(L1), length(L2)
	if L1_len > L2_len:
		L1, L2 = L2, L1

	# advance the longer lists to get to equal length lists
	for _ in range(abs(L1_len - L2_len)):
		L2 = L2.next

	while L1 and L2 and L1 is not L2:
		L1, L2 = L1.next, L2.next
	return L1

# Remove Duplicates from a Sorted List
# Traverse and remove successive nodes with the same value as the current node
def remove_duplicates(L):
	it = L
	while it:
		next_distinct = it.next
		while next_distinct and next_distinct.data == it.data:
			next_distinct = next_distinct.next
		it.next = next_distinct
		it = next_distinct
	return L



################################################
# Dictionaries
################################################

# Dictionaries are collections of associated pairs of items where each pair consists of a key and a value. 
# This key-value pair is typically written as key:value. Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces. 
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
capitals['Utah']='SaltLakeCity'
print(capitals)
for k in capitals:
   print(capitals[k]," is the capital of ", k)

myDict[k] # Returns the value associated with k, otherwise its an error
key in adict # Returns True if key is in the dictionary, False otherwise
del adict[key] # Removes the entry from

adict.keys() # Returns the keys of the dictionary in a dict_keys object
adict.values() # Returns the values of the dictionary in a dict_values object
adict.items() # Returns the key-value pairs in a dict_items object
adict.get(k) # Returns the value associated with k, None otherwise
adict.get(k,alt) # Returns the value associated with k, alt otherwise


phoneext={'david':1410,'brad':1137}

list(phoneext.keys())
['brad', 'david']

list(phoneext.values())
[1137, 1410]

list(phoneext.items())
[('brad', 1137), ('david', 1410)]




# Intersection of Two Arrays
def intersect(self, nums1, nums2):
	res = []
    map = {}
    for i in nums1:
        map[i] = map[i]+1 if i in map else 1
    for j in nums2:
        if j in map and map[j] > 0:
            res.append(j)
            map[j] -= 1


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



##############################################
# Hash Table
##############################################

# Hash table is a data structure that maps keys to values for efficient lookup. 

# In a simple implementation use an array of linked lists and a hash code function. 
# 1. Compute the hash code (usually int or long type)
# 2. Map the hash code to an index in the array
# 3. At this index there is a linked list of keys and values. We use a linked list because of collisions

# Alternatively can implement using a BST
# Why implementing hash table using BST https://stackoverflow.com/questions/22996474/why-implement-a-hashtable-with-a-binary-search-tree
# Less space but O(logN) lookup time instead of O(1)



# a data structure to be searched in O(1) time (inserts, deletes, and lookups)
# hasing table - collection of items stored in a way to make it easier to find them later
# load factor = number of items / table size
# two or more items in the same slot - collision

# Collission Resolution
# when two items are hashed to the same slot
# Linear Probing - open addressing - find the next open slot or address in the hash table
# rehash(pos)=(pos+skip)%sizeoftable
# Problem with linear probin is clustering - i.e. if many collisions occur at the same hash value
# Quadratic Probing - where the skip values are quadratic series
# Chaining - as more and more items hash to the same location, the difficulty of searching for the item in the collection increases



# Libraries
set
dict
collections.defaultdict
collections.Counter # returns the default value of the type that was specified when the collection was instantiated
# collections.defaultdict(list)

# to iterate over the key value, iterate over items(), to iterate over values, use values()



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

# Find anagrams
# sort the string as a key and return those with >=2 values 

def find_anagrams(dictionary):
	# sorted string can be used as a key
	sorted_string_to_anagram = collections.defaultdict(list)
	for s in dictionary:
		sorted_string_to_anagram[''.join(sorted(s))].append(s)

	return [group for group in sorted_string_to_anagram.values() if len(group)>=2]


# If it is possible to cover letter using magazine
# solution: store character counts for the letter in a single hash table - (keys are characters, and values are the number of timesit appears)
# then pass over magazine and reduce count by 1 or remove the hash if it goes to 0

def is_letter_from_magaize(letter_text, mag_text):
	char_freq_for_letter = collections.Counter(letter_text)
	for c in mag_text:
		if c in char_freq_for_letter:
			char_freq_for_letter[c]-=1
			if char_freq_for_letter[c] ==0:
				del char_freq_for_letter[c]
				if not char_freq_for_letter:
					return True
	return not char_freq_for_letter

# alternatively using the Counter 
# subtraction only keep keys with positive counts 
def is_letter_from_magaize(letter_text, mag_text):
	return (not collections.Counter(letter_text) - collections.Counter(mag_text))


# Implement an ISBN Cache
# create a cache for looking up prices of books identified b ISBN
# implement lookup, insert, and remove using the Least Used Policy for cache eviction 
class LRUCache: 
	def __init__(self, capacity):
		self._isbn_price_table = collections.OrderedDict()
		self._capacity = capacity

	def lookup(self, isbn):
		if isbn not in self._isbn_price_table:
			return -1
		price = self._isbn_price_table.pop(isbn)
		self._isbn_price_table[isbn] = price
		return price

	def insert(self, isbn, price):
		if isbn in self._isbn_price_table:
			price = self._isbn_price_table.pop(isbn)
		elif self._capacity <=len(self._isbn_price_table):
			self._isbn_price_table.popitem(last=False)
		self._isbn_price_table[isbn] = price

	def erase(self, isbn):
		return self._isbn_price_table.pop(isbn, None) is not None

# Find the nearest repeated entries in an array
# Solution: as we scan through the array, for each value seen so far, we store in a hash table the latest index at which it appears
# when processing the element, we use the hash table to see the latest index less than the current index holding the same value
def find_nearest_repitition(paragraph):
	word_to_latest_index, nearest_repeated_distance = {}, float('inf')
	for i, word in enumerate(paragraph):
		if word in word_to_latest_index:
			latest_equal_word = word_to_latest_index[word]
			nearest_repeated_distance = min(nearest_repeated_distance, i-latest_equal_word)

		word_to_latest_index[word] = i 
	return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1


# Find the longest subarray with distinct entries
# We need a hash table storing the most recent occurence of each element, and the longest duplicate-free subarray ending at the current element

def longest_subarray_distinct(A):
	most_recent_occurence = {}
	longest_subarray_start_idx = result = 0
	for i,a in enumerate(A):
		if a in most_recent_occurence:
			dup_idx = most_recent_occurence[a]
			if dup_idx >= longest_subarray_start_idx:
				result = max(result, i - longest_subarray_start_idx)
				longest_subarray_start_idx = dup_idx+1
		most_recent_occurence[a] = i 
	return max(result, len(A) - longest_subarray_start_idx)



##############################################
# Queue
##############################################

# A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.” 
# As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.

# Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
# enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
# dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
# isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items in the queue. It needs no parameters and returns an integer.



# Implement queue using Stack
# https://www.geeksforgeeks.org/queue-using-stacks/


# Impelment stack using queue
# https://www.geeksforgeeks.org/implement-stack-using-queue/


# Design Circular Queue
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/design-circular-queue.py
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.__start = 0
        self.__size = 0
        self.__buffer = [0] * k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.__buffer[(self.__start+self.__size) % len(self.__buffer)] = value
        self.__size += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.__start = (self.__start+1) % len(self.__buffer)
        self.__size -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.__buffer[self.__start]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.__buffer[(self.__start+self.__size-1) % len(self.__buffer)]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.__size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.__size == len(self.__buffer)



# Template BFS and DFS
# https://www.cnblogs.com/zuoyuan/p/3753507.html


# Cloned Graph
# Using a lookup map to replace the visited label 

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @BFS
    def cloneGraph(self, node):
        def dfs(input, map):
            if input in map:
                return map[input]
            output = UndirectedGraphNode(input.label)
            map[input] = output
            for neighbor in input.neighbors:
                output.neighbors.append(dfs(neighbor, map))
            return output
        if node == None: return None
        return dfs(node, {})

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @BFS
    def cloneGraph(self, node):
        if node == None: return None
        queue = []; map = {}
        newhead = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = newhead
        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    copy = UndirectedGraphNode(neighbor.label)
                    map[curr].neighbors.append(copy)
                    map[neighbor] = copy
                    queue.append(neighbor)
                else:
                    # turn directed graph to undirected graph
                    map[curr].neighbors.append(map[neighbor])
        return newhead


# Deque (or double-ended queue)
# A doubly linked list in which all insertions and deletions are from one of the two ends of the list (at the head or the tail)

# The deque abstract data type is defined by the following structure and operations. A deque is structured, as described above, as an ordered collection of items where items are added and removed from either end, either front or rear. The deque operations are given below.


# Libraries
q.append(e) # push the element onto the queue
q[0] # retrieve but not remove the element at the front
q.popleft() # remove and return element at the front of the queue


class Queue:
	def __init__(self):
		self._data = collections.deque()

	def enqueue(self,x):
		self._data.append(x)

	def dequeue(self):
		return self._data.popleft()

	def max(self):
		return max(self.data)


# Print binary trees in the same level
# Use a queue of nodes to store nodes at depth i and queue of nodes at depth i+1. 
def binary_tree_depth_order(tree):
	result, curr_depth_nodes = [], collections.deque([tree])
	while curr_depth_nodes:
		next_depth_nodes, this_level = collections.deque([]),[]
		while curr_depth_nodes:
			curr = curr_depth_nodes.popleft()
			if curr:
				this_level.append(curr.data)
			# defer the null checks to the null test above
			next_depth_nodes = [curr.left, curr.right]
		if this_level:
			result.append(this_level)
		curr_depth_nodes = next_depth_nodes
	return result 


# https://leetcode.com/problems/moving-average-from-data-stream/

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.moveSize = size
        self.items = deque()
        self.sum = 0
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.items) == self.moveSize:
            self.sum -= self.items.popleft()
        self.items.append(val)
        self.sum += val
        return 1.0*self.sum/len(self.items)



# Implement a Queue using Stacks
# Keep two stacks - one for enqueue, one for dequeue

class Queue:
	def __init__(self):
		self._enq, self._deq = [], []

	def enqueue(self, x):
		self._enq.append(x)

	def dequeue(self):
		if not self._deq:
			while self._enq:
				self._deq.append(self._enq.pop())

		if not self._deq:
			raise IndexError('empty queue')
		return self._deq.pop()


# Implement Queue with Max API
# Maintain a separate queue with elements such that no elements after is larger

class QueueWithMax:
	def __init__(self):
		self._entries = collections.deque()
		self._candidates_for_max = collections.deque()

	def enqueue(self, x):
		self._entries.append(x)
		while self._candidates_for_max and self._candidates_for_max[-1]<x:
			self._candidates_for_max.pop()
		self._candidates_for_max

	def dequeue(self):
		if self._entries:
			result = self._entries.popleft()
			if result == self._candidates_for_max[0]:
				self._candidates_for_max.popleft()
			return result
		raise IndexError('empty queue')

	def max(self):
		if self._candidates_for_max:
			return self._candidates_for_max[0]
		raise IndexError('empty queue')




##############################################
# Stack
##############################################
# A stack is structured, as described above, as an ordered collection of items where items are added to and removed from the end called the “top.” Stacks are ordered LIFO. 
# Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack. 
# push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
# pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
# peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
# isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items on the stack. It needs no parameters and returns an integer.

# Costs
# When implemented using Linked lsit the pop and push operations have O(1) time complexity. 
# If implemented using an array, there is maximum number of entries it can have - push and pop still O(1)
# If array is dynamically resized, the amortized time for both push and pop is O(1)


# Stack libraries - can just use the built in list type
s.append(e)
s[-1] # retrieves last element but does not remove
s.pop() # remove and return element at the top of stack
len(s) == 0 # test if empty

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items ==[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)



# Last in first out nature of a stack makes it useful for creating reverse iterators for sequences which are stored in a way
# that would make it difficult to step back from a given element. Use a stack to print entries of a linked list in reverse order

def print_linked_list_in_reverse(head):
	nodes = []
	while head:
		nodes.append(head.data)
		head = head.next
	while nodes:
		print(nodes.pop())


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


# MinStack


# initialize your data structure here
      
    def __init__(self):
    	self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        pre_min = sys.maxint if len(self.stack) == 0 else self.stack[-1][1]
        cur_min = min(x, pre_min)
        self.stack.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

# Using Named Tupples
# Max Stack
# Push on a tuple with both the element and the max seen so far 

class Stack:
	ElementWithCacheMax = collections.namedtuple('ElementWithCachedMax', ('element','max'))
	def __init__(self):
		self._element_with_cached_max = []

	def empty(self):
		return len(self._element_with_cached_max) == 0

	def max(self):
		if self.empty():
			raise IndexError('max(): empty stack')
		return self._element_with_cached_max[-1].max

	def pop(self):
		if self.empty():
			raise IndexError('pop(): empty stack')
		return self._element_with_cached_max.pop().element

	def push(self, x):
		self._element_with_cached_max.append(
			self.ElementWithCachedMax(x,x if self.empty() else max(x,self.max())))


# Reverse Polish Notation
# Intermediate results are added and removed in last-in, first out order which makes stack a natural data structure

def evaluate(RPN_expression):
	intermediate_results = []
	DELIMITER = ','
	OPERATORS = {
		'+': lambda y, x: x+y,
		'-': lambda y, x: x-y,
		'*': lambda y, x: x*y,
		'/': lambda y, x: int(x/y)
	} # mapping symbols to functions

	for token in RPN_expression.split(DELIMITER):
		if token in OPERATORS:
			intermediate_results.append(
				OPERATORS[token](
					intermediate_results.pop(),
					intermediate_results.pop()))
		else:
			intermediate_results.append(int(token))
	return intermediate_results[-1]

# Well Formed Parentesis

def is_well_formed(s):
	left_chars, lookup = [], {'(':')', '{':'}', '[':']'}
	for c in s:
		if c in lookup:
			left_chars.append(c)
		elif not left_chars or lookup[left_chars.pop()] != c:
			return False
	return not left_chars




# Daily Temperatures
# https://blog.csdn.net/fuxuemingzhu/article/details/79285081

def dailyTemperatures(self, T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    # append (i,t) to stack. Since it depends on future items, stack is a better structure
      
    if len(T)==0:
        return 0
    res = [0]*len(T)
    stack = []
    for i,t in enumerate(T):
        while stack and stack[-1][1] < t:
            idx = stack.pop()[0]
            res[idx] = i-idx
        stack.append((i,t))
            
    return res





################################################
# Binary Trees
################################################

# In a list of lists tree, we will store the value of the root node as the first element of the list. 
# The second element of the list will itself be a list that represents the left subtree. 
# The third element of the list will be another list that represents the right subtree. 

class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

# Depth of a node n is the number of nodes on the search path from the root to n. Height of a tree is the maximum depth of any node in the tree

# Traversing trees (time complexity O(n) and space complexity O(log n))
# traverse left subtree, visit root, traverse right subtree (in order)
# visit root, traverse left, traverse right (preorder)
# traverse left, traverse right, visit root (postorder)


# Height balanced - for each node in the tree, the difference in left subtree and right subtree is at most one


# Using named tuples to store results and call recursion on left or right 
# check if a tree is balanced 
# using a hash to store the results, realizing that once a subtree is done, don't need result from its subtrees

def is_balanced_binary_tree(tree):
	BalancedStatus = collections.namedtuple('BalancedStatus',('balanced','height'))
	def check_balanced(tree):
		if not tree:
			return BalancedStatus(True, -1)
		left_result = check_balanced(tree_left)
		if not left_result.balanced:
			return BalancedStatus(False, 0)

		right_result = check_balanced(tree_right)
		if not right_result.balanaced:
			return BalancedStatus(False, 0)

		is_balanced = abs(left_result.height - right_result.height) <=1
		height = max(left_result.height, right_result.height)+1
		return BalancedStatus(is_balanced, height)
	return check_balanced(tree).balanced



# Find LCAs of two nodes
# Instead of simply returning a Boolean indicating both nodes are in that subtree, we return an object with two fields -
# first is an integer indicating how many of the two nodes were present in that subtree, the second is their LCA, if both nodes are present

def lca(tree, node0, node1):
	Status = collections.namedtuple('Status',('num_target_nodes','ancestor'))
	def lca_helper(tree, node0, node1):
		if not tree:
			return Status(0,None)

		left_result = lca_helper(tree.left, node0, node1)
		if left_result.num_target_nodes == 2:
			return left_result
		right_result = lca_helper(tree.right, node0, node1)
		if right_result.num_target_nodes == 2:
			return right_result
		num_target_nodes = (
			left_result.num_target_nodes + right_result.num_target_nodes + int(tree is node0) + int(tree is node1)
			)
		return Status(num_target_nodes, tree if num_target_nodes==2 else None)
	return lca_helper(tree, node0, node1).ancestor



# Find LCA assuming has a pointer to parent
# First make sure both nodes have the same height

def lca(node_0, node_1):
	def get_height(node):
		depth = 0
		while node:
			depth+=1
			node.node.parent
		return depth

	depth_0, depth_1 = get_depth(node_0), get_depth(node_1)

	if depth_1>depth_0:
		node_0, node_1 = node_1, node_0

	# ascends from the deeper node
	depth_diff = abs(depth_0-depth_1)
	while depth_diff:
		node_0 = node_0.parent
		depth_diff-=1

	# now ascends both nodes until we reach the LCA	
	while node_0 is not node_1:
		node_0, node_1 = node_0.parent, node_1.parent
	return node_0

# Implement in order traversal without recursion 

def bst_in_sorted_order(tree):
	s, result = [], []
	while s or tree:
		if tree: 
			s.append(tree)
			tree = tree.left 
		else:
			tree = s.pop()
			result.append(tree.data)
			tree=tree.right
	return result

def preorder_traversal(tree):
	path, result = [tree], []
	while path:
		curr = path.pop()
		if curr:
			result.append(curr.data)
			path += [curr.right, curr.left]
	return result 


myTree = ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
     ]

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    
################################################
# Heaps
################################################

# Heap is a specialized binary tree
# Heap property (max heap) - the key at each node >= keys stored at its children
# Supports O(logn) insertions, O(1) max lookup and O(logn) deletions of the max element. Searching for arbitrary key has O(n) complexity
# After deletion of max of the heap, deletion is performed by replacing the root's key with the key at the last leaf and recovering heap property by repeatedly exchanging keys with children

# Good choice when you need to compute the k largest or k smallest elements in a collection


# Heapq library
# Only provides min-heap functionality. If need max heap, insert the negatives 
heapq.heapify(L) # transforms the elements in L into a heap in-place
heapq.nlargest(k, L) # returns the k largest or heapq.nsmallest which returns the smallest elements
heapq.heappush(h, e) # which pushes a new element onto the heap
heapq.heappop(h) # which pops the smallest element form the heap
heapq.heappushpop(h,a) # which pushes on the heap and then pops and returns the smalles element
e = h[0] # which returns the smallest without popping it



# Compute k longest strings in a stream
def top_k(k, stream):
	min_heap = [(len(s),s) for s in itertools.islice(stream, k)]
	heapq.heapify(min_heap)
	for next_string in stream:
		heapq.heappushpop(min_heap, (len(next_string),next_string))
	return [p[1] for p in heapq.nsmallest(k, min_heap)]



# Merge sorted files
# Maintain a min heap and always return the smallest number
# The heap needs both the number and which file (iterator) it's from

def merge_sorted_arrays(sorted_arrays):
	min_heap = []
	sorted_array_iters = [iter(x) for x in sorted_arrays]

	# put first element from each iterator in min_heap
	for i, it in enumerate(sorted_array_iters):
		first_element = next(it, None)
		if first_element is not None:
			heap.heappush(min_heap, (first_element,i))

	result = []
	while min_heap:
		smallest_entry, smallest_array_i = heapq.heappop(min_heap)
		smallest_array_iter = sorted_array_iters[smallest_array_i]
		result.append(smallest_entry)
		next_element = next(smallest_array_iter, None)
		if next_element is not None:
			heapq.heappush(min_heap, (next_element, smallest_array_i))
	return result

# same as heapq merge
def merge_sorted_arrays(sorted.arrays):
	return list(heapq.merge(*sorted_arrays))


# Sort an almost sorted array
# Each number is at most k away from its correctly sorted position
# Solution: maintain a min heap of size k and always pop the smallest one

def sort_almost_array(sequence, k):
	result = []
	min_heap = []

	# add first k elements, stop if there are fewer than k
	for x in itertools.islice(sequence, k):
		heapq.heappush(min_heap, x)

	# for every new element, add it to min_heap and extract the smallest 
	for x in sequence:
		smallest = heapq.heappushpop(min_heap, x)
		result.append(smallest)

	# if sequence is exhausted
	while min_heap:
		smallest = heapq.heappop(min_heap)
		result.append(smallest)

	return result 


# Find k closest stars to earth 
# Solution: keep a set of candidates and iteratively update the candidate set. The candidates are the k closest stars seen so far


class Star:
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z

	@property
	def distance(self):
		return math.sqft(self.x**2+self.y**2+self.z**2)

	def __lt__(self, rhs):
		return self.distance < rhs.distance


def find_closest_k_stars(stars, k):
	max_heap = []
	for star in stars:
		# add each star to max_heap. If max_heap size exceeds k, remove the maximum element to the max_heap
		# insert negative tuple to sort in reversed order 
		heapq.heappush(max_heap, (-star.distance, star))
		if len(max_heap) ==k+1:
			heapq.heappop(max_heap)

	return [s[1] for s in heapq.nlargest(k, max_heap)]




################################################
# Searching
################################################


# Squential Search
def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(list) and not found:
        if alist[pos] == item:
            found = True
        else: 
            pos = pos+1
    return found

# Binary Search
def binarySearch(alist, item):
    first = 0
    last = len(alist) -1
    found = False
    
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else: 
            if item < alist[midpoint]:
                last = midpoint - 1
            else: first = midpoint+1
    return found

# Another implementation of binary search - divide and conquer
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))


################################################
# Binary Search 
################################################
# bisect library
bisect.bisect_left(a,x) # returns the index of the first entry that is greater than or equal to the targeted value. If all less than x, return len(a)
bisect.bisect_right(a,x) # returns first element that is greater than a targeted value 

"""
Terminology used in Binary Search:

Target - the value that you are searching for
Index - the current location that you are searching
Left, Right - the indicies from which we use to maintain our search Space
Mid - the index that we use to apply a condition to determine if we should search left or right
"""

# If collection is unordered, we should sort first

def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helperSearch(nums, start, end, target):
            if len(nums)==0:
                return -1
            if start > end:
                return -1
            midx = (start+end)//2
            midvalue = nums[midx]
            if nums[midx] == target:
                return midx
            elif midvalue > target:
                return helperSearch(nums, start, midx-1, target)
            else:
                return helperSearch(nums, midx+1, end, target)
        return helperSearch(nums, 0, len(nums)-1, target)


# return index of the first occurence of the key
# maintain a set of candidates solutions. Think about each conditional the set of candidates remained

def search_first_of_k(A, k):
	left, right, result = 0, len(A)-1, -1
	while left <= right:
		mid = (left+right)//2
		if A[mid] > k:
			right = mide -1
		elif A[mid] == k:
			result = mid
			right = mid -1
		else:
			left = mid+1
	return result 



# Template #1 is used to search for an element or condition which can be determined by accessing a single index in the array.

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

# Template I 
def binarySearch(nums, target):
	if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

# Template II

# Search Condition needs to access element's immediate right neighbor. Use element's right neighbor to determine if condition is met and decide whether to go left or right
# Gurantees Search Space is at least 2 in size at each step
# Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) -1 and nums[left] == target:
        return left
    return -1


def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        left, right = 1, n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid) == True:
                right = mid
            if isBadVersion(mid) == False:
                left = mid+1
        if isBadVersion(left)==True:
            return left
        else:
            return left+1
# Template III
# It is used to search for an element or condition which requires accessing the current index and its immediate left and right neighbor's index in the array.

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1


# Search for a range
# https://www.cnblogs.com/zuoyuan/p/3775904.html
 def searchRange(self, A, target):
        left = 0; right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                list = [0, 0]
                if A[left] == target: list[0] = left
                if A[right] == target: list[1] = right
                for i in range(mid, right+1):
                    if A[i] != target: list[1] = i - 1; break
                for i in range(mid, left-1, -1):
                    if A[i] != target: list[0] = i + 1; break
                return list
        return [-1, -1]


# 2D search
# rows and columns are nondecreasing, check whether the targeted number appears

# search path: starts from top right and either moves left or moves down
def matrix_search(A, x):
	row, col = 0, len(A[0])-1 # start from the top right corner
	while row < len(A) and col >=0:
		if A[row][col] == x:
			return True
		elif A[row][col] < x:
			row+=1
		else:
			col -=1
	return False



##############################################
# BFS
##############################################

# First in first out: Queue
# Last in first out: Stack


# Implementing Circular Queue
# https://www.pythoncentral.io/circular-queue/

# Queue and BFS
# In the first round, process the root node
# In the second round, process the nodes next to the root node
# Processing order is exact the same as how they were added to the queue


# BFS template
# Node will be actual node or status
# Edge will be an actual edge or a possible transition

# BFS explore all from start


def bfs(graph, root):
    visited, queue = [], [root]
    while queue:
        vertex = queue.pop(0)
        for w in graph[vertex]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

graph = {0: [1, 2], 1: [2], 2: []}
bfs(graph, 0)


# https://leetcode.com/explore/featured/card/queue-stack/231/practical-application-queue/1373/
# BFS Solution

def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: None Do not return anything, modify rooms in-place instead.
    """
    INF = 2147483647
    if len(rooms) == 0:
        return rooms
    
    #add all gates to a queue
    queue = []
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                queue.append((i,j))
    
    while queue:
        (i, j) = queue.pop(0)
        for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] == INF:
                rooms[I][J] = rooms[i][j] + 1
                queue.append((I, J)) 

# Lock 
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/open-the-lock.py
def openLock(self, deadends, target):
    """
    :type deadends: List[str]
    :type target: str
    :rtype: int
    """
    
    def neighbors(node):
        res = []
        for i in xrange(4):
            x = int(node[i])
            for d in (-1, 1):
                y = (x + d) % 10
                res.append(node[:i] + str(y) + node[i+1:])
        return res

    dead = set(deadends)
    queue = collections.deque([('0000', 0)])
    seen = {'0000'}
    while queue:
        node, depth = queue.popleft()
        if node == target: return depth
        if node in dead: continue
        for nei in neighbors(node):
            if nei not in seen:
                seen.add(nei)
                queue.append((nei, depth+1))
    return -1


# BFS finding shortest path from start to end
# https://codereview.stackexchange.com/questions/193410/breadth-first-search-implementation-in-python-3-to-find-path-between-two-given-n

# https://blog.csdn.net/fuxuemingzhu/article/details/82703064


graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [10],
    4: [7, 8],
    5: [9, 10],
    7: [11, 12],
    11: [13]
}


def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            visited.add(vertex)


print bfs(graph, 1, 13)


# Perfect Squares
# https://leetcode.com/problems/perfect-squares/discuss/71475/short-python-solution-using-bfs


# Dequeue() in Python
# https://www.geeksforgeeks.org/deque-in-python/


# Flood Fill BFS

# https://blog.csdn.net/fuxuemingzhu/article/details/79401716
def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        queue = deque()
        queue.append((sr,sc))
        visited = {(sr,sc)}
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            currx, curry = queue.popleft()
            visited.add((currx,curry))
            image[currx][curry] = newColor
            for d in directions:
                newx, newy = currx+d[0], curry+d[1]
                if 0<=newx<len(image) and 0 <= newy<len(image[0]) and image[newx][newy] == oldColor and (newx,newy) not in visited:
                    queue.append((newx,newy))
        return image

# Flood Fill DFS
def floodFill(self, image, sr, sc, newColor):
	SR, SC = len(image), len(image[0])
	        color = image[sr][sc]
	        if color == newColor: return image
	        def dfs(r, c):
	            if image[r][c] == color:
	                image[r][c] = newColor
	                if r >= 1: dfs(r - 1, c)
	                if r < SR - 1: dfs(r + 1, c)
	                if c >= 1: dfs(r, c - 1)
	                if c < SC - 1: dfs(r, c + 1)
	        dfs(sr, sc)
	        return image

# Keys and Rooms
# https://leetcode.com/explore/featured/card/queue-stack/239/conclusion/1391/


def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) == 0:
            return False 
        queue = collections.deque()
        visited = set()
        queue.append(0)
        visited.add(0)
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            for neighbor in rooms[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
        if len(visited) >= len(rooms):
            return True
        return False
    
    # DFS Approach
#     def canVisitAllRooms(self, rooms):
#         """
#         :type rooms: List[List[int]]
#         :rtype: bool
#         """
#         visited = [0] * len(rooms)
#         self.dfs(rooms, 0, visited)
#         return sum(visited) == len(rooms)
        
#     def dfs(self, rooms, index, visited):
#         visited[index] = 1
#         for key in rooms[index]:
#             if not visited[key]:
#                 self.dfs(rooms, key, visited)
##############################################
# DFS 
##############################################

# Stack
# Last in Last Out
# Newest element added to the stack will be processed first

# DFS Using Stack
def dfs(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path


adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(dfs(adjacency_matrix, 1))


stack, path = [start], []

# [1, 3, 5, 6, 7, 2, 4]
# Find path given source to destination
# https://www.geeksforgeeks.org/find-paths-given-source-destination/

# https://www.geeksforgeeks.org/find-number-of-islands/
# https://leetcode.com/problems/open-the-lock/discuss/262165/Python-using-numbers-instead-of-strings


# Number of Islands (Connected Components)
# https://leetcode.com/explore/featured/card/queue-stack/231/practical-application-queue/1374/

def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, row, col, x, y):
            if grid[x][y] == '0':
                return 
            grid[x][y] = '0'

            if x != 0:
                dfs(grid, row, col, x - 1, y)
            if x != row - 1:
                dfs(grid, row, col, x + 1, y)
            if y != 0:
                dfs(grid, row, col, x, y - 1)
            if y != col - 1:
                dfs(grid, row, col, x, y + 1)
        
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1':
                    dfs(grid, row, col, i, j)
                    count += 1
        return count



# Another Solution
# https://www.geeksforgeeks.org/find-number-of-islands/





################################################
# Sorting
################################################
# The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. 
# In essence, each item “bubbles” up to the location where it belongs.


# Naive sorting in O(n2) time. Heapsort, mergesort and quicksort run in O(nlogn) time.
# Heapsort is in-place but not stable; merge sort is stable but not in-place, quicksort runs in O(n^2) in worst case
# An in place sort uses O(1) space and a stable sort is one where entries are equal appear in original order

# Heaps are helpful in sorting algorithms - supports O(logn) inserts O(logn) deletes and O(1) time lookup

# Most library sorting functions are based on quicksort which has O(1) space complexity

# Implement sorting routine - consider using a data structure like a BST, heap, or array indexed by values 


# Sort library
# to sort a list in place, use sort(); to sort an iterable, use the function sorted()
sort(key=None, reverse = False)
s.sort(key = lambda x: str(x)) # make sorting key a function which maps 

sorted() # take an iterable and return a new list containing all items from the iterable in ascending order


# Intersect two sorted arrays
def intersect_two_sorted_arrays(A,B):
    res = []
    i, j = 0,0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i==0 or A[i] != A[i-1]:
                res.append(A[i])
            i+=1
            j+=1
        elif A[i] < B[j]:
            i+=1
        else:
            j+=1
    return res


# Merge two sorted arrays
# One array has enough empty entries at its end and can be used to store the combined entries of the two arrays
# Solution: to not shift all entries, start from the end

def merge_two_sorted_arrays(A,m,B,n):
	a,b, write_idx = m-1, n-1, m+n-1
	while a>=0 and b>=0:
		if A[a] > B[b]:
			A[write_idx] = A[a]
			a-=1
		else:
			A[write_idx] = B[b]
			b-=1
		write_idx-=1
	while b>=0:
		A[write_idx] = B[b]
		write_idx, b = write_idx-1, b-1


# If A if less than B for all entries
class Team:
	Player = collectinos.namedtuple('Player', ('height'))

	def __init__(self, height):
		self._players = [Team.Player(h) for h in height]

	# checks if A can be placed in front of B
	@staticmethod
	def valid_placement_exists(A, B):
		return all(a<b
			for a, b in zip(sorted(A._players), sorted(B._players)))



# Remove first name duplicates
# Define comparison

def __init__(self, first_name, last_name):
	self.first_name, self.last_name = first_name, last_name

def __eq__(self, other):
	return self.first_name == other.first_name

def __lt__(self, other):
	return (sefl.first_name < other.frist_name if self.first_name != other.first_name else
			self.last_name < other.last_name 
		)

def eliminate_duplicate(A):
	A.sort()
	write_idx = 1
	for cand in A[1:]:
		if cand != A[write_idx-1]:
			A[write_idx] = cand
			write_idx+=1
	del A[write_idx:]


# Bubble Sort
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

# Insertion Sort
# The insertion sort, although still O(n2)O(n2), works in a slightly different way. It always maintains a sorted sublist in the lower positions of the list. 
# Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
    while position>0 and alist[position-1]>currentvalue:
        alist[position]=alist[position-1]
        position = position-1
    alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

# Merge Sort
# Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). 
# If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)



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



################################################
# Binary Search Trees
################################################

# Efficiently search for a key, find the min and max elements, look for successor/predecessor of a search key, and enumerate keys in a range in sorted order

# BST property: the key stored at a node is greater than or equal to the keys stored at the nodes of left subtree and less than or equal to the keys stored in the nodes of right subtree
# Red black trees are widely used in data structure libraries 


# using bintrees module (RBTree)

# some problems require a combination of BST and a hashtable



class BSTNode:
	def __init__(self, data=None, left=None, right =None):
		self.data, self.left, self.right = data, left, right

# check if a value is present in a BST
def search_bst(tree, key):
	return (tree if not tree or tree.data == key else search_bst(tree.left, key) 
		if key<tree.data else search_best(tree.right, key))


# Check if satisfying the BST property

def is_binary_tree_bst(tree, low_range = float('-inf'), high_range = float('inf')):
	if not tree:
		return True
	elif not low_range <= tree.data <= high_range:
		return False
	return (is_binary_tree_bst(tree.left, low_range, tree.data) and
			is_binary_tree_bst(tree.right, tree.data, high_range))


def is_binary_tree_bst(tree):
	QueueEntry = collections.namedtuple('QueueEntry', ('node','lower','upper'))

	bfs_queue = collections.deque(
		[QueueEntry(tree, float('-inf'), float('inf'))])

	while bfs_queue:
		front = bfs_queue.popleft()
		if front.node:
			if not front.lower <= font.node.data <= front.upper:
				return False
			bfs_queue += [
				QueueEntry(front.node.left, front.lower, front.node.data),
				QueueEntry(front.node.right, front.node.data, front.upper)
			]
	return True


# Find first key that's greater than a value
# Solution: candidates, if subtree's key is greater than input, then search the left subtree, and update the result to root, otherwise search right

def find_first_greater_than_k(tree, k):
	subtree, first_so_far = tree, None
	while subtree:
		if subtree.data >k:
			first_so_far, subtree = subtree, subtree.left 
		else:
			subtree=subtree.right

# Find k largest keys

def find_k_largest_in_bst(tree, k):
	def find_k_largest_in_bst_helper(tree):
		if tree and len(k_largest_elements)<k:
			find_k_largest_in_bst_helper(tree.right)
			if len(k_largest_elements) <k:
				k_largest_elements.append(tree.data)
				find_k_largest_in_bst_helper(tree.left)
	
	k_largest_elements = []
	find_k_largest_in_bst_helper(tree)
	return k_largest_elements



################################################
# Recursion
################################################

# https://leetcode.com/explore/learn/card/recursion-i/

# 1. A simple base case (or cases) — a terminating scenario that does not use recursion to produce an answer.
# 2. A set of rules, also known as recurrence relation that reduces all other cases towards the base case.

# Reverse String In Place Recursion
def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    def helper(start, end, ls):
        if start >= end:
            return
    
        # swap the first and last element
        ls[start], ls[end] = ls[end], ls[start]        

        return helper(start+1, end-1, ls)

    helper(0, len(s)-1, s)
            
# Swap Nodes in Pairs

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if (head is not None and head.next is not None):
        A = head
        B = head.next
        C = head.next.next
        B.next = A
        A.next = self.swapPairs(C)
        return B 
    else:
        return head

# Reverse LinkedList

def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if (head is not None and head.next is not None):
        A = head
        B = head.next
        C = self.reverseList(B)
        A.next = None
        B.next = A
        return C
    else:
        return head 


# Memoization
# Store the intermediate results so we can use them later
# Use a hash table to keep track of all results of F(n)
def fib(self, N):
	cache = {}
	def recur_fib(N):
		if N in cache:
			return cache[N]
		elif N < 2:
			result = N
		else:
			result = recur_fib(N-1) + recur_fib(N-2)
		cache[N] = result
		return result
    return recur_fib(N)


def fib(self,N):
	cache ={}
	if N in cache:
		return cache[N]
	elif N <2:
		result = N
	else:
		result = self.fib(N-1) + self.fib(N-2)
		cache[N] = result
	return result

# Stack allocated to a program reaches its space limit
# Stackoverflow

# The non-recursion related space refers to the memory space that is not directly related to recursion, which typically includes the space (normally in heap) that is allocated for the global variables.

def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n<=2:
                return n
            else:
                dp = [0]*(n+1)
                dp[1] = 1
                dp[2] = 2
                for i in range(3,n+1):
                    dp[i] = dp[i-1]+dp[i-2]
            return dp[n]


# Implement pow(x, n), which calculates x raised to the power n (xn).

 def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        elif n<0:
            return 1/self.myPow(x,-n)
        else:
            m = n//2
            temp = self.myPow(x,m)
            if n%2==0:
                return temp*temp
            else:
                return temp*temp*x


# Apply memoization 
# Tail recursion

# Unique Binary Search Trees
def generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    if n==0:
        return []
    else:
        return self.helper(1, n)

def helper(self, start, end):
    if start > end:
        return [None]
    res = []
    for current_root in range(start, end+1):
        leftTree = self.helper(start, current_root-1)
        rightTree = self.helper(current_root+1, end)
        for i in leftTree:
            for j in rightTree:
                root = TreeNode(current_root)
                root.left = i
                root.right = j
                res.append(root)
    return res



##############################################
# Dynamic Programming
##############################################

# https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/

# https://leetcode.com/problems/pascals-triangle/solution/
def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle


# https://blog.csdn.net/fuxuemingzhu/article/details/80484450

def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # use DP 
        length = len(nums)
        dp = [collections.defaultdict(int) for _ in range(length + 1)] 
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        return dp[length][S]



# default dict

d = defaultdict(int)
for word in words:
    firstletter = word[0].lower()
    d[firstletter] += 1

# same as 
d = {}
for word in words:
    firstletter = word[0].lower()
    if firstletter not in d:
        d[firstletter] = 0
    d[firstletter] += 1









################################################
# Big O Notation
################################################

# http://bigocheatsheet.com/




################################################
# Python Object Oriented Programming
################################################



# Classes

# We define a new class by providing a name and a set of method definitions that are syntactically similar to function definitions
# The first method that all classes should provide is the constructor. The constructor defines the way in which data objects are created. 
# To create a Fraction object, we will need to provide two pieces of data, the numerator and the denominator.
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    def show(self):
     print(self.num,"/",self.den)
    
    def __str__(self):
        return str(self.num)+"/"+str(self.den) # overriding the str method
    
    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    
    def __eq__(self, other):
    firstnum = self.num * other.den
    secondnum = other.num * self.den
    return firstnum == secondnum

myfraction = Fraction(3,5)
Fraction.show(myfraction)



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



# Exceptions

# The class extends the list and override the append method to check conditions that the method is an even integer

class EvenOnly(list):
	def append(self, integer):
		if not isinstance(integer, int):
			raise TypeError("only integers can be added")
		if integer%2:
			raise ValueError("Only even numbers can be added")
		super.append(integer)


def funny_division(divider):
	try:
		return 100/divider
	except ZeroDivisionError:
		return "zero division is not great"

print(funny_division(0))
print(funny_division(50))


# Use finally: the code if always called

# Exception Hierarchy
- BaseException
	- SystemExit
	- KeyboardInterrupt
	- Exception
		- other exceptions 

# Define own exceptions by inheriting from the Exceptions class

class InvalidAction(Exception):
	pass

raise InvalidAction("invalid actions")


# Exceptions don't have to be 

def divide_with_exception(number, divisor):
	try:
		print("{} / {} = {}".format(
			number, divisor, number / divisor * 1.0))
	except ZeroDivisionError:
		print("You can't divide by zero")


item_type = 'widget'
inv = Inventory()
inv.lock(item_type)
try:
	num_left = inv.purchase(item_type)
except InvalidItemType:
	print("Sorry, we don't sell {}".format(item_type))
except OutOfStock:
	print("Sorry, that item is out of stock.")
else:
	print("Purchase complete. There are ""{} {}s left".format(num_left, item_type))
finally:
	inv.unlock(item_type)



# Adding behaviors to classes via properties 
# In Java, never makes public members private. In python no real private members
# Get and set properties 
class Color:
	def __init__(self, rgb_value, name):
		self.rgb_value = rgb_value
		self._name = name
		
	def _set_name(self, name):
		if not name:
			raise Exception("Invalid Name")
		self._name = name
	
	def _get_name(self):
		return self._name
	
	name = property(_get_name, _set_name)

# this creates a new attribute on the Color class called name

# This property constructor can actually accept two additional arguments, a deletion function and a docstring for the property.

class Silly:
	def _get_silly(self):
		print("You are getting silly")
		return self._silly
	def _set_silly(self, value):
		print("You are making silly {}".format(value))
		self._silly = value
	def _del_silly(self):
		print("Whoah, you killed silly!")
		del self._silly
	silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")


# Property function can be used with the decorator syntax to turn a get function into a property
class Foo:
	@property
	def foo(self):
		return "bar"

class Foo:
	@property
	def foo(self):
		return self._foo
	
	@foo.setter
	def foo(self, value):
		self._foo = value

	# a setter function 


# Custom getter used for attributes needed to calculate on the fly
class AverageList(list):
	@property
	def average(self):
		return sum(self) / len(self)

class WebPage:
	def __init__(self, url):
	self.url = url
	self._content = None
	
	@property
	def content(self):
		if not self._content:
			print("Retrieving New Page...")
			self._content = urlopen(self.url).read()
		return self._content


# Split out steps into separate methods:
# Readability, Extensibility, Partitioning 

# A delegation method 

class ZipReplace:
	def __init__(self, filename, search_string, replace_string):
		self.filename = filename
		self.search_string = search_string
		self.replace_string = replace_string
		self.temp_directory = Path("unzipped-{}".format(filename))


def zip_find_replace(self):
	self.unzip_files()
	self.find_replace()
	self.zip_files()


if __name__ == "__main__":
	ZipReplace(*sys.argv[1:4]).zip_find_replace()


# Duplicate code
# Readability and maintainability


# Python Data Structures
# Tuples - used to store data
# Should generally store values that are different. Primary purpose is to aggregate different pieces of data into one container

# Named Tuples
# If know in advance what attributes to store, can use named nutples

# we describe the named tuple by giving it a name and outlining its attributes. This returns a class-like object that we can instantiate with the required values as many times as we want:
from collections import namedtuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("FB", 75.00, high=75.03, low=74.90)

# The namedtuple constructor accepts two arguments. The first is an identifier for the named tuple. The second is a string of space-separated attributes that the named tuple can have.


# Dictionary - when you want to find one object based on some other object
# Efficient for looking up a value given a key
for stock, values in stock.items():
	print("{} last value is {}".format(stock, values[0]))

# Lists are mutable therefore not hashable and not being used for dictionary keys

# Indexing system
# Each key represent some aspect of a single structure - similar set of keys

# Use defaultdict so we don't need to worry about if it has value or not
from collections import defaultdict
def letter_frequency(sentence):
	frequencies = defaultdict(int)
	for letter in sentence:
		frequencies[letter] += 1
		return frequencies


from collections import defaultdict
num_items = 0
def tuple_counter():
	global num_items
	num_items += 1
	return (num_items, [])
d = defaultdict(tuple_counter)


# Counter
from collections import Counter
def letter_frequency(sentence):
	return Counter(sentence)


from collections import Counter
responses = [
	"vanilla",
	"chocolate",
	"vanilla",
	"vanilla",
	"caramel",
	"strawberry",
	"vanilla"
]

print("the children voted for {} ice cream".format(Counter(responses).most_common(1)[0][0]))


# Lists
# Store items in some order

# Sorting lists

# To make it comparable, use the special method __lt__

class WeirdSortee:
	def __init__(self, string, number, sort_num):
		self.string = string
		self.number = number
		self.sort_num = sort_num
	
	def __lt__(self, object):
		if self.sort_num:
			return self.number < object.number
		return self.string < object.string
	
	def __repr__(self):
		return"{}:{}".format(self.string, self.number)

# Can just implement __lt__ and __eq__ and then applying the @total_ordering class decorator

from functools import total_ordering

@total_ordering
class Stores:
	def __int__(self, string, number, sort_num):
		self.string = string
		self.number = number
		self.sort_num = sort_num

	def __lt__(self, object):
		if self.sort_num:
			return self.number < object.number
		return self.string < object.string

	def __repr__(self):
		return"{}:{}".format(self.string, self.number)

	def __eq__(self, object):
		return all((
			self.string = object.string
			self.number = object.number
			self.sort_num = object.number
			self.sort_num == object.number
			))

# To customize sort keys
sort(key ="")

# Sets are helpful when needing unique objects
my_artists = {"Sarah Brightman", "Guns N' Roses", "Opeth", "Vixy and Tony"}

auburns_artists = {"Nickelback", "Guns N' Roses", "Savage Garden"}
print("All: {}".format(my_artists.union(auburns_artists)))
print("Both: {}".format(auburns_artists.intersection(my_artists)))
print("Either but not both: {}".format(
my_artists.symmetric_difference(auburns_artists)))

# Extending Built-ins 
# Either create a new object which holds the container as an attribute (composition), or subclass the built-in object (inheritance)

# Composition is usually the best alternative if all we want to do is use the container to store some objects using that container's features.
# But need to use Inheritance if we want to change the way the container actually works (for list overwrite set item and append methods)

# Special Methods

x in myobj # implement __contains__
myobj[i] = value # __setitem__ method 
something = myobj[i] # __getitem__


# Example of implementing a sorted dictionary 
from collections import KeysView, ItemsView, ValuesView
class DicSorterd(dict):
	def __new__(*args, **kwargs):
		new_dict = dict.__new__(*args, **kwargs)
		new_dict.ordered_keys = []
		return new_dict

	def __setitem__(self, key, value):
		if key not in self.ordered_keys:
			self.ordered_keys.append(key)
		super().__setitem__(key, value)

	def setdefault(self, key, value):
		if key not in self.ordered_keys:
			self.ordered_keys.append(key)
		return super().setdefault(key, value)

	def keys(self):
		return KeysView(self)

	def values(self):
		return ValuesView(self)

	def items(self):
		return ItemsView(self)

	def __iter__(self):
		'''for x in self syntax'''
		return self.ordered_keys.__iter__()

# The keys, items, and values methods all return views onto the dictionary.

# Queue can be better tha lists if you don't need random access. While using lists, if insert at beginning, requires shifting every other element

# Priority queue
# Convention is to store tuples in a priority queue, where the first element in the tuple is the priority of the element, and the second element is the data


len(myobj) # is essentially the same as MyObj.__len__(myobj)

reversed(myobj) # calls __reversed__()

enumerate(file)

import sys
filename = sys.argv[1]
with open(filename) as file:
	for index, line in enumerate(file):
		print("{0}: {1}".format(index+1, line), end='')

all, any 

hasattr, getattr, setattr, and delattr # which allow attributes on an object to be manipulated by their string names.



# Use readline so that you don't load too much data into memory

# Placing into context manager
# Makes sure the file is closed even if exception is occured 
with open('filename') as file:
	for line in file:
		print(line, end ='')

# two special methods required of the context manager with
class StringJoiner(list):
	def __enter__(self):
		return self
	def __exit__(self, type, value, tb):
		self.result = "".join(self)

# Method overloading

# to make an argument optional
def default_arguments(x, y, z, a="Some String", b=False):
	pass

# note the default value was calculated when the function was defined, not when it was called

# Python can also take an arbitrary number of positional and keyword arguments
# *links means I'll accept any number of arguments and put them all in a list named links

def get_pages(*links):
	for link in links:
		print(link)


**kwargs # arbitrary keyword arguments

class Options:
	default_options = {
		'port': 21,
		'host': 'localhost'
	}

	def __init__(self, **kwargs):
		self.options = dict(Options.default_options)
		self.options.update(kwargs)

	def __getitem__(self, key):
		return self.options[key]

# Keyword argument useful when we want to accept arguments to pass onto the second function but don't know which ones yet

# Unpacking arguments
# Given a list or dictionary of values, we can pass those values into a function as if they were normal positional or keyword arguments
*some_args
**more_args


# Functions are objects 
# Pass functions around at a later date (e.g. when a certain condition is met) - event driven timer

import datetime
import time
class TimedEvent:

# Create objects which can be called as though it were a function
# Any object can be made callable by giving it a __call__ method 



# Strings

template = "Hello {}, you are currently {}."
print(template.format('Dusty', 'writing'))


template = "Hello {0}, you are {1}. Your name is {0}."
print(template.format('Dusty', 'writing'))

# formating
# Can also do container lookup and object lookup (attributes)
print("Sub: ${0:0.2f} Tax: ${1:0.2f} "
"Total: ${total:0.2f}".format(
subtotal, tax, total=total))



# Pickle
# objected oriented way to store objects directly in a special storage format. Converts an object into a sequence of bytes that can be stored
# the file like object needs a write method 
# load method - needs file-like read and readline arguments 
import pickle
import pickle
some_data = ["a list", "containing", 5,"values including another list",["inner", "list"]]

with open("pickled_list", 'wb') as file:
	pickle.dump(some_data, file)

with open("pickled_list", 'rb') as file:
	loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_data

# dumps and loads behave like file-like counterparts, except they return or accept bytes instead of file-like objects

# what makes attributes unpicklable
# Usually, it has something to do with timesensitive attributes that it would not make sense to load in the future

# When pickle tries to serialize an object, it tries to store the object's __dict__ attribute (a dictionary mapping all attribute names to values)

__getstate__
__setstate__

# JSON is a data notation - but unable to represent classes, methods, and functions


# Iterator Pattern
while not iterator.done():
	item = iterator.next()
# do something with the item

# Iterator must have a __next__ method that the for loop can call. Additionally every iterator should fulfill the Iterable interface
# Any class that provides an __iter__ method is iterable
class CapitalIterable:
	def __init__(self, string):
		self.string = string

	def __iter__(self):
		return CapitalIterable(self.string)

class CapitalIterator:
	def __init__(self, string):
		self.words = [w.capitalize() for w in string.split()]
		self.index = 0

	def __next__(self):
		if self.index == len(self.words):
			raise StopIteration()
		word = self.words[self.index]
		self.index += 1
		return word
	
	def __iter__(self):
		return self

	def __iter__(self):
		return self


	iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
	iterator = iter(iterable)
	while True:
		try:
			print(next(iterator))
    	except StopIteration:		
    		break

# list comprehension is more efficient

# Anything iterable or can be placed in a for loop can be used with list comprehension

import sys
filename = sys.argv[1]
with open(filename) as file:
	header = file.readline().strip().split('\t')
	contacts = [
		dict(
			zip(header, line.strip().split('\t'))
			) for line in file
		]
for contact in contacts:
	print("email: {email} -- {last}, {first}".format(**contact))


# Set and dictionary comprehensions

Book = namedtuple("Book", "author title genre")
books = [
Book("Pratchett", "Nightwatch", "fantasy"),
Book("Pratchett", "Thief Of Time", "fantasy"),
Book("Le Guin", "The Dispossessed", "scifi"),
]
fantasy_authors = {b.author for b in books if b.genre == 'fantasy'}

# generator expression - To create a generator expression, wrap the comprehension in () instead of [] or {}.


import sys
inname = sys.argv[1]
outname = sys.argv[2]
with open(inname) as infile:
	with open(outname, "w") as outfile:
		warnings = (l for l in infile if 'WARNING' in l)
			for l in warnings:
				outfile.write(l)


# yield is key to generators 
# the function picks up after yield. If nothing after the yield, then jumps to the next iteration

import sys
inname, outname = sys.argv[1:3]
def warnings_filter(infilename):
	with open(infilename) as infile:
		yield from (
			l.replace('\tWARNING', '')
			for l in infile
			if 'WARNING' in l
			)

filter = warnings_filter(inname)
with open(outname, "w") as outfile:
	for l in filter:
		outfile.write(l)

def walk(file):
	if isinstance(file, Folder):
		yield file.name + '/'
		for f in file.children:
			yield from walk(f)
	else:
		yield file.name


# Decorator Pattern
# Wrap an object that provides core functionality with objects that alters functionality



