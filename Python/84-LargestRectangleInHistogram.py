class Solution:
    # @param {integer[]} height
    # @return {integer}
    # Chris::TODO: need to review this problem again!
    
    def largestRectangleArea(self, heights):        
        heights.append(0)
        idx = max_area = 0
        rect_stack = []
        length = len(heights)
        while idx < length:
              if not rect_stack or heights[idx] > heights[rect_stack[-1]]:
                 rect_stack.append(idx)
                 idx += 1
              else:
                 prev_idx = rect_stack.pop()
                 width = idx if not rect_stack else idx - rect_stack[-1] - 1
                 max_area = max(max_area, heights[prev_idx] * width)
              print 'i', idx, 'stack:', rect_stack, 'area', max_area
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
#                 # print area
#             print 'i', i, 'stack:', stack, 'area', area
#         return area

if __name__ == '__main__':
   s = Solution()
   print s.largestRectangleArea([2,1,5,6,2,3])
   print s.largestRectangleArea([2, 4, 2, 1])
   print s.largestRectangleArea([1,2,2])













        