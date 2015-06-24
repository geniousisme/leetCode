# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def inorderTraversal(self, root, val_list, node_list):
        if root:
           self.inorderTraversal(root.left, val_list, node_list)
           val_list.append(root.val)
           node_list.append(root)
           self.inorderTraversal(root.right, val_list, node_list)
        return

    def recoverTree(self, root):
        val_list  = []
        node_list = []
        self.inorderTraversal(root, val_list, node_list)
        val_list.sort()
        for i in xrange(len(val_list)):
            node_list[i].val = val_list[i]

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(4)
   test.left = TreeNode(2)
   test.right = TreeNode(7)
   test.left.left = TreeNode(1)
   test.left.right = TreeNode(3)
   test.right.left = TreeNode(5)
   test.right.right = TreeNode(6)

   s.recoverTree(test)

   res = []
   s.inorderTraversal(test, res, [])
   print res



        