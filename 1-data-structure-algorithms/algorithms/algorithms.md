# Data Structures

## Operations

Read
- look up particular spot (i.e. index of an array)
Search
- look for a particular value
Insert
- add a new value
Delete
- remove a value


## Array
Read
- computer can jump to the memory address the array begins and find the first element

Search
- read through one by one

Insert
- depends on where to insert
    - inserting at end is fast, since computer keeps track of the array size
    - allocating additional cells in memory can be tricky
- inserting data in the middle or beginning can be lengthy - that shifts pieces of data to make room for inserting

Delete
- May need to shift data to fill the blank


# Algorithms Basics

Definition: a set of instructions for completing a specific task

Big O: How Many Steps Relative to N Elements


## Searching Algorithms
Linear search
Binary search


## Sorting Algorithms
Bubble Sort
In each pass-through, the highest unsorted value “bubbles” up to its correct position.

```python
def bubble_sort(list):
    # unsorted_until_index is the rightmost index that has not been sorted
    unsorted_until_index = len(list) - 1
    sorted = False
    while not sorted:
        # in each pass-through, we’ll assume the array is sorted until we encounter a swap
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        unsorted_until_index -= 1
    return list
```

Selection Sort
In each pass through, keep track of index of the smallest value seen so far then swap with the starting value


Insertion Sort
Best case can work better than Selection sort or bubble sort



# Dynamic Programming

Dynamic programming is the process of optimizing recursive problems that have overlapping subproblems.

Essentially, memoization reduces recursive calls by remembering previously
computed functions.

```python
def fib(n, memo):
    if n == 0 or n == 1:
        return n
    
    # Check the hash table (called memo) to see whether fib(n) was already computed or not:
    if not memo.get(n):
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    return memo[n]
```

