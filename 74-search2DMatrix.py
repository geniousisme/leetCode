class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row_num = len(matrix)
        col_num = len(matrix[0])
        sorted_1D_list = []
        for i in xrange(row_num):
            sorted_1D_list.extend(matrix[i])
        return self.binarySearch(sorted_1D_list, 0, row_num * col_num, target)

    def binarySearch(self, nums, start, end, target):
        if len(nums[start:end]) == 1:
           return nums[start] == target
        mid = (end + start) / 2
        if target > nums[mid]:
           return self.binarySearch(nums, mid, end, target)
        elif target < nums[mid]:
             return self.binarySearch(nums, start, mid, target)
        else: # target == nums[mid]
             return True





if __name__ == '__main__':
   s = Solution()
   # matrix = [                   \
   #            [1,   3,  5,  7], \
   #            [10, 11, 16, 20], \
   #            [23, 30, 34, 50]  \
   #          ]
   # print s.searchMatrix(matrix, 3)
   nums = [1, 2, 4, 6, 9, 10]
   print s.binarySearch(nums, 0, len(nums), 11)
