class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1   = (C - A) * (D - B)
        area2   = (G - E) * (H - F)
        if E >= C or F >= D or A >= G or B >= H:
           overlap = 0
        else:
           overlap = self.overlapLen([A, E, C, G]) * self.overlapLen([D, H, B, F])
        return area1 + area2 - overlap
    
    def overlapLen(self, nums):
        nums.sort()
        return nums[2] - nums[1]


if __name__ == '__main__':
   s = Solution()
   print s.computeArea(0,0,0,0, -2, -2, 2, 2)
   print s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
   print s.computeArea(-2, -2, 2, 2, -4, -4, -3, -3)
