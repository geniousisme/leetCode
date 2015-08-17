class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigitsI(self, num):
        if num == 0:
           return 0
        return num - 9 * ((num - 1) / 9)
    
    def addDigits(self, num):
        res = 10
        while res > 9:
              res = 0
              while num > 0:
                    res += num % 10
                    num /= 10
              num = res              
        return res


if __name__ == '__main__':
   s = Solution()
   print s.addDigits(182)
   print s.addDigits(11)
   print s.addDigits(22)
   print s.addDigits(9)


