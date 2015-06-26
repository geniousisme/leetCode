class Solution:
    # @return a boolean
    def __init__(self):
        self.parentheses_idx_dict = \
                                  { 
                                    '(': [],
                                    '[': [],
                                    '{': []
                                  }
    
    def valid_parenthesis(self, pre_parenth, idx):
        # check if idx_list is not empty, (empty mean pair is wrong)
        # and if there is event numbers of str between two parentheses (odd numbers means pair wrong)
        return self.parentheses_idx_dict[pre_parenth] and \
              (idx - self.parentheses_idx_dict[pre_parenth].pop() - 1) % 2 == 0
    
    def isValid(self, s):
        if not s or len(s) % 2 == 1:
           return False
        for idx, parenthesis in enumerate(s):
            if parenthesis == ')':
               if not self.valid_parenthesis('(', idx):
                  return False
            elif parenthesis == ']':
                 if not self.valid_parenthesis('[', idx):
                    return False
            elif parenthesis == '}':
                 if not self.valid_parenthesis('{', idx):
                    return False
            else:
                self.parentheses_idx_dict[parenthesis].append(idx)
        for parenthesis_idx_list in self.parentheses_idx_dict.values():
            if parenthesis_idx_list: # if there are still left elems in list, means wrong
               return False
        return True

if __name__ == "__main__":
   import time
   start = time.clock()
   s = Solution()
   test = '{[()]}[]()[]'
   print s.isValid(test)
   test = '{[()]}[](])[()]'
   print s.isValid(test)
   test = '[(])'
   print s.isValid(test)
   test = '['
   print s.isValid(test)
   test = ''
   print s.isValid(test)
   print "%s sec" % (time.clock() - start)
