class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = ''
        for i in xrange(31, -1, -1):
            number = 2 ** i
            if n < number:
               bits = '0' + bits 
               continue
            n -= number
            bits = '1' + bits
        return int(bits, 2)


if __name__ == '__main__':
   s = Solution()
   print s.reverseBits(43261596)




        