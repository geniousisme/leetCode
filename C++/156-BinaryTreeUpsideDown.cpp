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
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
              struct TreeNode *parent = nullptr;
              struct TreeNode *parentLeft = nullptr;
              struct TreeNode *rootLeft, *rootRight;
              while (root) {
                     rootLeft  = root->left;
                     rootRight = root->right;
                     root->left = parentLeft;
                     root->right = parent;
                     parent = root;
                     parentLeft = rootRight;
                     root = rootLeft;
              };
              return parent;
    }
};