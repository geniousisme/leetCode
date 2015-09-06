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
    vector<int> inorderTraversalI(TreeNode* root) {
                vector<int> res;
                iterInorderHelper(root, res);
                return res;
    }
    vector<int> inorderTraversal(TreeNode* root) {
                vector<int> res;
                vector<TreeNode*> stack;
                while (root || !stack.empty()) {
                       if (root) {
                           stack.push_back(root);
                           root = root->left;
                       }
                       else {
                           root = stack.back();
                           res.push_back(root->val);
                           stack.pop_back();
                           root = root->right;
                       };
                };
                return res;
    }
private:
    void recInorderHelper(TreeNode* root, vector<int>& res){
         if (root != nullptr){
            recInorderHelper(root->left, res);
            res.push_back(root->val);
            recInorderHelper(root->right, res);
         };
         return;
    }
    // Chris:TODO::NTR!
};
int main(void){
    return 0;
}