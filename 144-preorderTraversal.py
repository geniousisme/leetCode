# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        res = []
        if root:
           self.iterPreorderVisit(root, res)
        return res
    
    def recPreorderVisit(self, root, res):
        if root:
           res.append(root.val)
           self.preorderVisit(root.left, res)
           self.preorderVisit(root.right, res)
        return

    def iterPreorderVisit(self, root, res):
        stack = []
        while root or stack:
              if root:
                 res.append(root.val)
                 stack.append(root)
                 root = root.left
              else:
                 root = stack.pop()
                 root = root.right
        return res



if __name__ == '__main__':
   s = Solution()

   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.right = TreeNode(5)
   test.left.left = TreeNode(4)
   test.right.left = TreeNode(6)
   test.right.right = TreeNode(7)
   
   print s.preorderTraversal(test)


