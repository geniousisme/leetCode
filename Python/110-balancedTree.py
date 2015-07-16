# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Chris:TODO:: find some faster algorithm

class Solution:
    # @param {TreeNode} root
    # @return {boolean}    
    # def isBalanced(self, root):
    #     if root is None: 
    #        return False
    #     return self.balanceCheck(root)

    # def balanceCheck(self, node):
    #     if node.right is None and node.left is None:
    #        return True
    #     elif node.right and node.left:
    #          return self.balanceCheck(node.right) and self.balanceCheck(node.left)
    #     else:
    #         if node.left and node.right is None:
    #            return not (node.left.left or node.left.right)
    #         if node.right and node.left is None:
    #            return not (node.right.left or node.right.right)
    def height(self, root):
        if root is None: 
           return 0
        else:
           return max(self.height(root.right), self.height(root.left)) + 1

    def isBalanced(self, root):
        if root is None: return True
        if abs(self.height(root.right) - self.height(root.left)) > 1:
           return False
        else:
           return self.isBalanced(root.right) and self.isBalanced(root.left)



if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   # test.left = TreeNode(0)
   # test.left.left = TreeNode(0)
   test.right = TreeNode(2)
   test.right.right = TreeNode(3)
   print s.isBalanced(test)             
        

