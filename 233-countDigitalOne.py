class Solution:
    # @param {integer} n
    # @return {integer}
    # take 
    def countDigitOne(self, n):
        # Chris:TODO::take this as reference 
        # http://www.cnblogs.com/grandyang/p/4629032.html
        res = 0; a = b = 1
        while n > 0:
              # print 'a', a
              # print 'b', b
              res += (n + 8) / 10 * a + (n % 10 == 1) * b
              # print 'res', res
              # a in charge of ten order, should add 10 or not, b in charge of the 
              # from unit to ten-th unit, (n % 10 == 1) deal with the special case, ex. 11, 111, 1111
              b   += n % 10 * a
              a   *= 10
              n /= 10
        return res

if __name__ == '__main__':
   s = Solution()
   print s.countDigitOne(11)
   print s.countDigitOne(19)

   print s.countDigitOne(56)
   print s.countDigitOne(101)
   print s.countDigitOne(111)

   print s.countDigitOne(1111)




        
