class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numTable = {}
        for i in xrange(len(nums)):
            if numTable.get(nums[i]) is not None:
               if i - numTable[nums[i]][0] <= k:
                  return True
               else:
                  numTable[nums[i]] = [i]
            else:
               numTable[nums[i]] = [i] 
        return False

if __name__ == '__main__':
   s = Solution()
   print s.containsNearbyDuplicate([1, 2, 2, 3, 4, 5], 3)
   print s.containsNearbyDuplicate([1, 2, 3, 4, 4, 5, 2], 3)

        