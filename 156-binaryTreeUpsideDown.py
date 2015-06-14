# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
# Chris:TODO::write following again, so sleepy.
class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        parent = None
        parent_left = None
        while root:
              left = root.left
              right = root.right
              root.left = parent
              parent = root
              root.right = parent_left
              parent_left = right
              root = left
        return parent

if __name__ == '__main__':
   s = Solution()
   
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.left.right = TreeNode(5)

   print s.upsideDownBinaryTree(test)



