class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        neg_flag     = numerator * denominator < 0
        numerator    = abs(numerator)
        denominator  = abs(denominator)
        num_pos_dict = {}
        loop_str     = ""
        quotient_list = []
        end = 0
        while True:
              quotient_list.append(str(numerator / denominator))
              # key diff between my and his, use this value can avoid the repeated situation
              numerator = 10 * (numerator % denominator)
              # print numerator
              end += 1
              if numerator == 0: 
                 break
              start = num_pos_dict.get(numerator)
              if start is not None:
                 loop_str = "".join(quotient_list[start:end])
                 # print loop_str
                 break
              num_pos_dict[numerator] = end
        res = quotient_list[0]
        if len(quotient_list) > 1:
           res += '.'
        if loop_str:
           res += "".join(quotient_list[1:len(quotient_list) - len(loop_str)]) + '(' + loop_str + ')'
        else:
           res += "".join(quotient_list[1:])
        if neg_flag: res = '-' + res
        return res

if __name__ == '__main__':
   s = Solution()
   print s.fractionToDecimal(2, 3)
   print s.fractionToDecimal(2, 5)
                 
        