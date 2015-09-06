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
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
    //  */
    TreeNode* insertNodeI(TreeNode* root, TreeNode* node) {
        // write your code here
        if (root == nullptr) {
            return node;
        }
        else {
            traverse(root, node);
        };
        return root;
    }
    TreeNode* insertNode(TreeNode* root, TreeNode* node) {
        // write your code here
        if (root == nullptr) {
            return node;
        };
        TreeNode *start = root;
        while (root) {
               if (root->val > node->val) {
                   if (root->left == nullptr) {
                       root->left = node;
                       break;
                   };
                   root = root->left;
               } 
               else if (root->val < node->val) {
                        if (root->right == nullptr) {
                            root->right = node;
                            break;
                        };
                        root = root->right;
               }
               else { // root->val == node->val
                   root = node;
                   break;
               };
        };
        return start;
    }
private:
    void traverse(TreeNode* root, TreeNode* node) {
         if (root->val > node->val) {
             if (root->left) {
                 traverse(root->left, node);
             }
             else {
                root->left = node;
                return;
             };
         }
         else if (root->val < node->val) {
                  if (root->right) {
                      traverse(root->right, node);
                  }
                  else {
                      root->right = node;
                      return;
                  };
         }
         else { // root->val == node->val
             root = node;
             return;
         };
    };
};
