#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct TreeNode {
       int val;
       TreeNode *left;
       TreeNode *right;
       TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> recRightSideView(TreeNode* root) {
                vector<int> right_nodes;
                dfs(root, right_nodes, 0);
                return right_nodes;
    }
    void dfs(TreeNode *root, vector<int>& right_nodes, int level) {
         if (root) {
             if (right_nodes.size() < level + 1) {
                 right_nodes.push_back(0);
             };
             right_nodes[level] = root->val;
             dfs(root->left,  right_nodes, level + 1);
             dfs(root->right, right_nodes, level + 1);
         };
         return;
    }
    // Chris::TODO:NTR
    vector<int> rightSideView(TreeNode* root) {
                vector<int> right_nodes;
                if (root) {
                    vector<TreeNode*> queue;
                    queue.push_back(root);
                    while (!queue.empty()) {
                           int size = queue.size();
                           for (int i = 0; i < size; i++) {
                                if (i == 0) {
                                    right_nodes.push_back(queue[i]->val);
                                };
                                TreeNode *root = *queue.begin();
                                queue.erase(queue.begin());
                                if (root->right) {
                                    queue.push_back(root->right);
                                }; 
                                if (root->left) {
                                    queue.push_back(root->left);
                                };
                           };
                           // queue.erase(queue.begin(), queue.begin() + size);
                    };
                };
                return right_nodes;
    }
};

int main(void) {
    Solution s;
    struct TreeNode test(1);
    s.rightSideView(&test);
    return 0;

};