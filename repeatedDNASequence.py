class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        ans = []
        valCnt = dict()
        map = {'A' : 0, 'C' : 1, 'G': 2, 'T' : 3}
        sum = 0
        for x in range(len(s)):
            sum = (sum * 4 + map[s[x]]) & 0xFFFFF
            print sum
            if x < 9:
                continue
            valCnt[sum] = valCnt.get(sum, 0) + 1
            if valCnt[sum] == 2:
                ans.append(s[x - 9 : x + 1])
        return ans

if __name__ == '__main__':
   s = Solution()
   print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")