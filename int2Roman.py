class Solution:
    # @return a string
    # Symbol  Value
    # I       1
    # V       5
    # X       10
    # L       50
    # C       100
    # D       500
    # M       1,000
    # special_dict = {
    #                 4:'IV', 
    #                 9:'IX',
    #                 40:'XL',
    #                 90:'XC',
    #                 400:'CD',
    #                 900:'CM'
    #                 }
    def intToRoman(self, num):
        final_roman = ""
        while num > 0:
            if num >= 1000:
                final_roman += 'M' * (num / 1000) 
                num %= 1000
            elif 1000 > num >= 500:
                if num / 100 == 9:
                    final_roman += 'CM'
                    num -= 900
                else:
                    final_roman += 'D' * (num / 500)
                    num %= 500
            elif 500 > num >= 100:
                if num / 100 == 4:
                    final_roman += 'CD'
                    num -= 400
                else:
                    final_roman += 'C' * (num / 100)
                    num %= 100
            elif 100 > num >= 50:
                if num / 10 == 9:
                    final_roman += 'XC'
                    num -= 90
                else:
                    final_roman += 'L' * (num / 50)
                    num %= 50
            elif 50 > num >= 10:
                if num / 10 == 4:
                    final_roman += 'XL'
                    num -= 40
                else:
                    final_roman += 'X' * (num / 10)
                    num %= 10
            elif 10 > num >= 5:
                if num == 9:
                    final_roman += 'IX'
                    num -= 9
                else:
                    final_roman += 'V' * (num / 5)
                    num %= 5
            elif 5 > num > 0:
                if num == 4:
                    final_roman += 'IV' 
                    num -= 4
                else:
                    final_roman += 'I' * num
                    num = 0
        return final_roman

s = Solution()
s.intToRoman(1000)

