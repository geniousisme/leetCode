class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        ans = 0
        stack = []
        last = '+'
        numStart = numEnd = 0
        for i in xrange(len(s)):
            if last 
            if s[i] in '0123456789':
               numStart = i
            else:
               numEnd = i
               if s[i] == '-':
                  last = -1
               else:
                  last = 1
               
            last * int(s[numStart:numEnd])

               

if __name__ == '__main__':
   s = Solution()
   print s.calculate("")
   print s.calculate("1 + 1")
   print s.calculate(" 2-1 + 2 ")
   print s.calculate("(1+(4+5+2)-3)+(6+8)")