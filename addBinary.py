class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        result_binary = str(int(a) + int(b))
        result_binary = [int(b) for b in result_binary]
        length        = len(result_binary)
        carry         = 0
        result_binary.insert(0, 0)
        for i in xrange(length - 1, -1, -1):
            result_binary[i] += carry
            if result_binary[i] > 2:
               result_binary[i] -= 2
               carry = 1
            else:
               carry = 0

1111
1111

02222
11110

        