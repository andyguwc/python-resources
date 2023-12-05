# Hash Tables
We can now understand why a hash table would yield faster lookups for our
restaurant menu than an array. With an array, we would have to search through each cell until we find it. For an unordered array, this would take up to O(N), and for an ordered array, this would take up to O(log N). Using a hash table, however, we can now use
the actual menu items as keys, allowing us to do a hash table lookup of O(1).

Hash collision
- Separate chaining - store a reference to an array


Efficient hash table
strike a balance of avoiding collisions while not consuming lots of memory
- how much data
- how many cells
- which hash function to use


# Stacks
- Data can be inserted only at the end of a stack.
- Data can be deleted only from the end of a stack.
- Only the last element of a stack can be read.


# Queues
- Data can be inserted only at the end of a queue. (This is identical behavior to the stack.)
- Data can be deleted only from the front of a queue. (This is the opposite behavior of the stack.)
- Only the element at the front of a queue can be read. (This, too, is the opposite of behavior of the stack.)



# Linked List

Linked lists, on the other hand, work quite differently. Instead of being a
contiguous block of memory, the data from linked lists can be scattered across
different cells throughout the computer’s memory.

This is the key to the linked list: each node also comes with a little extra
information, namely, the memory address of the next node in the list.

This extra piece of data—this pointer to the next node’s memory address—is
known as a link.

Search O(N)
Read O(N)
Insert at beginning O(1) while Array favor inserting at the end of the list
Delete from begining O(1)

Operation | Array              | Linked list
Reading   | O(1)               | O(N)
Search    | O(N)               | O(N)
Insertion | O(N) (O(1) at end) | O(N) (O(1) at beginning)
Deletion  | O(N) (O(1) at end) | O(N) (O(1) at beginning)


Queues as Doubly Linked Lists
Because doubly linked lists have immediate access to both the front and end
of the list, they can insert data on either side at O(1) as well as delete data
on either side at O(1).
Because doubly linked lists can insert data at the end in O(1) time and delete
data from the front in O(1) time, they make the perfect underlying data structure
for a queue.


# Binary Search Tree

Data structure that maintains order yet also has fast search

A balanced tree if its nodes' subtrees have the same number of nodes in it

A binary tree is a tree in which each node has zero, one, or two children.
A binary search tree is a binary tree that also abides by the following rules:
- Each node can have at most one “left” child and one “right” child.
- A node’s “left” descendants can only contain values that are less than the node itself. Likewise, a node’s “right” descendants can only contain values that are greater than the node itself.

If there are N nodes in a balanced binary tree, there will be about log N levels

While ordered arrays have O(log N) search and O(N) insertion, binary search trees have O(log N) search and O(log N) insertion.

Traversal
- inorder traversal
- call recursively on left child, visit the node, call itself recursively on right child

```python
def traverse_and_print(node):
    if node is None:
        return
    traverse_and_print(node.leftChild)
    print(node.value)
    traverse_and_print(node.rightChild)
```


# Priority Queue & Binary Heap

A priority queue is a list whose deletions and access are just like a classic
queue, but whose insertions are like an ordered array. That is, we only delete
and access data from the front of the priority queue, but when we insert data,
we always make sure the data remains sorted in a specific order.

Array implementation would take O(N) for insertion and O(1) for delete (only end of the array, which represents the front of the priority queue)


The binary heap is a specific kind of binary tree. As a reminder, a binary tree
is a tree where each node has a maximum of two child nodes. (The binary
search tree from the last chapter was one specific type of binary tree.)

The (max) heap is a binary tree that maintains the following conditions: 
- The value of each node must be greater than each of its descendant nodes. This rule is known as the heap condition.
- The tree must be complete. A complete tree is a tree that is completely filled with nodes; no nodes are missing. 
    - So, if you read each level of the tree from left to right, all of the nodes are there. 
    - However, the bottom row can have empty positions, as long as there aren’t any nodes to the right of these empty positions.
    - The reason why completeness is important is because we want to ensure our heap remains well-balanced.

In a heap, the root node will always have the greatest value. (In a min-heap, the root will contain the smallest value.) This will be the key as to why the heap is a great tool for implementing priority queues. In the priority queue, we always want to access the value with the greatest
priority. With a heap, we always know that we can find this in the root node. Thus, the root node will represent the item with the highest priority.

Insertion takes O(log N)

Deletion - only delete the root node takes O(log N)


# Trie

The trie is a kind of tree that is ideal for text-based features such as autocomplete.

The point of our trie is to store words. Let’s see how the following trie
stores the words, “ace,” “bad,” and “cat” as shown in the diagram on page 308.
This trie stores the three words by turning each character of each word into
its own trie node. If you start with the root node and follow its "a" key, for
example, it points to a child node containing a key of "c". The "c" key, in turn,
points to a node that contains a key of "e". When we string these three characters
together, we get the word "ace".


Trie search
```python
def search(self, word):
    currentNode = self.root

    for char in word:
        if currentNode.children.get(char):
            currentNode = currentNode.children[char]
        else:
            return None
    
    return currentNode


def insert(self, word):
    currentNode = self.root

    for char in word:
        if currentNode.children.get(char):
            currentNode = currentNode.children[char]
        else:
            # if current character isn't found, add the character as a new child node
            newNode = TrieNode()
            currentNode.children[char] = newNode
            currentNode = newNode

    # after inserting the entire word add * key at the end
    currentNode.children["*"] = None


# collect all the words
def collectAllWords(self, node=None, word="", words=[]):
    currentNode = node or self.root

    for key, childNode in currentNode.children.items():
        # If the current key is *, it means we hit the end of a
        # complete word, so we can add it to our words array:
        if key == "*":
            words.append(word)
        else:
            # If we're still in the middle of a word:
            # We recursively call this function on the child node.
            self.collectAllWords(childNode, word + key, words)
    
    return words
```

# Graphs

Trees are graphs
- all nodes must be connected
- no cycles


Depth-first Search

1. Start at any random vertex within the graph.
2. Add the current vertex to the hash table to mark it as having been visited.
3. Iterate through the current vertex’s adjacent vertices.
4. For each adjacent vertex, if the adjacent vertex has already been visited,
ignore it.
5. If the adjacent vertex has not yet been visited, recursively perform depthfirst
search on that vertex.


Breadth-first Search
Traverse immediate connections first. Then spiral outward to move further and further from the root node.
1. Start at any vertex within the graph. We’ll call this the “starting vertex.”
2. Add the starting vertex to the hash table to mark it as having been visited.
3. Add the starting vertex to a queue.
4. Start a loop that runs while the queue isn’t empty.
5. Within this loop, remove the first vertex from the queue. We’ll call this
the “current vertex.”
6. Iterate over all the adjacent vertices of current vertex.
7. If the adjacent vertex was already visited, ignore it.
8. If the adjacent vertex has not yet been visited, mark it as visited by adding
it to a hash table, and add it to the queue.
9. Repeat this loop (starting from Step 4) until the queue is empty.

