class Solution:
    # @param {string} s
    # @return {integer}
    # Chris::TODO: take this as reference:
    # http://www.wengweitao.com/leetcode-basic-calculator.html
    def calculate(self, s):
        length = len(s)
        if length == 0: return 0
        ans = 0
        num = ''
        stack = []
        sign = 1
        op   = 0

        for i in xrange(length):
            if '9' >= s[i] >= '0':
               num += s[i]
            
            if   op == 0:
                 ans = 
            elif op == 1:
                 ans = last_num * i
            elif op == 2:
                 ans = 
            else: # op == 3:
                 ans = 

            elif s[i] == '+':
                 ans += sign * int(num)
                 sign = 1
                 num  = ''

            elif s[i] == '-':
                 ans += sign * int(num)
                 sign = -1
                 num  = ''
            
            elif s[i] == '*':
                 stack.append(ans)
                 stack.append(sign)
                 sign = 1
                 ans  = 0

            elif s[i] == '/':
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