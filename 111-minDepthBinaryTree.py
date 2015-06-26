# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root:
           return self.minDepthTraversal(root)
        return 0

    def minDepthTraversal(self, root):
        if root is None:
           return float('inf')
        if root.right is None and root.left is None:
           return 1
        # print 'right:', self.minDepth(root.right)
        # print 'left:', self.minDepthTraversal(root.left)
        return min(self.minDepthTraversal(root.right), self.minDepthTraversal(root.left)) + 1

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(0)
   # test.right = TreeNode(2)
   # test.right.right = TreeNode(3)
   print s.minDepth(test)