#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    # isMatch("aa","a") → false
    # isMatch("aa","aa") → true
    # isMatch("aaa","aa") → false
    # isMatch("aa", "a*") → true
    # isMatch("aa", ".*") → true
    # isMatch("ab", ".*") → true
    # isMatch("aab", "c*a*b") → true
    def split_diff_str(self, string):
        diff_str_list = []
        start = 0
        length = len(string)
        if not string: 
           return diff_str_list
        if length == 1:
           return [string]
        for i in xrange(1, length):
            if string[i] != string[i - 1]:
               if string[i] != '*':
                  diff_str_list.append(string[start:i])
                  start = i
            if i == length - 1:
               diff_str_list.append(string[start:length])
        return diff_str_list

    def forward_to_diff_str_idx(self, idx, string):
        while string[idx] == string[idx + 1]:
              idx += 1
        return idx + 1

    def match_string_pattern(self, string, pattern):
        si = pi = 0 # string index, pattern idnex
        while pi < len(pattern):
              if pattern[pi] == string[si] or pattern[pi] == '.':
                 pi += 1
                 if pattern[pi] == '*': # means there might be a series same cha
                    si = self.forward_to_diff_str_idx(si)
                 else:
                    si += 1
              else: # current pattern != string
                 if pattern[pi + 1] == '*':
                    si += 1
                 else: # general single letter
                   if pattern[pi] != string[si]:
                      if pattern[pi + 1] == '*':
                         pi += 2
                   else:
                      pass
    def isMatch(self, string, pattern):
        if pattern.find('.') == -1 and pattern.find('*') == -1:
           return string == pattern
        elif pattern == '.*':
             return True
        else:
            string_list  = self.split_diff_str(string)
            pattern_list = self.split_diff_str(pattern)
            pi = si = 0
            p_len = len(pattern_list); s_len = len(string_list)
            while pi < p_len:
                  print "p:", pattern_list[pi]
                  print "s:", string_list[si]
                  if si >= s_len:
                     return False
                  if not (pattern_list[pi][0] == string_list[si][0] or \
                          pattern_list[pi][0] == '.'):
                     if pattern_list[pi][-1] == '*':
                        pi += 1
                     else:
                        return False
                  else: # pattern_list[pi][0] == string_list[si][0] or pattern_list[pi][0] == '.'
                    if pattern_list[pi][-1] == '*' or pattern_list[pi][-1] == '.':
                       if pi < p_len - 1:
                          pi += 1; si += 1
                       else: # at the end of 
                          return True
                    else: 

                       return False
            # if si < s_len: return False
            return True



if __name__ == '__main__':
   s = Solution()
   # string = 'aaacddde'
   # pattern = 'a*c*...'
   # print s.split_diff_str(string)
   # print s.split_diff_str(pattern)
   # print s.isMatch(string, pattern)   
   string = 'cccaabbbb'
   pattern = 'c*a*b'
   print s.forward_to_diff_str_idx(4, string)
   # print s.split_diff_str(string)
   # print s.split_diff_str(pattern)
   # print s.isMatch('aab', 'c*a*b')   


        