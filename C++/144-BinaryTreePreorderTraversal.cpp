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
    vector<int> preorderTraversal(TreeNode* root) {
                vector<int> res;
                recPreorderTraverse(root, res);
                return res;
    }
private:
    void recPreorderTraverse(TreeNode* root, vector<int>& res) {
         if (root){
             res.push_back(root->val);
             recPreorderTraverse(root->left,  res);
             recPreorderTraverse(root->right, res);
         };
         return;
    }
    void iterPreorderTraverse(TreeNode* root, vector<int>& res) {
         vector<TreeNode*> stack;
         while (root || !stack.empty()) {
                if (root){
                    res.push_back(root->val);
                    stack.push_back(root);
                    root = root->left;
                } else {
                    root = stack.back();
                    stack.pop_back();
                    root = root -> right;
                };
         };
         return;
    }
};
int main(void){
    return 0;
}