#include "../include/common.h"
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param root: The root of the binary search tree.
     * @param k1 and k2: range k1 to k2.
     * @return: Return all keys that k1<=key<=k2 in ascending order.
     */
    vector<int> searchRange(TreeNode* root, int k1, int k2) {
                vector<int> res;
                vector<TreeNode*> stack;
                while (root || !stack.empty()) {
                       if (root) {
                           stack.push_back(root);
                           root = root->left;
                       }
                       else {
                           root = stack.back();
                           stack.pop_back();
                           if (k1 <= root->val && root->val <= k2) {
                               res.push_back(root->val);    
                           };
                           root = root->right;
                       };
                };
                return res;
    }
};

int main(void) {
    Solution s;
    Utils u;
    TreeNode root(20);
    TreeNode lnode(8);
    TreeNode rnode(22);
    TreeNode llnode(4);
    TreeNode lrnode(12);
    (&root)->left = &lnode;
    (&root)->right = &rnode;
    (&root)->left->left = &llnode;
    (&root)->left->right = &lrnode;
    u.printIntVector(s.searchRange(&root, 10, 22));
    return 0;
};
