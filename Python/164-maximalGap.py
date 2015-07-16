class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if not nums:
           return 0
        max_num = max(nums); min_num = min(nums)
        length  = len(nums)
        if length < 2: return 0
        bucket_range  = max(1, ((max_num - min_num - 1) / (length - 1)) + 1)
        bucketlen     = (max_num - min_num) / bucket_range + 1
        bucketlist    = [None for i in xrange(bucketlen)]
        for num in nums:
            bucket_idx = (num - min_num) / bucket_range
            if bucketlist[bucket_idx] is None:
               bucketlist[bucket_idx] = {'max': num, 'min': num}
            else:
               bucketlist[bucket_idx]['max'] = max(bucketlist[bucket_idx]['max'], num)
               bucketlist[bucket_idx]['min'] = min(bucketlist[bucket_idx]['min'], num)
        maxGap = i = 0
        # for i in xrange(bucketlen):
        while i < bucketlen:
              if bucketlist[i] is None:
                 continue
              next_i = i + 1
              while next_i < bucketlen and bucketlist[next_i] is None:
                    next_i += 1
              if next_i < bucketlen:
                 maxGap = max(maxGap, bucketlist[next_i]['min'] - bucketlist[i]['max']) # since we need to find out the biggest diff between two neighbors after sorted
              i = next_i
        return maxGap

    def sortedMaximumGap(self, nums):
        nums.sort()
        maxGap = 0
        for i in xrange(1, len(nums)):
            maxGap = max(maxGap, nums[i] - nums[i - 1])
        return maxGap

if __name__ == '__main__':
   s = Solution()
   print s.maximumGap([3, 4, 10, 11, 23, 2, 100])
   print s.maximumGap([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740])




