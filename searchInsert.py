class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        length = len(nums)
        if not nums:
           return [target]
        if target > nums[-1]: # target is larger than all of elems in list
           return length
        elif target < nums[0]: # target is smaller than all of elem in list
             return 0
        else:
             return self.binaryInsertSearch(nums, 0, length, target)

    
    def binaryInsertSearch(self, nums, start, end, target):
        if len(nums[start:end]) == 1:
           return start
        elif len(nums[start:end]) == 2:
             last_idx = end - 1
             if nums[last_idx] > target > nums[start]:
                return start + 1
             else:
                if nums[last_idx] == target: return last_idx
                if nums[start] == target: return start
        else:
             mid = (end + start) / 2
             if nums[mid] > target:
                return self.binaryInsertSearch(nums, start, mid, target)
             elif nums[mid] < target:
                  return self.binaryInsertSearch(nums, mid, end, target)
             else:
                  return mid

if __name__ == '__main__':
   s = Solution()
   nums = [1,3,5,6]
   print s.searchInsert(nums, 1)
   print s.searchInsert(nums, 3)
   print s.searchInsert(nums, 5)
   print s.searchInsert(nums, 6)
   print s.searchInsert(nums, 7)
   print s.searchInsert(nums, 0)
   print s.searchInsert(nums, 2)
   print s.searchInsert(nums, 4) # this one need to debug


