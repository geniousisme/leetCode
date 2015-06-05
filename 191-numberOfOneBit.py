class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        bit_num = 0
        # bit_str = ''
        for i in xrange(31, -1, -1):
            if 2 ** i > n:
               # bit_str += '0'
               continue
            bit_num += 1
            # bit_str += '1'
            n -= 2 ** i
        return bit_num

if __name__ == '__main__':
   s = Solution()
   print s.hammingWeight(11)
   print s.hammingWeight(0)
   print s.hammingWeight(1)
   print s.hammingWeight(32)
   print s.hammingWeight(110)





