class Solution:
    # @return an integer
    def maxArea(self, height):
        left = max_area = 0; right = len(height) - 1
        while left != right:
              tmp_area = min(height[left], height[right]) * (right - left)
              if tmp_area > max_area:
                 max_area = tmp_area
              if height[left] < height[right]:
                 left  += 1
              else:
                 right -= 1
        return max_area

# from maxArea import Solution
# s = Solution()
# s.maxArea([1,2,3,4]) 
# s.maxArea([2,2,3,6]) 