# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def __init__(self):
        self.res = []
    
    def levelOrderBottom(self, root):
        self.travserse(1, root)
        return self.res
        
    def travserse(self, level, node):
        if node:
           if len(self.res) < level: 
              self.res.insert(-level, [])
           self.res[-level].append(node.val)
           self.travserse(level + 1, node.left)
           self.travserse(level + 1, node.right)
        return

