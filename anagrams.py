class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def __init__(self):
        self.res = []
        self.anagram_dict = {}
    
    def anagrams(self, strs):
        for string in strs:
            sorted_str = sorted(string)
            if not self.anagram_dict.get(sorted_str):
               self.anagram_dict[sorted_str] = [string]
            else:
               self.anagram_dict[sorted_str].append(string)
        
          

    # def is_anagrams(self, str1, str2):
    #     char_freq_dict = {}
    #     for s in str1:
    #         if not char_freq_dict.get(s):
    #            char_freq_dict[s] = str1.count(s)

if __name__ == '__main__':
   s = Solution()
        