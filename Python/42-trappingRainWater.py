class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        length       = len(height)
        if length == 0: return 0
        left_max_bar = water = 0
        left_max_bar_heights = []
        
        for i in xrange(length):
            if height[i] > left_max_bar:
               left_max_bar = height[i]
            left_max_bar_heights.append(left_max_bar)

        right_max_bar = 0

        for i in xrange(length - 1, -1, -1):
            if height[i] > right_max_bar:
               right_max_bar = height[i]
            water += min(left_max_bar_heights[i], right_max_bar) - height[i]
        return water

if __name__ == '__main__':
   s = Solution()
   print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])


