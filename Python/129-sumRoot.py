# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def __init__(self):
        self.res = []
    
    def sumNumbers(self, root):
        res = []
        self.dfs(root, "", res)
        # print res
        return sum(res)
        
    def dfs(self, root, num, res):
        if root:
           if root.right is None and root.left is None:
              res.append(int(num + str(root.val)))
              return
           # num += str(root.val)
           self.dfs(root.left,  num + str(root.val), res)
           self.dfs(root.right, num + str(root.val), res)
        return

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.left.right = TreeNode(5)
   test.right.left = TreeNode(6)
   test.right.right = TreeNode(7)
   print s.sumNumbers(test)
   print s.sumNumbers(None)



