class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        length = len(s)
        stack  = []
        maxlen = 0; last = -1
        for i in xrange(length):
            if s[i] == '(':
               stack.append(i)
            else:
               if stack == []:
                  last = i
               else:
                  stack.pop()
                  if stack == []:
                     maxlen = max(maxlen, i - last)
                  else:
                     maxlen = max(maxlen, i - stack[-1])
        return maxlen

if __name__ == '__main__':
   s = Solution()
   print s.longestValidParentheses(")()())")
   print s.longestValidParentheses("(()")
   print s.longestValidParentheses("()")

        