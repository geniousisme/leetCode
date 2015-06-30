class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstringTwoDistinct(self, s):
        
        two_word_dict     = {}
        distinct_count    = 0
        max_len = tmp_len = 0
        diff_idx          = 0
        if s:
           for i in xrange(len(s)):
               if two_word_dict.get(s[i], False):
                  tmp_len += 1
                  # diff_idx = i
               else:
                  distinct_count += 1
                  if distinct_count > 2:
                     two_word_dict = {}
                     two_word_dict[s[i]] = True
                     two_word_dict[s[i - 1]] = True
                     if s[diff_idx] != s[i - 1]:
                        diff_idx = i - 1
                     tmp_len = 1 + i - diff_idx
                     diff_idx = i
                  else:                     
                     diff_idx = i
                     # print 'diff_idx', diff_idx
                     two_word_dict[s[i]] = True
                     tmp_len += 1
               # print s[i], 'tmp_len', tmp_len
               max_len = max(max_len, tmp_len)
        return max_len

if __name__ == '__main__':
   s = Solution()
   print s.lengthOfLongestSubstringTwoDistinct('eceba')
   # print s.lengthOfLongestSubstringTwoDistinct('eecebaaaaa')
   # print s.lengthOfLongestSubstringTwoDistinct('ee')
   print s.lengthOfLongestSubstringTwoDistinct("abaccc")
   print s.lengthOfLongestSubstringTwoDistinct('ccaabbb')




