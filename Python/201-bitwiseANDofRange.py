class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        count = 0
        while m != n:
              m >>= 1
              n >>= 1
              count += 1
        return n << count
