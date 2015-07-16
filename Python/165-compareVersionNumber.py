class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        len1 = len(v1_list)
        len2 = len(v2_list)
        length = self.makeEqualLength(v1_list, v2_list, len1, len2)
        for i in xrange(length):
            if int(v1_list[i]) > int(v2_list[i]):
                return 1
            elif int(v2_list[i]) > int(v1_list[i]):
                return -1
        return 0

    def makeEqualLength(self, list1, list2, len1, len2):
        if len1 > len2:
            diff = len1 - len2
            for i in xrange(diff):
                list2.append('0')
            return len1
        elif len2 > len1:
            diff = len2 - len1
            for i in xrange(diff):
                list1.append('0')
            return len2
        else:
            return len1

if __name__ == '__main__':
   s = Solution()
   version1 = '1.1'
   version2 = '0.1'
   print s.compareVersion(version1, version2)
   version2 = '1.3.3.4'
   version1 = '1.3.4'
   print s.compareVersion(version1, version2)

   

