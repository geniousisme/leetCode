# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def __init_(self):
        self.res = []
    
    def buildBinaryTree(self, start, end):
        res = []
        if start > end:
           res.append(None)
           return res
        for node_val in xrange(start, end + 1):
            left_node_list  = self.buildBinaryTree(start, node_val - 1)
            right_node_list = self.buildBinaryTree(node_val + 1, end)
            for l in left_node_list:
                for r in right_node_list:
                    node = TreeNode(node_val)
                    node.left  = l
                    node.right = r
                    res.append(node)
        return res

    def generateTrees(self, n):
        return self.buildBinaryTree(1, n)
                

if __name__ == '__main__':
   s = Solution()
   print s.generateTrees(3)