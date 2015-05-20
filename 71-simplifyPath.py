class Solution:
    # @param {string} path
    # @return {string}
    def mySimplifyPath(self, path):
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

    def simplifyPath1(self, path): # purely by idx
        stack = []
        i = 0
        res = ''
        while i < len(path):
            end = i+1
            while end < len(path) and path[end] != "/":
                end += 1
            sub=path[i+1:end]
            if len(sub) > 0:
                if sub == "..":
                    if stack != []: stack.pop()
                elif sub != ".":
                    stack.append(sub)
            i = end
        if stack == []: return "/"
        for i in stack:
            res += "/"+i
        return res

    def simplifyPath2(self, path):
        path = path.split('/')
        curr = '/'
        for i in path:
            if i == '..':
                if curr != '/':
                    curr = '/'.join(curr.split('/')[:-1])
                    if curr == '': curr = '/'
            elif i != '.' and i != '':
                curr += '/' + i if curr != '/' else i
        return curr
        
if __name__ == '__main__':
   s = Solution()
   print s.simplifyPath("/a/./b/../../c/")
   print s.simplifyPath("/home/")
   print s.simplifyPath("/home/foo/etc/../../usr")
   print s.simplifyPath('/home//foo/')
   print s.simplifyPath('/../')
   print s.simplifyPath("/home/../../..")
   print s.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")