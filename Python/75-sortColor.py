class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColorsI(self, nums): # two pointers solution
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

    def sortColors(self, nums):
        count  = [0, 0, 0]
        length = len(nums) 
        k      = 0
        for i in xrange(length):
            count[nums[i]] += 1
        j = 0
        while j < length:
            while count[k]:
                  count[k] -= 1
                  nums[j] = k
                  j += 1
            k += 1



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