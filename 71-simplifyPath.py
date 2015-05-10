class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        path_list = path.split('/')
        print path_list
        simp_path = []
        for i in xrange(len(path_list)):
            # print 'simp_path:', simp_path
            if not path_list[i] or path_list[i] == '.': # path[i] == ''
               # simp_path.append('')
               continue
            # elif path_list[i] == '.':
            #      continue
            elif path_list[i] == '..':
                 if simp_path:
                    simp_path.pop()
            else:
                 # simp_path.append()
                 simp_path.append('/' + path_list[i])
            # print simp_path
        res = ''.join(simp_path)
        if not res:
           return '/'
        else:
           return res
        
if __name__ == '__main__':
   s = Solution()
   print s.simplifyPath("/a/./b/../../c/")
   print s.simplifyPath("/home/")
   print s.simplifyPath("/home/foo/etc/../../usr")
   print s.simplifyPath('/home//foo/')
   print s.simplifyPath('/../')
   print s.simplifyPath("/home/../../..")
   print s.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")