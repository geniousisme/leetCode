class Solution:
    # @param {integer} n
    # @return {integer}
    # take 
    def countDigitOne(self, n):
        res = 0; a = b = 1
        while n > 0:
              print 'a', a
              print 'b', b
              res += (n + 8) / 10 * a + (n % 10 == 1) * b
              b   += n % 10 * a
              a   *= 10
              n /= 10
        return res

if __name__ == '__main__':
   s = Solution()
   print s.countDigitOne(11)
   print s.countDigitOne(56)
   print s.countDigitOne(101)
   print s.countDigitOne(1111)




        
