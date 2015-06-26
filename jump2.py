class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def jump(self, nums):
        length = len(nums)
        last = curr = step_num = 0
        for i in xrange(length):
            print 'i:', i
            print 'last:', last
            print 'curr:', curr
            if i > last:
               print '###'
               last = curr
               print 'last:', last
               print '###'
               step_num += 1
            if i + nums[i] > curr:
               curr = i + nums[i]
        return step_num

        # for i in xrange(length):
        #     if i > last:
        #        last     = curr
        #        step_num += 1
        #     curr = max(curr, i + nums[i])


if __name__ == '__main__':
   s = Solution()
   # print s.jump([2,3,1,1,4])
   print s.jump([2, 2, 2, 1, 4])
   # print s.jump([1, 1, 1, 1, 2, 0, 0])
   # print s.jump([3, 2, 1, 0, 4])
   # print s.jump([5,9,3,2,1,0,2,3,3,1,0,0])







