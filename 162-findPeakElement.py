class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        # length = len(nums)
        # if length == 1: return 0
        return self.searchPeak(nums, 0, len(nums) - 1)
    
    def searchPeak(self, nums, start, end):
        if end == start:
           return start
        if end == start + 1:
           return start if nums[start] > nums[end] else end
        mid = (end + start) / 2
        if nums[mid] > nums[mid + 1]:
           return self.searchPeak(nums, start, mid)
        elif nums[mid] < nums[mid + 1]:
             return self.searchPeak(nums, mid, end)

if __name__ == '__main__':
   s = Solution()
   print s.findPeakElement([1, 5, 2, 3, 4, 2, 1])
   print s.findPeakElement([2, 1])
   print s.findPeakElement([1])


