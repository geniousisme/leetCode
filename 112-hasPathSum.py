# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root is None:
           return False
        return self.pathSumCheck(root, 0, sum)
        
    def pathSumCheck(self, node, curr_sum, goal_sum):
        if node is None:
           return False
        curr_sum += node.val
        if node.right is None and node.left is None:
           return curr_sum == goal_sum
        else:
           return self.pathSumCheck(node.right, curr_sum, goal_sum) or \
                  self.pathSumCheck(node.left,  curr_sum, goal_sum) 
                  

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.right = TreeNode(2)
   print s.hasPathSum(test, 2)
   print s.hasPathSum(test, 1)

