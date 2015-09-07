/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
                if (root) {
                    inorderTraversal(root);
                    calledIdx = -1;
                };
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
         return calledIdx < res.size();
    }

    /** @return the next smallest number */
    int next() {
        calledIdx++;
        return res[calledIdx];
    }
private:
    vector<int> res;
    int calledIdx;
    void inorderTraversal(TreeNode *root) {
         if (root) {
             inorderTraversal(root->left);
             res.push_back(root->val);
             inorderTraversal(root->right);
         };
         return;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */