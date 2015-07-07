class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
           return False
        numDict = collections.OrderedDict()
        length = len(nums)
        
        for j in xrange(length):
            key = nums[j] / max(1, t)
            for i in [key - 1, key, key + 1]:
                if i in numDict and abs(numDict[i] - nums[j]) <= t:
                   return True
            numDict[key] = nums[j]
            if j >= k:
               numDict.popitem(last=False)
        return False



        