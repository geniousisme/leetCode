# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def __init__(self):
        self.res = []
    
    def zigzagLevelOrder(self, root):
        self.zigzag_traverse(0, root)
        return self.res
        
    def zigzag_traverse(self, depth, node):
        if node:
           if len(self.res) < depth + 1: 
               self.res.append([])
           # print 'node:', node.val
           # print 'depth:', depth
           if depth % 2 == 0:
              self.res[depth].append(node.val)
           else: 
              self.res[depth].insert(0, node.val)
           self.zigzag_traverse(depth + 1, node.left)
           self.zigzag_traverse(depth + 1, node.right)
        return

if __name__ == '__main__':
   test             = TreeNode(1)
   test.left        = TreeNode(2)
   test.right       = TreeNode(3)
   test.left.left   = TreeNode(4)
   test.left.right   = TreeNode(-1)
   test.right.left  = TreeNode(-1)
   test.right.right = TreeNode(5)
   print Solution().zigzagLevelOrder(test)

