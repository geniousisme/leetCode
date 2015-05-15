# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        return self.traversal(root, 0)

    def traversal(self, node, depth):
        if node is None:
           return depth
        return max(self.traversal(node.left, depth + 1), self.traversal(node.right, depth + 1))

    def seniorMaxDepth(self, root):
        if root is None: 
           return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1