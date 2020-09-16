# O(n^2) time | O(1) space
# "two index solution, non-pythonic"
def twoNumberSum_1(array, targetSum):
    for i in range(len(array)-1):
        iv = array[i]
        for j in range(i+1, len(array)):
            jv = array[j]
            if iv + jv == targetSum:
                return [iv, jv]
    return []

# O(n^2) time | O(1) space, except slicing copies,
# so O(n) space if you are being fussy.  A better python implementation would not.
# "index and slicing solution, pythonic"
def twoNumberSum_1p(array, targetSum):
    for (i, iv) in enumerate(array[:-1]):
        for jv in array[i+1:]:
            if iv + jv == targetSum:
                return [iv, jv]
    return []

# O(n) time | O(n) space
# "hash-map solution"
def twoNumberSum_2(array, targetSum):
    nums = {}
    for x in array:
        y = targetSum - x
        if y in nums:
            return [x, y]
        else:
            nums[x] = True
    return []


# O(nlogn) | O(1) space
# "in-place sort based solution"
def twoNumberSum_3(array, targetSum):
    array.sort()
    L = 0
    R = len(array)-1
    while L < R:
        v = array[L] + array[R]
        if v == targetSum:
            return [array[L], array[R]]
        elif v < targetSum:
            L += 1
        elif v > targetSum:
            R -= 1
    return []


def test_twoNumberSum(f):
    output = f([3, 5, -4, 8, 11, 1, -1, 6], 10)
    assert(set(output) == set([11, -1]))
    output = f([3, 5, -4, 8, 11, 1, -1, 6], 18)
    assert(set(output) == set([]))


test_twoNumberSum(twoNumberSum_1)
test_twoNumberSum(twoNumberSum_1p)
test_twoNumberSum(twoNumberSum_2)
test_twoNumberSum(twoNumberSum_3)
