#!/usr/bin/env python
# coding: utf-8

# ### Correctness, Run-Time, Algorithmic Run-Time
# ##### *22 September 2020*
# ##### *DATA 1050*
# 
# 1. Correctness - When is an algorithm correct?
# 2. Run-time
# 3. Algorithmic Run-Time (ART)

# #### Fixing bugs versus showing correctness
# 
# Fixing bugs is great, but how do we know the algorithm itself is **correct**?
# 
# In order to show correctness one needs to show two things:
# 1. Algorithm will return the right answer if it finishes (i.e., terminates)
# 2. Algorithm will actually terminate
# 
# For iterative algorithms (i.e. algorithms with loops), a common strategy is to identify
# 
# 1. **Loop invariants** (true on loop entry, true on loop exit) guarantee the problem is on track for solution or solved
#    * on entry, answer is available, and with every iteration
#    * on exit, answer has been found
# 
# 2. **Loop termination guarantee** establishes real*real progress* is being made
#    * problem size is "finite"
#    * problem size reduced by at least **a constant amount** every iteration
# 

# #### Example `isin_binarySearch(L, item)`:
# 
# **Loop Invariant:**
# 
# * Entry: At the beginning of each iteration, the search space (i.e., {L[k]: k in in [low,...,high]} contains the solution
# * Exits:
# 1. (L[mid]==item) => item has been found 
# 2. (low>high), search space is empty => item has not been found
# 
# **Termination Guarantee:**
# After each iteration, the size of of the search space |[low,...,high]| is reduced by at least 1.

# In[ ]:


def isin_binarySearch(L,item): # L=[1], item=1
    '''Returns True when item is in L, False otherwise.
    Assumes L is sorted in ascending order.'''
    low = 0
    high = len(L) - 1
    while low <= high: 
        # Loop Invariant Entry: (must be true at beginning of each iteration)
        # Elements of list L with indices between low and high (inclusive) have not been examined.
        # list elements with index < low don't contain item. (no skipping)
        # list elements with index > high don't contain the item. (no skipping)
        mid = (low + high) // 2
        if L[mid] == item:
            return True # Loop Invariant Exit 1: L[mid] is the item being search for
        if L[mid] > item: # list[mid] was too high
            high = mid - 1
        else: # The guess was too low.
            low = mid + 1
        # Termination guarantee: (must be true after each iteration)
        # the number of elements between low and high have been reduced by at least 1

    # Loop Invariant Exit 2: Search space is now empty (L>H), item not found 
    return False


# **Exercise 4.1**
# 
# Show isin_linearSearch is correct.

# In[ ]:


# *Solution 4.1* 
# Your solution here

def isin_linearSearch(L,item):
    for e in L:
        if e == item:
            return True
    return False


# In[ ]:





# In Python, `for` loops can conveniently hide details, e.g., the above loop hides the index that is being using to linearly iterate through L.  But it is really helpful to have access to the index when reasoning about loops.  
# 
# Similar issues arise when trying to reason about list comprehensions, the `in` operator for contains, `filter`, `map`, `reduce`, etc.
# 
# #### Let's refactor this `for` loop into a `while` loop
# 
# **Question:** Is it always possible to convert other loop constructs into a corresponding while loop?
# 
# **Answer:** Yes! see below.
# 
# **Question:** Does this mean I should only use `while` loops when I program? Absolutely not, use of explicit indexing often leads to code that is harder to write correctly and read subsequently (and thus maintain).  Whereas, avoiding it can often make your code easier to write and for others to understand. _Simple is often better._

# In[ ]:


def isin_linearSearch_while_version(L,item):
    'Returns True when item is in L, False otherwise'
    i = 0
    while i < len(L):
        if L[i] == item:
            return True
        i = i+1
    return False

print(isin_linearSearch_while_version([4,2,6,7,10],1))
print(isin_linearSearch_while_version([4,2,6,7,10],6))
print(isin_linearSearch_while_version([4,2,6,7,10],11))


# In[ ]:


def isin_linearSearch_while_version(L,item):
    'Returns True when item is in L, False otherwise'
    i = 0
    while i < len(L):
        # Loop Invariant Entry: item may be in {L[k] : k in [i,...,len(L))}
        # item is not in {L[k] : k in [0,...,i)} (nothing missed)
        if L[i] == item:
            return True # Loop Invariant Exit 1: item was found
        i = i+1
        # Termination Guarantee: Size of problem, |[i,...,len(L))| has been reduced by 1

    # Loop Invariant Exit 2: no remaining elements remain to check
    return False

