# class Solution:
#     # @param {integer[]} nums
#     # @return {integer[][]}
#     def __init__(self):
#         self.res = [[]]
    
#     def subsets(self, nums):
#         nums.sort()
#         for i in xrange(1, len(nums) + 1):
#             self.permute(nums, i)
#         return self.res

#     def permute(self, nums, length):
#         self.DFS([], nums, length)
        
#     def DFS(self, comb, left_nums, length):
#         if len(comb) == length:
#            self.res.append(list(comb))
#            return
#         for i in xrange(len(left_nums)):
#             comb.append(left_nums[i])
#             self.DFS(comb, left_nums[i + 1:], length)
#             comb.pop()

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.res = []
        self.length = 0 
    
    def subsets(self, nums):
        nums.sort()
        self.length = len(nums)
        self.DFS([], 0, nums, 0)
        return self.res
        
    def DFS(self, comb, start, nums, depth):
        self.res.append(list(comb))
        if depth == self.length:  return
        for i in xrange(start, self.length):
            comb.append(nums[i])
            # self.DFS(comb + [nums[i]], i + 1, nums, depth + 1)
            self.DFS(comb, i + 1, nums, depth + 1)
            comb.pop()

if __name__ == '__main__':
   s = Solution()
   print s.subsets([1, 2, 3])