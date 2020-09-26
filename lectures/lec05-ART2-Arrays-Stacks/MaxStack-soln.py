"""
Write a MaxStack class that supports:

- Pushing and popping values on and off the stack
- Peeking at the value at the top of the stack
- Getting the maximum of the stack at any given time

All methods should run in constant time and constant space.
"""

class MaxStack:
    # O(1) time | O(1) space
    def peek(self):
        "Returns what is on the top of stack but does not remove it"
        return self.stack[-1]
    
    # O(1) time | O(1) space
    def pop(self):
        "Removes top element from stack and returns it"
        self.maxStack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number):
        "Adds an element to the top of the stack"
        newMax = number
        if len(self.maxStack):
            newMax = max(self.maxStack[-1], number)
        self.maxStack.append(newMax)
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMax(self):
        "Return the largest item currently in the stack"
        return self.maxStack[-1]

    # O(1) time | O(1) space
    def __init__(self):
        "Initalizes an instance of the class"
        self.maxStack = []
        self.stack = []

def test_MaxStack():  
    # Q: How do we test a Class?
    ms = MaxStack() # Q: Make an instance, and test that.
    assert ms.maxStack==[], 'init' # Verify init is working (Whitebox)
    ms.push(2)
    assert ms.peek()==2, 'n=1'
    assert ms.getMax()==2, 'n=1'

# Q: Are more tests needed?
# A: Clearly, n>1, also, our current **test coverage** is lacking.

# Measuring Coverage
# $ pytest xyz.py --cov #
# $ 