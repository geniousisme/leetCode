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
    vector<vector<int> > levelOrder(TreeNode* root) {
                         vector<vector<int> > res;
                         if (root) {
                             levelOrderHelper(root, res, 1);
                         };
                         return res;
    }
private:
    void levelOrderHelper(TreeNode *root, vector<vector<int> >& res, int depth) {
         if (root == nullptr) {
             return;
         };
         if (res.size() < depth) {
             vector<int> level;
             res.push_back(level);
         };
         res[depth - 1].push_back(root->val);
         levelOrderHelper(root->left,  res, depth + 1);
         levelOrderHelper(root->right, res, depth + 1);
    }
};

int main(void) {
    Solution s;
    Utils u;
    TreeNode root(1);
    TreeNode lnode(2);
    TreeNode rnode(3);
    TreeNode llnode(4);
    TreeNode lrnode(5);
    TreeNode rlnode(6);
    TreeNode rrnode(7);
    (&root)->left = &lnode;
    (&root)->right = &rnode;
    (&root)->left->left = &llnode;
    (&root)->right->right = &rrnode;
    u.print2DIntVector(s.levelOrder(&root));
    return 0;
};