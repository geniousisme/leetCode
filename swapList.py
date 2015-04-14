class Solution:
    # @return a string
    def mergeSwap(self, num_list):
        num_len = len(num_list)
        if num_len == 1:
            return num_list
        if num_len == 2:
            return self.swap(*num_list)
        mid = len(num_list) / 2
        prev = mergeSwap(num_list[:mid])
        post = mergeSwap(num_list[mid:])
        while

    def swap(self, num_list):
        tmp = num_list[0]
        num_list[0] = num_list[1]
        num_list[1] = tmp
        return num_list
        

if __name__ == '__main__':
   s = Solution()
   print s.countAndSay(0)

        
            





