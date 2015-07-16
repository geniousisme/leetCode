class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        numTable = {}
        for n in nums:
            if numTable.get(n, 0) > 0:
               return True
            else:
               numTable[n] = 1
        return False

if __name__ == '__main__':
   s = Solution()
   print s.containsDuplicate([1, 2, 3, 4, 5])
   print s.containsDuplicate([1, 2, 2])




        