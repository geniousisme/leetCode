class Solution:
    # @return an integer
    def __init__(self):
        self.roman_int_dict = \
                            {
                               'I' :   1,
                               'V' :   5,
                               'X' :  10,
                               'L' :  50,
                               'C' : 100,
                               'D' : 500,
                               'M' :1000
                            }
    
    def romanToInt(self, s):
        final_int = 0
        for i in xrange(0, len(s) - 1):
            if self.roman_int_dict[s[i]] < self.roman_int_dict[s[i + 1]]:
                final_int -= self.roman_int_dict[s[i]]
            else:
                final_int += self.roman_int_dict[s[i]]
        final_int += self.roman_int_dict[s[len(s) - 1]]
        return final_int


s = Solution()
s.romanToInt('MDCCCXCIX')