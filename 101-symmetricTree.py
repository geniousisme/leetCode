# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root:
           return self.recursiveJudge(root.left, root.right)
        return True
    

    def recursiveJudge(self, l, r):
        if l == None and r == None: return True
        if l and r and l.val == r.val: 
           return self.recursiveJudge(l.right and r.left) and self.recursiveJudge(l.left, r.right)
        return False
