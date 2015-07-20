#include <iostream>
#include <vector>
#include <queue>


using namespace std;

struct TreeNode {
       int val;
       TreeNode *left;
       TreeNode *right;
       TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
              if (root == nullptr) {
                  return nullptr;
              };
              TreeNode* tmp = root->left;
              root->left = invertTree(root->right);
              root->right = invertTree(tmp);
              return root;
    }
    TreeNode* myRecInvertTree(TreeNode* root) {
              if (root == nullptr) {
                  return nullptr;
              };
              TreeNode* tmp = root->left;
              root->left = root->right;
              root->right = tmp;
              invertTree(root->left);
              invertTree(root->right);
              return root;
    }
    TreeNode* myInvertTree(TreeNode* root) {
              TreeNode *new_root = root;
              vector<TreeNode*> stack;
              while (root || !stack.empty()) {
                     if (root) {
                         TreeNode *tmp_root = root->left;
                         root->left = root->right;
                         root->right = tmp_root;
                         stack.push_back(root->left);
                         stack.push_back(root->right);
                     };
                     if (!stack.empty()) {
                         root = stack.back();
                         stack.pop_back();
                     };
              };
              return new_root;
    }
    TreeNode* iterInvertTree(TreeNode* root) {
              TreeNode *new_root = root;
              if (root != nullptr) {
                  queue<TreeNode*> queue;
                  queue.push(root);
                  while (!queue.empty()) {
                         root = queue.front();
                         queue.pop();
                         TreeNode *tmp_root = root->left;
                         root->left = root->right;
                         root->right = tmp_root;
                         if (root->left) {
                             queue.push(root->left);
                         };
                         if (root->right) {
                             queue.push(root->right);
                         };                     
                  };
              };
              return new_root;
    }
};