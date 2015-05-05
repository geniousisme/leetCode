class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def __init__(self):
        self.res  = []

    def combine(self, n, k):
        if not n:
           return self.res
        self.DFS([], range(1, n + 1), k)
        return self.res
    
    def DFS(self, comb, left_nums, k):
        if len(comb) == k:
            self.res.append(list(comb))
            return
        for i in xrange(len(left_nums)):
            comb.append(left_nums[i])
            # self.DFS(comb + [left_nums[i]], left_nums[i + 1:], k)
            self.DFS(comb, left_nums[i + 1:], k)
            # comb.remove(left_nums[i])
            comb.pop(-1)


if __name__ == '__main__':
   s = Solution()
   combination = s.combine(10, 3)
   print combination
   print 'length:', len(combination)