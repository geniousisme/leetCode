#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    # 把 list 拆成 2^X 的集合，然後個別 swap 之後再合併
    
    def swapList(self, num_list): # 合併 array
        num_two_sqrt_list = self.divide_two_pow(num_list, len(num_list))
        final_list = []
        for num_list in num_two_sqrt_list:
            final_list.extend(self.mergeSwap(num_list))
        return final_list
        # cool code in one line, but it is slower actually
        # return [num for num_list in num_two_sqrt_list for num in self.mergeSwap(num_list)]
    
    def mergeSwap(self, num_list): # 把 2 次方的 array 兩兩相鄰的對調
        result = []
        num_len = len(num_list)
        if num_len == 1:
            return num_list
        if num_len == 2:
            return self.swap(num_list)
        mid = len(num_list) / 2
        prev = self.mergeSwap(num_list[:mid])
        post = self.mergeSwap(num_list[mid:])
        result.extend(prev)
        result.extend(post)
        return result

    def divide_two_pow(self, num_list, num_len): # 找出 array 是幾個 2 次方數的集合，ex. 14 = 2 ** 3 + 2 ** 2 + 2
        result = []; start = 0
        while num_len > 0:
              if 3 > num_len > -1:
                 result.append(num_list[start:start + num_len])
              if num_len > 2:
                 power = 0; quotient = num_len
                 while quotient > 1:
                       quotient /= 2
                       power += 1
                 length = 2 ** power
                 result.append(num_list[start:start + length])
                 start += length
              num_len -= length
        return result
        
    def swap(self, num_list): # 兩兩相鄰元素對調
        tmp = num_list[0]
        num_list[0] = num_list[1]
        num_list[1] = tmp
        return num_list
        

if __name__ == '__main__':
   s = Solution()
   arr = range(0, 12)
   print s.swapList(arr)
   # print s.mergeSwap(arr)
   # print s.divide_two_pow(6)
   # print s.divide_two_pow(arr, len(arr))
   # print s.divide_two_pow(10)
   # print s.divide_two_pow(12)
   # print s.divide_two_pow(14)
   # print s.divide_two_pow(16)
   # print s.divide_two_pow(20)
   # print s.divide_two_pow(17)

        
            