print(isin_linearSearch_while_version([4,2,6,7,10],1))
print(isin_linearSearch_while_version([4,2,6,7,10],6))
print(isin_linearSearch_while_version([4,2,6,7,10],11))


# Once you clearly understand how things like `for` loops operate, you can also reason about them directly, e.g.,

# In[ ]:


def isin_linearSearch(L,item):
    'Returns True when item is in L, False otherwise'
    for e in L:
        # Looop Invariant Entry: item may remain in rest of L
        # item not present in the beginning of L (no skipping)
        if e == item:
            return True # Loop *Invariant Exit #1* item was found
        # Termination: elements following e will be considered

    *Invariant Exit #2* no remaining elements remain to check
    return False


# ##### Calculating acutal runtimes
# Assumption: 
# 
# * Each __primitive statement__ takes a certain amount of time to execute.
# * For a given input we can add up the individual times to get the total time.
# 
# Example:
# 
# Below, the input size is len(L), times are indicated by `t1,...,t7` and we assume similar statements take a similar amount of time.

# In[ ]:


TIME

t0   def isin_binarySearch(L,item):   # Assign calling arguments to local variables L and item
         '''Returns True when item is in L, False otherwise. 
         Assumes L is sorted in ascending order.'''
t1       low = 0                      # Assign constant
t2       high = len(L) - 1            # Access len method, substract a constant
t3       while low <= high:           # Access two variables, comparison with jump
t4           mid = (low + high) // 2  # lookup two numbers and add them, then divide by 2
t5*          if L[mid] == item:       # Access two variables, lookup array element, comparison with jump
t6+               return True         # Return constant boolean value
t5*          if L[mid] > item:        # Access two variables, lookup array element, comparison with jump
t7-              high = mid - 1       # lookup value, substract 1
t8           else:                    # The guess was too low.
t7-              low = mid + 1        # lookup value, add 1
t6+      return False                 # Return constant boolean value


# Can use this approach to calculate worst cast runtime on a particular piece of hardware.
# 
# **Question:** Where is this sort of analysis very important?
n low high mid  RT(n)  # worst case, assume item is too small
0  0  -1        RT(0) = (t0 + t1 + t2) + (t3 + t6)

1  0   0    0   RT(1) = (t0 + t1 + t2) + (t3 + t4 + 2*t5 + t7) +
   0  -1         (t3 + t6) 

2  0   1    0   RT(2) = (t0 + t1 + t2) + (t3 + t4 + 2*t5 + t7) +
   0  -1         (t3 + t6)

3  0   2    1   RT(2) = (t0 + t1 + t2) + (t3 + t4 + 2*t5 + t7) +
   0   1    0    (t3 + t4 + 2*t5 + t7) +
   0  -1        (t3 + t6)

4  0   3    1   RT(n) = (t0 + t1 + t2) + (t3 + t4 + 2*t5 + t7) +
   0   0    0    (t3 + t4 + 2*t5 + t7) +
   0  -1         (t3 + t6)

5  0   4    2   RT(n) = (t0 + t1 + t2) + (t3 + t4 + 2*t5 + t7) +
   0   1    0    (t3 + t4 + 2*t5 + t7) +
   0   0    0    (t3 + t4 + 2*t5 + t7) +
   0  -1         (t3 + t6)

6  0   5    2   RT(n) = (t0 + t1 + t3) + (t3 + t4 + 2*t5 + t7) +
   0   1    0    (t3 + t4 + 2*t5 + t7) +
   0   0    0    (t3 + t4 + 2*t5 + t7) +
   0  -1         (t3 + t6)

In general what is RT(n)?
# **Solution**
# 
# $\newcommand\floor[1]{\lfloor#1\rfloor}$ 
# $\newcommand\ceil[1]{\lceil#1\rceil}$
# For $n>0$
# $$RT(n) = (t0 + t1 + t2) + (t3 + t4 + 2*t5 + t7)\ceil{\log(n)}+(t3+t6)$$
# 
# But even this isn't quite right due to _caching_, _Turbo Boost Technology_, etc.

# ##### Algorithmic Runtime, I
# 
# Goal: Move away from **machine-dependent details**, but still talk about performance of Algorithms.
# 
# Idea #1: Bound the time of all statements that don't depend on the size of the input by a constant!
# 
# Specifically, take C >= max(t1,t2,...,tk)
# 
# * This is possible because there are a finite number of statements.
# 
# As before we can the total number of Cs for a given input, and 
# can also count the number of Cs for a worst-case input of size n.

