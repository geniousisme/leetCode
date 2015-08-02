class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagramI(self, s, t):
        slst = list(s)
        tlst = list(t)
        slst.sort()
        tlst.sort()
        return slst == tlst

    def isAnagram(self, s, t):
        sdict = {}; tdict = {}
        for word in s:
            sdict[word] = sdict.get(word, 0) + 1
        for word in t:
            tdict[word] = tdict.get(word, 0) + 1
        for key in sdict:
            telem = tdict.pop(key, None)
            if telem is None:
               return False
            elif telem != sdict[key]:
                 return False
        return tdict == {}


