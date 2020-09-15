
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i, iv in enumerate(array[:-1]):
        for j, jv in enumerate(array[i+1:]):
            if iv + jv == targetSum:
                return [iv, jv]
    return []
    


output =  twoNumberSum([1,2,5], 6)
assert( set(output) == set([1,5] ))
