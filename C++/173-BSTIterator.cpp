#include "include/common.h"
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// class BSTIterator {
// public:
//     BSTIterator(TreeNode *root) {
//                 cout << "called" << endl;
//                 if (root) {
//                     inorderTraversal(root);
//                     calledIdx = -1;
//                 };
//     }

//     /** @return whether we have a next smallest number */
//     bool hasNext() {
//          // cout << "calledIdx: " << calledIdx << endl;
//          // cout << "resSize: " << res.size() << endl;
//          return calledIdx < res.size() - 1;
//     }

//     /** @return the next smallest number */
//     int next() {
//         calledIdx++;
//         // cout << "elem: " << res[calledIdx] << endl;
//         return res[calledIdx];
//     }
// private:
//     vector<int> res;
//     int calledIdx;
//     void inorderTraversal(TreeNode *root) {
//          if (root) {
//              inorderTraversal(root->left);
//              res.push_back(root->val);
//              inorderTraversal(root->right);
//          }
//          return;
//     }
// };
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
                while (!stk.empty()) {
                       stk.pop();  
                };
                pushLeft(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
         return !stk.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *root = stk.top();
        stk.pop();
        int res = root->val;
        pushLeft(root->right);
        return res;
    }
private:
    stack<TreeNode*> stk;
    void pushLeft (TreeNode *root) {
         while (root) {
                stk.push(root);
                root = root->left;
         };
    }
};
// lintcode version of BST Iterator
/* Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 * Example of iterate a tree:
 * Solution iterator = Solution(root);
 * while (iterator.hasNext()) {
 *    TreeNode * node = iterator.next();
 *    do something for node
 */
class Solution {
public:
    //@param root: The root of binary tree.
    Solution(TreeNode *root) {
             while (!stk.empty()) {
                    stk.pop();
             };
             pushLeft(root);
    }

    //@return: True if there has next node, or false
    bool hasNext() {
         // write your code here
         return !stk.empty();
    }
    
    //@return: return next node
    TreeNode* next() {
              // write your code here
              TreeNode *root = stk.top();
              stk.pop();
              pushLeft(root->right);
              return root;
    }
private:
    stack<TreeNode*> stk;
    void pushLeft(TreeNode* root) {
         while (root) {
                stk.push(root);
                root = root->left;
         };
    }
};


/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
 int main(void) {
    // Solution s;
    // Utils u;
    TreeNode root(20);
    TreeNode lnode(8);
    TreeNode rnode(22);
    TreeNode llnode(4);
    TreeNode lrnode(12);
    (&root)->left = &lnode;
    (&root)->right = &rnode;
    (&root)->left->left = &llnode;
    (&root)->left->right = &lrnode;
    BSTIterator i = BSTIterator(&root);
    // cout << "next: " << i.next() << endl;
    while (i.hasNext()) {
           cout << i.next() << " ";
    };
    cout << endl;
    return 0;
};
