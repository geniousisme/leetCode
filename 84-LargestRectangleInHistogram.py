class rectangle:
      def __init__(self, height, index):
          self.height = height
          self.index  = index

# Chris::TODO: figure put what the hell this algo is!!! fxck!

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, heights):        
        rect_stack = []
        max_area = i  = 0
        heights.append(0)
        
        while i < len(heights):
              curr_rect = rectangle(heights[i], i)
              if not rect_stack or curr_rect.height > rect_stack[-1].height:
                 rect_stack.append(curr_rect)
                 i += 1
              else:
                 rect  = rect_stack.pop()
                 width = [curr_rect.index - rect.index - 1, i][not rect_stack]
                 print 'width', width
                 max_area = max(max_area, rect.height * width)
        return max_area

# class Solution:
#     # @param height, a list of integer
#     # @return an integer
#     def largestRectangleArea(self, height):
#         stack, area, i = [], 0, 0
#         height.append(0)
#         while i < len(height):
#             if stack == [] or height[i] > height[stack[-1]]:
#                 stack.append(i)
#                 i += 1
#             else:
#                 curr = stack.pop()
#                 width = i if stack == [] else i - (stack[-1] + 1)
#                 area = max(area, height[curr] * width)
#                 print area
#         return area

if __name__ == '__main__':
   s = Solution()
   print s.largestRectangleArea([2,1,5,6,2,3])
   print s.largestRectangleArea([2, 4, 2, 1])
   print s.largestRectangleArea([1,2,2])













        