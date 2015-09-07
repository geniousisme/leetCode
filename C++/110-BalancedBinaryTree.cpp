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
    bool isBalanced(TreeNode* root) {
         // 不能用一般的方法做，因為你這樣沒辦法確定每一層的 node 是否都有深度相等
         // 不能只看下一層是否有兩層，有可能是下一層的下一層還有，那這層其實就不能算了
         // if (root == nullptr) {
         //     return true;
         // };
         // if (root->left == nullptr) {
         //     if (root->right && (root->right->left || root->right->right)) {
         //         return false;
         //     };
         // };
         // if (root->right == nullptr) {
         //     if (root->left && (root->left->left || root->left->right)) {
         //         return false;
         //     };
         // };
         // return isBalanced(root->right) && isBalanced(root->left);
         if (root == nullptr) {
             return true;
         };
         int diff = maxDepth(root->left) - maxDepth(root->right);
         if (diff > 1 || diff < -1) {
             return false;
         };
         return isBalanced(root->left) && isBalanced(root->right);
    }
private:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        };
        int leftDep  = maxDepth(root->left);
        int rightDep = maxDepth(root->right);
        return (leftDep > rightDep ? leftDep : rightDep) + 1;
    }
};

int main (void) {
    Solution s;
    TreeNode root(1);
    TreeNode lnode(2);
    TreeNode rnode(3);
    TreeNode llnode(3);
    (&root)->left = (&lnode);
    // (&root)->right = (&rnode);
    (&root)->left->left = (&llnode);
    cout << s.isBalanced(&root) << endl;
    // cout << s.isBalanced((&root)->left) << endl;
    return 0;
};