class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    # Chris::TODO:find some faster way to deal with this prob & review again, so sleepy.
    def ladderLength(self, beginWord, endWord, wordDict):
        wordDict.add(endWord)
        queue = [(beginWord, 1)]
        while queue:
              currword, currlen = queue.pop(0)
              if currword == endWord: return currlen
              for i in xrange(len(currword)):
                  for alphabet in 'abcdefghijklmnopqrstuvwxyz':
                      if alphabet != currword[i]:
                         nextword = currword[:i] + alphabet + currword[i + 1:]
                         if nextword in wordDict:
                            queue.append((nextword, currlen + 1))
                            wordDict.remove(nextword)                      
        return 0

if __name__ == '__main__':
   s = Solution()
   beginWord = 'hit'
   endWord = 'cog'
   wordDict = ["hot","dot","lot","log"]
   print s.ladderLength(beginWord, endWord, wordDict)
   beginWord = 'a'
   endWord = 'c'
   wordDict = ['a', 'b', 'c']
   print s.ladderLength(beginWord, endWord, wordDict)
  