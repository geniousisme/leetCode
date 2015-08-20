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
    vector<int> postorderTraversalI(TreeNode* root) {
                vector<int> res;
                traverse(root, res);
                return res;

    }
    void traverse(TreeNode* root, vector<int>& res) {
         if (root) {
             traverse(root->left, res);
             traverse(root->right, res);
             res.push_back(root->val);       
         };
         return;
    }
    vector<int> postorderTraversal(TreeNode* root) {
                vector<int> res;
                iterTraverse(root, res);
                return res;
    }
    void iterTraverse(TreeNode* root, vector<int>& res) {
         vector<TreeNode*> stack;
         TreeNode* prev = nullptr, curr = nullptr;
         if (root) {
             stack.push_back(root);
             while(!stack.empty()) {
                   curr = stack[stack.size() - 1];
                   if ((curr->right == nullptr && curr->left == nullptr) || (prev && (prev == curr->right || prev == curr->right))) {
                        
                        stack.pop();
                   }
                   else {

                   };

             };
         };
    }

    

};