class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dictionary = {'A' : 0, 'C': 1, 'G' : 2, 'T' : 3}
        res = []
        sum = 0
        seq_val_freq = {}
        for i in xrange(len(s)):
            sum = (sum * 4 + dictionary[s[i]]) & 0xFFFFF
            if i < 9:
               continue
            seq_val_freq[sum] = seq_val_freq.get(sum, 0) + 1
            if seq_val_freq[sum] == 2:
               res.append(s[i - 9:i + 1])
        return res
    
    # Chris:TODO:: write a pure dictionary version without bit manipulation

if __name__ == '__main__':
   s = Solution()
   print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")