class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    
    def nextPermutation(self, num):
        length = len(num); end = length - 1; partition = -1
        for i in xrange(end, 0, -1):
            if num[i] > num[i - 1]:
               partition = i - 1
               break        
        if partition == -1:
           self.reverse(num, 0, end)
           return
        for i in xrange(end, partition, -1):
            if num[i] > num[partition]:
               self.swap_in_list(num, i, partition)
               break
        self.reverse(num, partition + 1, end)            

    def reverse(self, lst, start, end):
        while end >= start:
              self.swap_in_list(lst, start, end)
              end   -= 1
              start += 1
    
    def swap_in_list(self, lst, idx1, idx2):
        tmp       = lst[idx1] 
        lst[idx1] = lst[idx2]
        lst[idx2] = tmp


if __name__ == '__main__':
   s = Solution()
   test_lst = [3,2,1]
   # test_lst = [1, 4, 5, 3, 2]
   # print s.reverse(test_lst, 2, 4)
   s.nextPermutation(test_lst)
   print test_lst