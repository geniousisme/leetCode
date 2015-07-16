# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def recurKthSmallest(self, root, k):
        res = []
        self.inorderTraversal(root.left, res)
        return res[k - 1]
        
    def inorderTraversal(self, root, res):
        if root:
           self.inorderTraversal(root.left, res)
           res.append(root.val)
           self.inorderTraversal(root.right, res)
        return

    def kthSmallest(self, root, k):
        stack = []
        node  = root
        while node:
              stack.append(node)
              node = node.left
        count = 1
        while stack and count <= k:
              node = stack.pop()
              count += 1
              right = node.right
              while right:
                    stack.append(right)
                    right = right.left
        return node.val

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(4)
   test.left = TreeNode(2)
   test.right = TreeNode(6)
   test.left.left = TreeNode(1)
   test.left.right = TreeNode(3)
   test.right.left = TreeNode(5)
   test.right.right = TreeNode(7)
   # print s.countTreeNum(test)
   s.kthSmallest(test, 1)

