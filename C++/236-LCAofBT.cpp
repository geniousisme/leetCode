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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
              if (root == nullptr) {  
                  return nullptr;
              };
              if (root == p || root == q) {
                  return root;
              };
              TreeNode *leftNode  = lowestCommonAncestor(root->left,  p, q);
              TreeNode *rightNode = lowestCommonAncestor(root->right, p, q);
              if (leftNode && rightNode) {
                  return root;
              };
              return leftNode != nullptr ? leftNode : rightNode;
    }   
};

int main(void) {
    Solution s;
    TreeNode root(1);
    TreeNode lnode(2);
    TreeNode rnode(3);
    TreeNode llnode(4);
    TreeNode rrnode(5);
    (&root)->left = &lnode;
    (&root)->right = &rnode;
    (&root)->left->left = &llnode;
    (&root)->right->right = &rrnode;
    cout << s.lowestCommonAncestor(&root, (&root)->left, (&root)->right->right)->val << endl;
    cout << s.lowestCommonAncestor(&root, (&root)->left, (&root)->right)->val << endl;
    cout << s.lowestCommonAncestor(&root, (&root)->left, (&root)->left->left)->val << endl;

    return 0;
};