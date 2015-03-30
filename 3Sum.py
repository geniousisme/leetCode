class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        three_sum_list = []
        if len(num) < 3:
            return []
        elif [0] * len(num) == num:
            return [[0] * 3]
        num = sorted(num)
        idx = self.get_positive_zero_idx(num)
        if idx == None or idx == 0: 
            return []
        # if num[idx] == 0: 
        # # if we hv 0 in list, then we only need to find only 
        # # need to find negative & positive pair for sum, ex. (-2, 0, 2)
        # if we hv no zero in list, then we hv two pattern for three sum
        # (-, -, +) & (-, +, +), ex.(-1, -2, 3) & (-4, 2, 2)
        for ni, n in enumerate(num[:idx + 1]):
            for pi, p in enumerate(num[idx:]):
                if -(p + n) in num[idx + pi + 1:]:
                    if [n, p, -(p + n)] not in three_sum_list:
                        three_sum_list.append([n, p, -(p + n)])
                if -(p + n) in num[ni + 1:idx]:
                    if [n, -(p + n), p] not in three_sum_list:
                        three_sum_list.append([n, -(p + n), p])
        return three_sum_list

    def get_positive_zero_idx(self, num):
        for i, n in enumerate(num):
            if n >= 0:
                return i

##### find of dead end, too many cases to solve, change to another one #####
    
if __name__ == "__main__":
    import time
    start = time.clock()
    s = Solution()
    num = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print s.threeSum(num)
    print "%s sec" % (time.clock() - start)
    
    # def binarySearch(self, numList, num):
    #     length = len(numList)
    #     if length == 1:
    #         return 
    #     elif numList[length / 2:][0] < num:
    #         numList = numList[length / 2:]
    #         return binarySearch(numList, num)
    #     elif numList[length / 2:][0] > num:
    #         numList = numList[:length / 2]
    #         return binarySearch(numList, num)
    #     else:  
    #         return numList.index(num)



        