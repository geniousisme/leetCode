#include <vector>
#include <iostream>
#include <string>
using namespace std;

struct TreeLinkNode {
       int val;
       TreeLinkNode *left, *right, *next;
       TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};
 
class Solution {
public:
    void connect(TreeLinkNode *root) {
         vector<TreeLinkNode*> nodesArr;
         dfs(root, nodesArr, 1);
         return;
    }

    void dfs(TreeLinkNode *root, vector<TreeLinkNode*>& nodesArr, int level) {
         if (root) {
             if (nodesArr.size() < level) {
                struct TreeLinkNode dummy(-1);
                nodesArr.push_back(&dummy);          
             };
             nodesArr[level - 1]->next = root;
             nodesArr[level - 1] = nodesArr[level - 1]->next;
             dfs(root->left, nodesArr, level + 1);
             dfs(root->right, nodesArr, level + 1);
         };
         return;
    }
    //Chris:TODO::NTR, need to use drawing to simulate the traversal.
    void iterConnect(TreeLinkNode *root) {
         if (!root) {
             return;
         };
         TreeLinkNode *curr = root, *nxt_lv = nullptr, *last = nullptr;
         while (curr) {
                if (!nxt_lv) {
                    if (curr->left) {
                        nxt_lv = curr->left;
                    } else if (curr->right) {
                        nxt_lv = curr->right;
                    };
                };
                if (curr->left) {
                    if (last) {
                        last->next = curr->left;
                    };
                    last = curr->left;
                };
                if (curr->right) {
                    if (last) {
                        last->next = curr->right;
                    };
                    last = curr->right;
                };  
                if (curr->next) {
                    curr = curr->next;
                } else {
                    curr   = nxt_lv;
                    nxt_lv = nullptr;
                    last   = nullptr;
                };

         };
         return;
    }
};

int main(void) {
    Solution s;
    struct TreeLinkNode test(0);
    s.connect(&test);
    return 0;
};