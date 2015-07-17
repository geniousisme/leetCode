#include <iostream>
// using namespace std;

// Definition for a binary tree node.
struct TreeNode {
       int val;
       TreeNode *left;
       TreeNode *right;
       TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

typedef struct TreeNode treenode;

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
         if (p && q) return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
         else if (!p && !q) return true;
         else return false; // (!p && q) || (p && !q)         
    }
};

int main(int argc, char *argv []){
    treenode test1(1);
    treenode(2) = test1.left;
    treenode(3) = test1.right;
    return 0;

};