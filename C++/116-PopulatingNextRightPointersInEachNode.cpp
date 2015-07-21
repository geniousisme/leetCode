#include <iostream>
#include <stack>

using namespace std;

struct TreeLinkNode {
       int val;
       TreeLinkNode *left, *right, *next;
       TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};
 
 // Chris:NTR!!
class Solution {
public:
    void connect(TreeLinkNode *root) {
         if (root) {
             if (root->left) {
                 root->left->next = root->right;
             };
             if (root->right && root->next) { 
                 root->right->next = root->next->left;
             };
             connect(root->left);
             connect(root->right);
         };
         return;
    }
    void connect(TreeLinkNode *root) {
         if (root && root->left) { 
             // since it is prefect binary tree, no left node = no right node.
             root->left->next = root->right;
             if (root->next) { // so it doesn't need to consider root->right == nullptr case
                 root->right->next = root->next->left;
             };
             connect(root->left);
             connect(root->right);
         };
         return;
    }
    void iterConnect(TreeLinkNode* root) {
         stack<TreeLinkNode*> stack;
         stack.push(root);
         while (!stack.empty()) {
                root = stack.top();
                stack.pop();
                if (root && root->left) {
                    root->left->next = root->right;
                    if (root->next) {
                        root->right->next = root->next->left;
                    };
                    stack.push(root->left);
                    stack.push(root->right);
                };
         };
         return;
    }
};