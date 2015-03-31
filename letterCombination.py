class Solution:
    # @return a list of strings, [s1, s2]
    def __init__(self):
        self.digit_letter_dict = \
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
    def letter_comb_merge(self, digits, letter_comb_list):
        tmp_comb_list = [] if len(letter_comb_list) >= 1 else digits
        for digit in digits:
            tmp_comb_list += [letter_comb + digit for letter_comb in \
                              letter_comb_list]
        return tmp_comb_list


    def letterCombinations(self, digits=""):
        letter_comb_list = []
        for digit in digits:
            letter_comb_list = self.letter_comb_merge                 \
                                    (                                 \
                                        self.digit_letter_dict[digit],\
                                        letter_comb_list              \
                                    )
        return letter_comb_list

if __name__ == "__main__":
    import time
    start = time.clock()
    s = Solution()
    result = s.letterCombinations()
    print result
    print "%s sec" % (time.clock() - start)
    print "length:", len(result)
 

        