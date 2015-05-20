class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.res = []
        self.prev_num = None
    
    def permuteUnique(self, nums):
        if nums: 
           nums.sort()
           self.DFS([], nums, None)
        return self.res

    def DFS(self, comb, left_nums, prev_num):
        if not left_nums:
           self.res.append(comb)
           return
        for i in xrange(len(left_nums)):
            if prev_num != left_nums[i]:
               prev_num =  left_nums[i]
               self.DFS(comb + [left_nums[i]], left_nums[:i] + left_nums[i + 1:], prev_num)
               

if __name__ == '__main__':
   s = Solution()
   print s.permuteUnique([1, 1, 2])