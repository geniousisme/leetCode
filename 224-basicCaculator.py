class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        ans = 0
        stack = []
        s = s + ' '
        length = len(s)
        numStart = -1; numEnd = length
        last = 1
        for i in xrange(length):
            # print 's', s[i]
            if s[i] in '0123456789':
               if numEnd < 0:
                  continue
               # print 's: |' + s[i] + '|'
               numStart = i
               numEnd   = -1
            else:
               
               if numStart < 0:
                  if s[i] == '-':
                     last = -1
                  continue
               numEnd = i
               if s[numStart:numEnd]:
                  # print 'numStart', numStart
                  # print 'i', i
                  ans += last * int(s[numStart:i])
                  numStart = -1
                  last = 1
               if s[i] == '-':
                  last = -1
            # print stack
            # print '----------------'          
        return ans
                 
           

            

if __name__ == '__main__':
   s = Solution()
   print s.calculate('234567890')
   print s.calculate("1 + 1")
   print s.calculate(" 2-1 + 2 ")
   print s.calculate("(1+(4+5+2)-3)+(6+8)")