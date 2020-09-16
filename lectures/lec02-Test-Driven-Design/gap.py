# Test Driven Design for gap_test (Step by step)
# 1) Think clearly about how each function should work
#   What are the inputs(what are arguments)
#   A: Two numbers, x and y
#   What is the outputs (what should be returned)
#   A: The distance between x and y, i.e., |x-y|
#   What are the special cases?
#   A: x and y the same, i.e., x==y
#   What are the usual cases?
#   A: x>y or x<y
# 2) Develop a function signature (def + docstring)

def gap(x, y):
    ''' Returns the distance between two input numbers.'''
    pass

# 3) Write actual “test cases” before you start to code each function
def test_gap():
    assert gap(10,10)==0, 'x==y test failed.'
    assert gap(1, 10)==9, 'x<y test failed.'
    assert gap(15,13)==2, 'x>y test failed.'
# 4) Now code the function

def gap(x, y):
    ''' Returns the distance between two input numbers.'''
    if x > y:
        return x - y
    else:
        return y - x

# 4) Keep on testing, add new cases to 3) above as needed
if __name__ == '__main__':
   test_gap()
   print('test_gap completed')
   print(gap(5,6))

print('gap.py __name__ = '+__name__)