class Solution:
    # @param {string} s
    # @return {integer}
    # Chris::TODO: take this as reference:
    # http://www.wengweitao.com/leetcode-basic-calculator.html
    def calculate(self, s):
        length = len(s)
        if length == 0: 
           return 0
        ans = last_num = op = i = 0
        num = ''
        sign = 1
        # op = 0: +, -
        # op = 1: *
        # op = 2: /
        while i < length:
            if s[i] == ' ':
               i += 1
               continue
            
            if '9' >= s[i] >= '0':
                num = ''
                while i < length and '9' >= s[i] >= '0':
                      num += s[i]
                      i += 1
                i -= 1
                if op == 1:
                   last_num *= int(num)
                elif op == 2:
                     last_num /= int(num)
                else: # op == 0, +, -
                     last_num = int(num)

            if s[i] == '+':
               ans += sign * last_num
               op   = 0 
               sign = 1

            elif s[i] == '-':
                 ans += sign * last_num
                 op   = 0
                 sign = -1
            
            elif s[i] == '*':
                 op   = 1
                 
            elif s[i] == '/':
                 op   = 2
            
            i += 1
        
        ans += sign * last_num

        return ans
            

if __name__ == '__main__':
   s = Solution()
   # print s.calculate("3+2*2")
   # print s.calculate(" 3/2 ")
   # print s.calculate(" 3+5 / 2 ")
   print s.calculate("2*3+4")

   