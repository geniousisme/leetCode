# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        res = []
        self.iterPostOrder(root, res)
        return res

    def recurPostOrder(self, root, res):
        if root:
           self.recurPostOrder(root.left, res)
           self.recurPostOrder(root.right, res)
           res.append(root.val)
        return

    def iterPostOrder(self, root, res):
        stack = []
        prev = None
        if root:
           stack.append(root)
           while stack:
                 curr = stack[-1]
                 if (curr.left is None and curr.right is None) or (prev and (prev == curr.left or prev == curr.right)):
                    res.append(curr.val)
                    prev = stack.pop()
                 else:
                    if curr.right: stack.append(curr.right)
                    if curr.left:  stack.append(curr.left)
        return res


if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.left.right = TreeNode(5)
   test.right.left = TreeNode(6)
   test.right.right = TreeNode(7)
   print s.postorderTraversal(test)
