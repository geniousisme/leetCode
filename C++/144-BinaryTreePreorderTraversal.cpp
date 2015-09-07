#include <vector>

using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> preorderTraversalI(TreeNode* root) {
                vector<int> res;
                recPreorderTraverse(root, res);
                return res;
    }
    vector<int> preorderTraversalII(TreeNode* root) {
                vector<int> res;
                if (root) {
                    vector<TreeNode*> stack;
                    stack.push_back(root);
                    while (!stack.empty()) {
                           root = stack[stack.size() - 1];
                           res.push_back(root->val);
                           stack.pop_back();
                           if (root->right) {
                               stack.push_back(root->right);
                           };
                           if (root->left) {
                               stack.push_back(root->left);
                           };
                    };
                };
                return res;
    };
    vector<int> preorderTraversal(TreeNode* root) {
                vector<int> res;
                vector<TreeNode*> stack;
                while (root || !stack.empty()) {
                       if (root) { 
                           res.push_back(root->val);
                           stack.push_back(root);
                           root = root->left;
                       }
                       else {
                           root = stack.back();
                           stack.pop_back();
                           root = root->right;
                       };
                };
                return res;
    };
private:
    void recPreorderTraverse(TreeNode* root, vector<int>& res) {
         if (root){
             res.push_back(root->val);
             recPreorderTraverse(root->left,  res);
             recPreorderTraverse(root->right, res);
         };
         return;
    }

};
int main(void){
    return 0;
}