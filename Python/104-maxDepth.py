# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    # def maxDepth(self, root):
    #     return self.traversal(root, 0)

    def traversal(self, node, depth):
        if node is None:
           return depth
        return max(self.traversal(node.left, depth + 1), self.traversal(node.right, depth + 1))

    def seniorMaxDepth(self, root):
        if root is None: 
           return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

    def maxDepth(self, root):
        self.max_depth = 0
        self.traverse(root, 0)
        return self.max_depth

    def traverse(self, root, depth):
        if root is None:
           self.max_depth = max(self.max_depth, depth)
           return
        else:
           self.traverse(root.right, depth + 1)
           self.traverse(root.left,  depth + 1)

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.left.left.left = TreeNode(4)
   test.left.right = TreeNode(5)
   print s.maxDepth(test)


 
            
