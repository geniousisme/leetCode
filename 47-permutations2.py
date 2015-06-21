class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.length = 0
    def permuteUnique(self, nums):
        res = []
        if nums:
           self.length = len(nums)
           nums.sort()
           visited = [False for i in xrange(self.length)]
           self.dfs(nums, [], 0, visited, res)
        return res

    def dfs(self, nums, perm, perm_len, visited, res):
        if perm_len == self.length:
           res.append(perm)
           return
        for i in xrange(self.length):
            if not visited[i]:
               if i > 0 and visited[i - 1] == False and nums[i - 1] == nums[i]:
                  continue
               visited[i] = True
               self.dfs(nums, perm + [nums[i]], perm_len + 1, visited, res)
               visited[i] = False

if __name__ == '__main__':
   s = Solution()
   print s.permuteUnique([1,1,2])
        