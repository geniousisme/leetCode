class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        i = 1
        zero_num = 0
        five_num = n / pow(5, i)
        while five_num > 0:
              zero_num += five_num
              i += 1
              five_num = n / pow(5, i)
        return zero_num

if __name__ == '__main__':
   print Solution().trailingZeroes(101)