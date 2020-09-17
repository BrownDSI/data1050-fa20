# %% [markdown]
"""
Solve the following problem using Test-First Design (TFD):

> Write a function `gap(x,y)` that returns the distance between two numbers?  Use
`if` statements and not a function like `abs` or `max`. 

Follow the TFD Steps (below) in order, and document the result of each step.

**Test-First Design Steps**  
`**Think before you code**`   
1. Inputs - what are arguments?  
2. Outputs - what should be returned?  
3. Usual cases  
4. Special cases   
5. Create **function specification** (signature + docstring)  
6. Implement tests for each case
7. Implement function  
8. add/improve tests as needed 
"""

# %%
# BEGIN SOLUTION
"""
Following **Test-First Design Steps**  
1. Inputs - what are arguments?  
A: Two numbers, x and y

2. Outputs - what should be returned? 
A: The distance between x and y, i.e., |x-y|

# 3. Special cases
A: x=y, gap(5,5) = 0

# 4. Usual cases     
A: x>y or x<y
examples: gap(10,8) = 2, gap(-2,3) = 5
"""

# 5. Develop a function signature (def + docstring)

def gap(x, y):
    ''' Returns the distance between two input numbers.'''
    pass

# 6) Implement tests for each cases

def test_gap():
    assert gap(5, 5)==0, 'x==y test failed'
    assert gap(10, 8)==2, 'x>y test failed' 
    assert gap(-2, 3)==5, 'x<y test failed' 

# 7) Implement function 

def gap(x, y):
    ''' Returns the distance between two input numbers.'''
    if x > y:
        return x - y
    else:
        return y - x

# 8) add/improve tests as needed 
#A: No additional tests needed

# END SOLUTION

if __name__ == '__main__': 
   test_gap()
   print('all tests complete')
