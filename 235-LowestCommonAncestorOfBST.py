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
        return self.iterLCA(root, p, q)

    def iterLCA(self, root, p, q):
        while root:
              if (root.val - p.val) * (root.val - q.val) <= 0:
                 return root
              elif root.val > p.val:
                 root = root.left
              else:
                 root = root.right

    def recLCA(self, root, p, q):
        if (root.val - p.val) * (root.val - q.val) <= 0:
           return root
        elif root.val > p.val:
           return self.recLCA(root.left,  p, q)
        else:
           return self.recLCA(root.right, p, q)

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(6)
   test.left = TreeNode(2)
   test.right = TreeNode(8)
   test.left.left = TreeNode(0)
   test.left.right = TreeNode(4)
   test.right.left = TreeNode(7)
   test.right.right = TreeNode(9)
   root = s.lowestCommonAncestor(test, test.left, test.right)
   print root.val