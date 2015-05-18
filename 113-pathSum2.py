# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def __init__(self):
        self.res = []
    
    def pathSum(self, root, sum):
        if root:
           # print 'root'
           self.dfs(root, [], sum)
        return self.res

    def dfs(self, node, path, left_sum):
        if node:
           if node.right is None and node.left is None:
              if left_sum == node.val:
                 path.append(node.val)
                 self.res.append(list(path))
                 path.pop()
                 return
           path.append(node.val)
           self.dfs(node.right, path, left_sum - node.val)
           self.dfs(node.left,  path, left_sum - node.val)
           path.pop()
        return
if __name__ == '__main__':
   s = Solution()
   test = TreeNode(5)
   test.left = TreeNode(4)
   test.right = TreeNode(8)
   test.left.left = TreeNode(11)
   test.left.left.left = TreeNode(7)
   test.left.left.right = TreeNode(2)
   test.right.left = TreeNode(13)
   test.right.right = TreeNode(4)
   test.right.right.left = TreeNode(5)
   test.right.right.right = TreeNode(1)
   print s.pathSum(test, 22)
        
