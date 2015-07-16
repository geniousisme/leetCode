class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        length = len(nums)
        if length == 1:
           return nums[0]
        return self.binarySearch(nums, nums[0], 0, len(nums))
    
    # Chris: this website has clear graph to show whats going on .
    def binarySearch(self, nums, curr_min, start, end):
        if end == start + 1:
           return curr_min
        mid = (start + end) / 2
        if nums[mid] > nums[start]:
           curr_min = min(curr_min, nums[start])
           return self.binarySearch(nums, curr_min, mid, end)
        elif nums[mid] < nums[start]:
             curr_min = nums[mid] # must be the minimum, by the graph showing
             return self.binarySearch(nums, curr_min, start, mid)
        else: # nums[mid] == nums[start]:
             return self.binarySearch(nums, curr_min, start + 1, end)

if __name__ == '__main__':
   s = Solution()
   print s.findMin([4, 5, 6, 7, 1, 2, 3, 3, 3])
   print s.findMin([1])
   print s.findMin([3, 3, 4, 4, 5, 0, 1, 1, 2, 2, 3, 3])




        