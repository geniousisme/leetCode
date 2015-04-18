class Solution:
    # @param an integer
    # @return a list of string
    def dfs_parenth(self, left, right, string, result):
        if right < left:
           return
        if right == 0 and left == 0:
           result.append(string)
        if right > 0:
           self.dfs_parenth(left, right - 1, string + ')', result)
        if left  > 0:
           self.dfs_parenth(left - 1, right, string + '(', result)

    def generateParenthesis(self, n):
        result = []
        if n > 0:
           self.dfs_parenth(n, n, '', result)
        return result

if __name__ == '__main__':
   s = Solution()
   print s.generateParenthesis(3)

   # test = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
   # for i,t in enumerate(test):
   #     if t not in result:
   #        print "err_index:", i, t
   #        print "there is something wrong"
   
   # for i,r in enumerate(result):
   #     if r not in test:
   #        print "err_index:", i, r
   #        print "there is something wrong"
   # print "all the same"