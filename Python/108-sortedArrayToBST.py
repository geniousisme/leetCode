# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        return self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, start, end):
        if start > end: return None
        mid = (start + end) / 2
        root = TreeNode(nums[mid]) 
        root.right = self.buildTree(nums, mid + 1, end)
        root.left  = self.buildTree(nums, start, mid - 1)
        return root

if __name__ == '__main__':
   s = Solution()
   print s.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8])

