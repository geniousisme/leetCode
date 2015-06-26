class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        result_binary = str(int(a) + int(b))
        result_binary = [int(b) for b in result_binary]
        result_binary.insert(0, 0)
        length        = len(result_binary)
        carry         = 0
        for i in xrange(length - 1, -1, -1):
            result_binary[i] += carry
            if result_binary[i] > 1: # only can be 2 or 3
               result_binary[i] -= 2
               carry = 1
            else:
               carry = 0
        if result_binary[0] == 0:
           result_binary = result_binary[1:]
        return ''.join([str(rb) for rb in result_binary])
                

if __name__ == '__main__':
   s = Solution()
   a = '111'
   b = '1'
   print s.addBinary(a, b)