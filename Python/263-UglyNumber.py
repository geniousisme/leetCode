class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
           return False
        while num > 1:
              print "num", num
              if num % 2 == 0:
                 num /= 2
                 continue
              elif num % 3 == 0:
                   num /= 3
                   continue
              elif num % 5 == 0:
                   num /= 5
                   continue
              else:
                   return False
        return True

if __name__ == '__main__':
   s = Solution()
   print s.isUgly(6)
   print s.isUgly(8)
   print s.isUgly(14)
   print s.isUgly(-2147483648)
