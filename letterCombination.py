class Solution:
    # @return a list of strings, [s1, s2]
    def __init__(self):
        digit_letter_dict = \
                            {
                            '0':[""],
                            '1':[""],
                            '2':['a', 'b', 'c'],
                            '3':['d', 'e', 'f'],
                            '4':['g', 'h', 'i'],
                            '5':['j', 'k', 'l'],
                            '6':['m', 'n', 'o'],
                            '7':['p', 'q', 'r', 's'],
                            '8':['t', 'u', 'v'],
                            '9':['w', 'x', 'y', 'z']
                            }
    def letterCombinations(self, digits):

        for digit in digits:
            