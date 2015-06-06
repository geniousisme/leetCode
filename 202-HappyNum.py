class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        happy_hash = {}
        while n != 1:
            n = self.sqrtDigitSum(n)
            happy_hash[n] = happy_hash.get(n, 0) + 1
            if happy_hash[n] > 1:
               return False
        return True

    def sqrtDigitSum(self, n):
        return sum([int(n) ** 2 for n in list(str(n))])

if __name__ == '__main__':
   s = Solution()
   print s.isHappy(19)
   print s.isHappy(20)
   print s.isHappy(18)

