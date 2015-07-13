# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
           return None
        
        if root == p or root == q:
           return root
        
        left_ancestor  = self.lowestCommonAncestor(root.left, p, q)
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)

        if left_ancestor and right_ancestor:
           return root

        return [left_ancestor, right_ancestor][left_ancestor is None]

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(6)
   test.left = TreeNode(2)
   test.right = TreeNode(8)
   test.left.left = TreeNode(0)
   test.left.right = TreeNode(4)
   test.right.left = TreeNode(7)
   test.right.right = TreeNode(9)

   print s.lowestCommonAncestor(test, test.left, test.left.left).val
        