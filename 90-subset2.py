class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.res = []
        self.length = 0
    
    def subsetsWithDup(self, nums):
        self.length = len(nums)
        nums.sort()
        if not self.length:
           return []
        self.DFS(nums, [], 0, 0)
        return self.res

    def DFS(self, nums, comb, start, depth):
        if comb not in self.res:
           self.res.append(list(comb))
        if depth == self.length:
           return
        for i in xrange(start, self.length):
            # comb.append(nums[i])
            self.DFS(nums, comb + [nums[i]], i + 1, depth + 1) # this is the fastest one, think it will use the mem to trade for time
            # self.DFS(nums, comb, i + 1, depth + 1)
            # comb.pop()


    def subsetsIter(self, nums):
        self.length = len(nums)
        nums.sort()
        if not self.length:
           return []
        self.DFS(nums, [], 0, 0)
        return self.res

if __name__ == '__main__':
   s = Solution()
   nums = [1, 2, 2]
   print s.subsetsWithDup(nums)
        