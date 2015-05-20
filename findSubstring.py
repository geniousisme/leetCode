class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    # def __init__(self):
    #     self.word_length   = 0
    #     self.words_length  = 0
    #     self.word_comb_len = 0
    #     self.res           = []
    #     # self.alphabet_comb_dict = {}
    def findSubstring(self, s, words):
        word_length   = len(words[0])
        words_length  = len(words)
        word_comb_len = word_length * words_length
        res           = []
        for idx in xrange(len(s) - word_comb_len + 1):
            seg = [s[i:i + word_length] for i in xrange(idx, idx + word_comb_len, word_length)]
            for comb in words:
                if comb in seg:
                   seg.remove(comb)
                else:
                   break
            if not seg:
               res.append(idx)
        return res

    #     word_perm_list     = self.permuate(words)
    #     word_idx_list      = []
    #     # print 'word_perm_list', word_perm_list
    #     for word_perm in word_perm_list:
    #         if not self.alphabet_comb_dict.get(word_perm[0]):
    #            self.alphabet_comb_dict[word_perm[0]] = [word_perm]
    #         else:
    #            self.alphabet_comb_dict[word_perm[0]].append(word_perm)
    #     for i in xrange(0, len(s), self.word_length):
    #         if s[i] in self.alphabet_comb_dict:
    #            if s[i:i + self.word_comb_len] in self.alphabet_comb_dict[s[i]]:
    #               word_idx_list.append(i)
    #            else:
    #               break
    #         else:  
    #            break
    #     return word_idx_list

    # def permuate(self, words):
    #     if not words:
    #        return words
    #     self.DFS("", words)
    #     return self.res

    # def DFS(self, comb, left_words):
    #     if len(comb) == self.word_comb_len:
    #        self.res.append(comb)
    #        return
    #     else:
    #        for i in xrange(len(left_words)):
    #            self.DFS(comb + left_words[i], left_words[:i] + left_words[i + 1:])

if __name__ == '__main__':
   s = Solution()
   # print s.permuate(['foo', 'bar', 'lol'])          
   print s.findSubstring("brfoothefobarman", ['foo', 'bar'])