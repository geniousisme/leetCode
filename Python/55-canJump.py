class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        length   = len(nums)
        curr_idx = length - 1
        i        = length - 2
        while i > -1:
              if i + nums[i] >= curr_idx:
                 curr_idx = i
              i -= 1
        if not curr_idx:
           return True
        return False

if __name__ == '__main__':
   s = Solution()
   print s.canJump([2,3,1,1,4])
   print s.canJump([2, 2, 2, 1, 4])
   print s.canJump([1, 1, 1, 1, 2, 0, 0])
   print s.canJump([3, 2, 1, 0, 4])
   print s.canJump([5,9,3,2,1,0,2,3,3,1,0,0])







