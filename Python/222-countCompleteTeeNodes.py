# Definition for a binary tree node.
# Chris:Still dont know whats wrong for cant be accepted.
# maybe checkout later.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def __init__(self):
        self.count = 0
    
    def countNodes(self, root):
        if root:
           left_depth  = self.countDepth(root, 'left')
           right_depth = self.countDepth(root, 'right')
           if left_depth == right_depth:
              return 2 ** left_depth - 1
           else:
              self.countRecursive(root)
        return self.count

    def countDepth(self, root, direction):
        if root is None:
           return 0
        if direction == 'left':
           next = root.left
        else: # 'right'
           next = root.right
        return 1 + self.countDepth(next, direction)
    
    def countRecursive(self, root):
        if root is None:
           return
        self.count += 1
        self.countRecursive(root.right)
        self.countRecursive(root.left)

    def countRecursive2(self, root):
        if root is None:
           return 0
        return self.countRecursive2(root.right) + self.countRecursive2(root.left) + 1


if __name__ == '__main__':
   s = Solution()
   
   test = TreeNode(4)
   test.right = TreeNode(7)
   test.left  = TreeNode(2)
   test.right.right = TreeNode(9)
   test.right.left = TreeNode(6)
   test.left.right = TreeNode(3)
   test.left.left = TreeNode(1)

   # print s.countDepth(test, 'right')
   # print s.countDepth(test, 'left')
   # print s.countNodes(test)
   print s.countRecursive2(test)

