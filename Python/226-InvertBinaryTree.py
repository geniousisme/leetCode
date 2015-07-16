# Definition for a binary tree node.
from ds import TreeNode

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root:
           self.invertRecursive(root) 
        return root
    
    def invertRecursive(self, root):
        if root is None:
           return
        root.right, root.left = root.left, root.right
        self.invertRecursive(root.right)
        self.invertRecursive(root.left )


if __name__ == '__main__':
   s = Solution()
   
   test = TreeNode(4)
   test.right = TreeNode(7)
   test.left  = TreeNode(2)
   test.right.right = TreeNode(9)
   test.right.left = TreeNode(6)
   test.left.right = TreeNode(3)
   test.left.left = TreeNode(1)







