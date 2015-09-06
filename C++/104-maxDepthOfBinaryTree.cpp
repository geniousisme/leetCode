#include <iostream>
#include <string>

//  * Definition for a binary tree node.
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

typedef struct TreeNode tnoode;

class Solution {
public:
    int juniorMaxDepth(TreeNode* root) {
        int max_depth = 0;
        traverse(root, 0, max_depth);
        return max_depth;
    }
    int maxDepth(TreeNode *root) {
        if (root == nullptr) {
            return 0;
        };
        int leftDepth  = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        return (leftDepth > rightDepth ? leftDepth : rightDepth) + 1;
    } 
private:
    void traverse(TreeNode* root, int depth, int& max_depth){
         if (root == nullptr){
            max_depth = depth > max_depth ? depth : max_depth;
            return;
         } else {
            traverse(root->left, depth + 1, max_depth);
            traverse(root->right, depth + 1, max_depth);
         };
    }
};

int main(int argc, char *argv []){
    Solution s;
    tnoode root = TreeNode(1);
    tnoode left = TreeNode(2);
    tnoode right = TreeNode(3);
    root.left = &left;
    root.right = &right;
    // root.left->left = &left;
    // root.left->left->left = &left;
    std::cout << "max depth: " << s.maxDepth(&root) << std::endl;
    return 0;
};