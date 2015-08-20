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
    vector<int> postorderTraversal(TreeNode* root) {
                vector<int> res;
                iterTraverse(root, res);
                return res;

    }
private:
    void recTraverse(TreeNode* root, vector<int>& res) {
         if (root) {
             recTraverse(root->left, res);
             recTraverse(root->right, res);
             res.push_back(root->val);       
         };
         return;
    }
    void iterTraverse(TreeNode* root, vector<int>& res) {
         vector<TreeNode*> stack;
         TreeNode *prev = nullptr, *curr = nullptr;
         if (root == nullptr) {
             return;
         };
         stack.push_back(root);
         while (!stack.empty()) {
                curr = stack[stack.size() - 1];
                if ((curr->right == nullptr && curr->left == nullptr) || (prev && (prev == curr->right || prev == curr->left))) {
                    res.push_back(curr->val);
                    prev = curr;
                    stack.pop_back();
                }
                else {
                    if (curr->right) {
                        stack.push_back(curr->right);
                    };
                    if (curr->left) {
                        stack.push_back(curr->left);
                    };
                };
         };
         return;
    }
};

int main(void) {
    Solution s;
    TreeNode root = TreeNode(1);
    // root.left = &TreeNode(2);
    // root.right = &TreeNode(3);
    s.postorderTraversal(&root);
    return 0;
}