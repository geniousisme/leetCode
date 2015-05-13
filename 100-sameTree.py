# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p and q:
           return self.recurCheck(p, q)
        return False

    def recurCheck(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
           return self.recurCheck(p.right, q.right) and self.recurCheck(p.left, q.left)
        return False

        