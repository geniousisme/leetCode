class Solution:
    # @param {integer} n
    # @return {integer[]}
    def myGrayCode(self, n):
        code_list = [0]
        curr_code = '0' * n
        # print 'code', curr_code
        for i in xrange(1, 2 ** n):
            if i % 2 == 1:
               # last = '1' if prev_code[-1] == '0' else '0'
               curr_code = self.not_convert(curr_code, n - 1)
            else: # i % 2 == 0
               idx = n - 1
               while curr_code[idx] != '1':
                     idx -= 1
               curr_code = self.not_convert(curr_code, idx - 1)
            # print curr_code
            code_list.append(int(curr_code, 2))
        return code_list
    
    def not_convert(self, code, idx):
        # print 'idx', idx
        # print code[:idx]
        # print code[idx + 1:]
        return code[:idx] + ('1' if code[idx] == '0' else '0') + code[idx + 1:]
    
    def grayCode(self, n):
        res = []
        size = 1 << n
        for i in xrange(size):
            res.append(i >> 1 ^ i)
        return res

if __name__ == '__main__':
   s = Solution()
   print s.grayCode(3)