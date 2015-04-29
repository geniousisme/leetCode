class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.length = 0
        self.res    = []

    def permute(self, num):
        if not num: return num
        if len(num) == 1: return [num]
        self.length = len(num)
        self.DFS([], num)
        return self.res

    def DFS(self, perm, left_num):
        if len(perm) == self.length:
           self.res.append(perm)
           return self.res
        for i in xrange(len(left_num)):
            self.DFS(perm + [left_num[i]], left_num[:i] + left_num[i + 1:])

if __name__ == '__main__':
   s = Solution()
   num = [1, 2, 3, 4]
   print s.permute(num)



