class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if len(nums) == 1: 
           return nums[0]
        return self.binarySearch(nums, nums[0], 0, len(nums))

    def binarySearch(self, nums, curr_min, start, end):
        if end == 1 + start:
           return curr_min
        mid = (end + start) / 2
        if nums[mid] > nums[start]:
           curr_min = min(curr_min, nums[start])
           return self.binarySearch(nums, curr_min, mid, end)
        elif nums[mid] < nums[start]:
             curr_min = nums[mid]
             return self.binarySearch(nums, curr_min, start, mid)

if __name__ == '__main__':
   s = Solution()
   print s.findMin([4, 5, 6, 7, 0, 1, 2])
   print s.findMin([4, 5, 6, 7, 1, 2])
   print s.findMin([1])
   print s.findMin([2, 1])






