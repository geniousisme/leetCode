#include <iostream>
#include <queue>
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
    bool recIsSameTree(TreeNode* p, TreeNode* q) {
         if (p && q) return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
         else if (!p && !q) return true;
         else return false; // (!p && q) || (p && !q)         
    }
    bool isSameTree(TreeNode* p, TreeNode* q){
         std::queue<TreeNode*> pqueue;
         std::queue<TreeNode*> qqueue;

         pqueue.push(p);
         qqueue.push(q);
         
         while (!pqueue.empty() && !qqueue.empty()){
                TreeNode *tmp_p = pqueue.front();
                TreeNode *tmp_q = qqueue.front();

                pqueue.pop();
                qqueue.pop();

                // if (!tmp_q && !tmp_p) continue;
                if (tmp_q == nullptr && tmp_p == nullptr) continue;
                if (tmp_q == nullptr || tmp_p == nullptr) return false;
                if (tmp_q->val != tmp_p->val) return false;
                // if (!tmp_q || !tmp_p) return false;


                pqueue.push(tmp_p->left);
                pqueue.push(tmp_p->right);
                qqueue.push(tmp_q->left);
                qqueue.push(tmp_q->right);
         };

         return pqueue.empty() && qqueue.empty();
    }
};

int main(int argc, char *argv []){
    Solution s;
    treenode t1 = TreeNode(0);
    treenode t2 = TreeNode(1);
    std::cout << s.isSameTree(&t1, &t2) << std::endl;
};