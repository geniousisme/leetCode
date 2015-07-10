class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        length = len(s)
        if length == 0: return 0
        ans = 0
        num = ''
        stack = []
        sign = 1

        for i in xrange(length):
            if '9' >= s[i] >= '0':
               num += s[i]
            
            elif s[i] == '+':
                 ans += sign * int(num)
                 sign = 1
                 num  = ''

            elif s[i] == '-':
                 ans += sign * int(num)
                 sign = -1
                 num  = ''
            
            elif s[i] == '(':
                 stack.append(ans)
                 stack.append(sign)
                 sign = 1
                 ans  = 0

            elif s[i] == ')':
                 ans += sign * int(num)
                 sign = stack.pop()
                 ans  = sign * ans + stack.pop()
                 num  = 0

        if num != 0:
           ans += sign * int(num)

        return ans
                 
           

            

if __name__ == '__main__':
   s = Solution()
   print s.calculate('234567890')
   print s.calculate("1 + 1")
   print s.calculate(" 2-1 + 2 ")
   print s.calculate("(1+(4+5+2)-3)+(6+8)")