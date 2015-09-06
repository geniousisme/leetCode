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
    bool isValidBST(TreeNode* root) {
         double inf = numeric_limits<double>::infinity();
         return validTraverse(root, -inf, inf);
    }
private:
    // Chris:NTR!! must remember!!!
    int startVal;
    bool validTraverse(TreeNode* root, double pastMin, double pastMax) {
         if (root == nullptr) {
             return true;
         };
         if (!(root->val > pastMin && root->val < pastMax)) {
             return false;
         };
         return validTraverse(root->left, pastMin, root->val) && validTraverse(root->right, root->val, pastMax);
    }
};

int main(void) {
    Solution s;
    TreeNode root(0);
    cout << s.isValidBST(&root) << endl;
    return 0;
};