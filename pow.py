class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        pow_result = 1
        negative = True if n < 0 else False
        n = abs(n)
        while n > 0:
              multiply = 1
              tmp_result = x
              while n > multiply * 2:
                    multiply   = multiply * 2
                    tmp_result = tmp_result ** 2
              n          -= multiply
              pow_result *= tmp_result
        if negative: pow_result = 1 / pow_result
        return pow_result

if __name__ == '__main__':
   s = Solution()
   print s.myPow(0, 0)