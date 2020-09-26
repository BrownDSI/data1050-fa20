# Array

![](https://i.imgur.com/GP2RRe9.png)

The simplest data structure is the array, which is a contiguous block of memory. It is usually used to represent sequences.

Given an array A, A[i] denotes the (i + 1)th object stored in the array. Retrieving and updating A[i] takes O(1) time. Insertion into a full array can be handled by resizing, i.e., allocating a new array with additional memory and copying over the entries from the original array. This increases the worst-case time of insertion, but if the new array has, for example, a constant factor larger than the original array, the average time for insertion is constant since resizing is infrequent. Deleting an element from an array entails moving all successive elements one over to the left to fill the vacated space. For example, if the array is <2,3,5,7,9,11,13,17>, then deleting the element at index 4 results in the array <2,3,5,7,11,13,17>.The time complexity to delete the element at index i from an array of length n is O(n - i). The same is true for inserting a new element (as opposed to updating an existing entry).

## Know your array libraries

### Instantiating a list in Python

- [3, 5, 7, 11]
- [1] + [0] \* 10,
- list(range(100))
- [i for i in range(100)] i.e. list comprehension

### Basic list operations

- len(A)
- a.append(2)
- a.remove(2)
- a.insert(i, elem)
- a.reverse() in-place
- enumerate(A) in for loop
- Binary search for sorted list
  - bisect.bisect(A, 6)
  - bisect.bisect_left(A, 6)
  - bisect.bisect_right(A, 6)
- List slicing  
   A = [1, 6, 3, 4, 5, 2, 7]  
   A[2:4] = [3, 4]  
   A[2:] = [3, 4, 5, 2, 7]  
   A[:4] = [1, 6, 3, 4]  
   A[:-1] = [1, 6, 3, 4, 5, 2]  
   A[-3:] = [5, 2, 7]  
   A[-3:-1] = [5, 2]  
   A[1:5:2] = [6, 4]  
   A[5:1:-2] = [2, 4]  
   A[::-1] = [7, 2, 5, 4, 3, 6, 1] (reverses list)

# Hash Tables

## Hash Function

A function that maps a key to a hash value. For example, h(k) = k % m

## Resolve Hash Collision

if m = 20,

1 → 1 % 20 → 1  
5 → 5 % 20 → 5  
23 → 23 % 20 → 3  
63 → 63 % 20 → 3

- Chaining
  ![](https://i.imgur.com/VTQep20.png)

- Open Addressing
  ![](https://i.imgur.com/F2ziBZh.png)

[Reference](https://en.wikipedia.org/wiki/Hash_table#Separate_chaining)

## O(1) Lookup

## Python Built-in Hash Function

hash() is a built-in function that returns the hash value of an object (if hashable, mutable containers are not hashable, for example). Hash values are integers used to quickly compare dictionary keys while looking up a dictionary. **\_\_hash\_\_()** method of an object which is set by default is called internally.

## Know your hash table libraries

Hash table-based data structures in Python

- set (only stores keys)
- dict (stores key-value pairs, accessing value associated with a key that is not present leads to a KeyError exception)
- collections.defaultdict (returns the default value of the type that was specified when
  the collection was instantiated)
- collections.Counter (used for counting the number of occurrences of keys)

Basic Operations

- Set

  - s.add(3)
  - s.remove(3)
  - s.discard(3)
  - x in s
  - s <= t (is a subset of t)
  - s - t (elements in s that are not in t)

- Dict, defaultdict, and Counter
  - operations on Set
  - dict.items() to iterate over key-value pairs
  - dict.keys() to iterate over keys
  - dict.values() to iterate over values

# String

A string can be viewed as a special kind of array, namely one made out of characters. We treat strings separately from arrays because certain operations are commonly applied to strings, for example, comparison, joining, splitting, searching for substrings, replacing one string by another, parsing, etc., do not make sense for general arrays.

In order to work effectively with strings you need to know how strings are represented in memory, and understand basic operations on strings such as comparison, copying, joining, splitting, matching & etc. Advanced string processing algorithms often use hash tables and dynamic programming, which we will talk more about in the future.

A palindromic string is one that reads the same when it is reversed. The program below checks whether a string is palindromic. Rather than creating a new string for the reverse of the input string, it traverses the input string forwards and backwards, thereby saving space. Notice how it uniformly handles even and odd length strings.

```python
def is_palindromic(s):
    # Note that s[~i] translates to s[-(i + 1)] and s[len(s) - i - 1]
    return all(s[i] == s[~i] for i in range(len(s) // 2))
```

The time complexity is O(n) and the space complexity is O(1), where n is the length of the string.

## Know your string libraries

Key operations and functions

- s[3]
- len(s)
- s + t
- s[2:4]
- s.strip()
- s.startswith(prefix)
- s.endswith(suffix)
- s.split(',')
- ','.join(['a', 'b', 'c'])
- "Hello, {}. You are {}.".format(name, age)

Strings are immutable — operations like s = s[1:] or s += ’123’ imply creating a new array of characters that is then assigned back to s. This implies that concatenating a single character n times to a string in a for loop has O(n^2) time complexity.

# Linked List

(Based on EPI 7) A list implements an ordered collection of values, which may include repetitions. Specifically, a singly linked list is a data structure that contains a sequence of nodes such that each node contains an object and a reference to the next node in the list. The first node is referred to as the head and the last node is referred to as the tail; the tail's next field is null. The structure of a singly linked list is given in Figure 4.1. There are many variants of linked lists, e.g, tn a doubly linked list, each node has a link to its predecessor; similarly, a sentinel node or a self-loop can be used instead of null to mark the end of the list. The structure of a doubly linked list is given in Figure 4.2.

A list is similar to an array in that it contains objects in a linear order. The key differences are that inserting and deleting elements in a list has time complexity O(1). On the other hand, obtaining the kth element in a list is expensive, having O(n) time complexity. Lists are usually building blocks of more complex data structures. However, as we will see in this chapter, they can be the subject of tricky problems in their own right.

![](https://i.imgur.com/ud0GHsE.png)

For all EPI problems, unless otherwise stated, each node has two entries - a data field,
and a next field, which points to the next node in the list, with the next field of the last node being null. Its prototype is as follows:

```python
class ListNode:
    def __init__(self , data=0, next_node=None):
        self.data = data
        self.next = next_node
```

There are two types of list-related problems-those where you have to implement your own list,
and those where you have to exploit the standard list library. We will review both these aspects
here, starting with implementation, then moving on to list libraries.

Implementing a basic list APl-search, insert, delete-for singly linked lists is an excellent way
to become comfortable with lists.

Search for a key:

```python
def search_list(L, key):
    while L and L.data != key:
        L = L.next
    # If key was not present in the list , L will have become null.
    return L
```

Insert a new node after a specified node:

```python
# Insert new_node after node.
def insert_after(node , new_node):
    new_node.next = node.next
    node.next = new_node
```

Delete a node:

```python
# Delete the node past this one. Assume node is not a tail.
def delete_after (node):
    node.next = node.next.next
```

Insert and delete are local operations and have O(1) time complexity. Search requires traversing the entire list, e.g, if the key is at the last node or is absent, so its time complexity is O(n), where n is the number of nodes.

# Stack and Queues

Stacks support last-in, first-out semantics for inserts and deletes, whereas queues are first-in,
first-out. Stacks and queues are often building blocks in a solution to complex coding problems. As we will soon see, they can also make for stand-alone problems.

### Stacks

A stack supports two basic operations push and pop. Elements are added (pushed) and removed (popped) in last-in, first-out order, as shown below.

![](https://i.imgur.com/sWvgCIu.png)

If the stack is empty, pop typically returns None or throws an exception. When a stack is implemented using a linked list these operations have O(1) time complexity. If implemented using an array, there is maximum number of entries a stack can have, but push and pop are still O(1). If the array is dynamically resized, the amortized time for both push and pop is O(1). A stack can support additional operations such as peek, which returns the top of the stack without popping it.

### Queues

A queue also supports two basic operations, they are enqueue and dequeue. (If the queue is empty, dequeue typically returns null or throws an exception.) Elements are added (enqueued) and removed (dequeued) in first-in, first-out order. The most recently inserted element are often referred to as the tail or back element, and the item that was inserted least recently is referred to as the head or front element.

![](https://i.imgur.com/jWxCcab.png)

A queue can be implemented using a linked list, in which case these operations have O(1) time complexity. The queue API often includes other operations, e.g., a method that returns the item at the head of the queue without removing it, a method that returns the item at the tail of the queue without removing it, etc.