# In[ ]:


TIME

C   def isin_binarySearch(L,item): # L=[1], item=1
         '''Returns True when item is in L, False otherwise. 
         Assumes L is sorted in ascending order.'''
C        low = 0
C        high = len(L) - 1
C        while low < high:
C           mid = (low + high) // 2
C            if L[mid] == item:
C                return True
C            if L[mid] > item: # list[mid] was too high
C                high = mid - 1
C            else: # The guess was too low.
C                low = mid + 1
C        return False # Item doesn't exist


# Q: What is the runtime bound in this case?
# \
# A: Can just renumber everything
# ```
# n low high  mid RT(n)  # worst case, assume item is too small
# 0  0  -1        RT(0) = 3C + 2C
# 1  0   0    0   RT(1) = 3C + 5C +
#    0  -1         2C 
# 2  0   1    0   RT(2) = 3C + 5C +
#    0  -1         2C
# 3  0   2    1   RT(2) = 3C + 5C +
#    0   1    0    4C +
#    0  -1        2C
# 4  0   3    1   RT(n) =  3C + 5C +
#    0   0    0    5C +
#    0  -1         2C
# 5  0   4    2   RT(n) = 3C + 5C +
#    0   1    0    5C +
#    0   0    0    5C +
#    0  -1         2C
# 6  0   5    2   RT(n) = 3C + 5C +
#    0   1    0    5C +
#    0   0    0    5C +
#    0  -1         2C
# ```
# 
# The runtime bounds RTB(n) is as follows:
# $\newcommand\floor[1]{\lfloor#1\rfloor}$ 
# $\newcommand\ceil[1]{\lceil#1\rceil}$
# For $n>0$
# $$RTB(n) = 3C + 5C\ceil{\log(n)}+2C$$

# ##### Algorithmic Run-time, II
# 
# Goal: Move away from machine-dependent details, but still talk about performance of Algorithms.
# 
# Another Idea: Partition code into blocks of statements that don't depend on the size of the input, bound time for each block by a constant.
# 
# * This is possible because there are a finite number of statement blocks.
# 
# As before we can add up the total number of constants for a given input, can also count the number for a worst-case input of size n.
# 

# In[ ]:


TIME def isin_binarySearch(L,item): # L=[1], item=1
         '''Returns True when item is in L, False otherwise. 
         Assumes L is sorted in ascending order.'''
------------------------------------------------------------
A        low = 0
         high = len(L) - 1
-----------------------------------------------------------
B        while low < high:
             mid = (low + high) // 2
             if L[mid] == item:
                 return True
             if L[mid] > item: # list[mid] was too high
                 high = mid - 1
             else: # The guess was too low.
                 low = mid + 1
-----------------------------------------------------------
C        return False # Item doesn't exist


# For a given input, we can add up the total number of statement blocks that were entered.
# This gives a coarse but useful bound on the runtime.
# 
# For Binary Search (and most algorithms):
# 
# There are at most 
# * A units of setup time
# * B units of time per iteration
# * C units of exit time.
# 
# 
# The worst-case algorithmic runtime for an input of size $n>0$ is $$A+B\lceil{\log_2{n}}\rceil+C$$
# 
# Thinking in terms of setup time, calculation time, and exit time is a very useful way to compare different ways of solving a problem.  This let's us meaningful compare algorithms, even for small n.

# **Example** 
# Using Algorithmic Run-Time (ART), we will compare using linear search versus pre-sorting and binary search to check whether or not $k$ numbers are in an unsorted list of length $n$.
# 
# We will assume sorting takes $n\log{n}$ operations.

# ```
# def isin_binarySearch_kitems(L,items): # L=[1], item=1
#          '''Returns True when item is in L, False otherwise.'''
#         L = sorted(L) # Takes A_s+(n*log n)*B_s+C_s
#         return [isin_binarySearch(L,item) for item in items]
# ```
# 
# $ART(linear\_search, n) = A_l+B_l \cdot n+C_l$
# 
# $ART(binary\_search, n) = A_b+B_b \cdot \log{n}+C_b$
# 
# $ART([sort, binary\_search], n, k) = A_s + B_s \cdot n\log{n}+ C_s + k \cdot (A_b+B_b \cdot \log{n}+C_b)$
# 
# $ART(linear\_search, n, k) = k \cdot (A_l+B_l \cdot n+C_l)$
