# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def __init__(self):
        self.stack = []
        self.res   = []

    def inorderTraversal(self, root):
        self.recursive_traverse(root)
        return self.res

    def recursive_traverse(self, node):
        if node:
           self.recursive_traverse(node.left)
           self.res.append(node.val)
           self.recursive_traverse(node.right)
        return

    def iterTraverse(self, root):
        while root or self.stack:
              if root:
                 self.stack.append(root)
                 root = root.left
              else:
                 root = self.stack.pop()
                 self.res.append(root.val)
                 root = root.right
        return

  