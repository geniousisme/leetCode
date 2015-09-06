#include "include/common.h"
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        sum = 0, maxSum = 0;
        if (root) {
            maxSum = -numeric_limits<double>::infinity();
            maxPathHelper(root);
        };
        return maxSum;
    }
private:
    int sum;
    double maxSum;
    int maxPathHelper(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        };
        int leftSum  = maxPathHelper(root->left);
        int rightSum = maxPathHelper(root->right);
        sum = root->val;
        if (leftSum > 0) {
            sum += leftSum;
        };
        if (rightSum > 0) {
            sum += rightSum;
        };
        if (sum > maxSum) {
            maxSum = sum;
        };
        int currMaxSum = root->val + (leftSum > rightSum ? leftSum : rightSum);
        return root->val > currMaxSum ? root->val : currMaxSum;
    }
};

int main (void) {
    Solution s;
    TreeNode root(-1);
    TreeNode leftNode(-2);
    TreeNode rightNode(3);
    (&root)->left = (&leftNode);
    (&root)->right = (&rightNode);
    cout << s.maxPathSum(&root) << endl;
    return 0;
};