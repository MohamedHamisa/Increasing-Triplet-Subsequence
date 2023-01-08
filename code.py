class Solution:
    def increasingTriplet(self, nums):
        inc = [float('inf')] * 2
        for x in nums:
            i = bisect.bisect_left(inc, x)
            if i >= 2:
                return True
            inc[i] = x
        return False
      

'''
Bisect left finds the leftmost insertion point in the sorted array. Bisect right finds the rightmost insertion point in the sorted array.
The only condition where bisect_left and bisect_right will return the same result is if the element does exist in the array.
'''
