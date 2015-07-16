# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def __init__(self):
        self.max = -float('inf')
    
    def maxPathSum(self, root):
        if root is None: 
           return 0
        self.dfs(root)
        return self.max
    
    def dfs(self, root):
        if root is None:
           return 0
        sum = root.val
        left_max = right_max = 0
        if root.left:
           left_max =  self.dfs(root.left)
           if left_max > 0:
              sum   += left_max
        if root.right:
           right_max =  self.dfs(root.right)
           if right_max > 0:            
              sum    += right_max
        if sum > self.max: self.max = sum
        return max(root.val, max(root.val + right_max, root.val + left_max))

# Chris:TODO::study this and write your own version
# class Solution:
#     # @param root, a tree node
#     # @return an integer
#     deep = 0
 
#     def maxPathSum(self, root):
#         if root == None:
#             return 0
#         if Solution.deep == 0: ＃ Solution.maxSum is set to infinitesimal every time when a new test case starts
#             Solution.maxSum = -10 ** 10
#         Solution.deep += 1
#         vLeft = self.maxPathSum(root.left)
#         vRight = self.maxPathSum(root.right)
#         Solution.deep -= 1
#         Solution.maxSum = max(root.val + vLeft + vRight, Solution.maxSum)
#         if Solution.deep == 0:
#             return Solution.maxSum
#         return max(root.val + vLeft, root.val + vRight, 0)


if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.right = TreeNode(2)
   test.right.right = TreeNode(4)
   test.right.left  = TreeNode(5)
   test.left  = TreeNode(3)
   test.left.right  = TreeNode(6)
   test.left.left  = TreeNode(7)

   print s.maxPathSum(test)
   test2 = TreeNode(0)
   print s.maxPathSum(test2)

   test3 = TreeNode(2)
   test3.right = TreeNode(-1)
   print s.maxPathSum(test3)


        