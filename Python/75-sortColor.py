class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        length = len(nums)
        zero_idx = i = 0; two_idx = length - 1
        while i <= two_idx:
              if nums[i] == 0:
                 nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                 zero_idx += 1
                 i        += 1
              elif nums[i] == 2:
                   nums[two_idx], nums[i] = nums[i], nums[two_idx]
                   two_idx -= 1
              else: # nums[i] == 1:
                   i += 1

if __name__ == '__main__':
   s = Solution()
   nums = [0, 0]
   s.sortColors(nums)
   print nums
   nums = [1, 2, 0]
   s.sortColors(nums)
   print nums
   nums = [1, 1, 2, 1, 0, 2, 2, 0, 1, 2, 0, 0, 1, 2]
   s.sortColors(nums)
   print nums