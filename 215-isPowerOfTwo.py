class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        binary_str = '{0:b}'.format(n)
        if binary_str[0] != '1': 
           return False
        for i in xrange(1, len(binary_str)):
            if binary_str[i] != '0':
               return False
        return True 

