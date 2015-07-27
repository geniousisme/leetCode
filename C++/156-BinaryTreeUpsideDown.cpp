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
                     // store the value first
                     rootLeft    = root->left;
                     rootRight   = root->right;
                     
                     // assign new value to root
                     root->left  = parentLeft;
                     root->right = parent;
                     
                     //store the value for the next root
                     parent      = root;
                     parentLeft  = rootRight;
                     
                     // move the next root
                     root = rootLeft;
              };
              return parent;
    }
};