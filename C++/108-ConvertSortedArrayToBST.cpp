#include "include/common.h"
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
              return buildTree(nums, 0, nums.size() - 1);
    }

private:
    TreeNode* buildTree(vector<int>& nums, int start, int end) {
              if (start > end) {
                  return nullptr;
              };
              int mid        = start + (end - start) / 2;
              // cout << "node1" << endl;
              // TreeNode newNode = TreeNode(nums[mid]);
              // TreeNode *node   = &newNode;
              // cout << "node: " << node << endl;
              TreeNode *node = new TreeNode(nums[mid]); // in this way, c++ wil generate a new ptr
              // node->val      = nums[mid];
              // cout << "node->val: " << node->val << endl;

              node->left     = buildTree(nums, start, mid - 1);
              node->right    = buildTree(nums, mid + 1, end);
              return node;
    }
};

int main(void) {
    Solution s;
    int iarr [] = {0, 1, 2};
    vector<int> nums(iarr, iarr + sizeof(iarr)/sizeof(iarr[0]));
    s.sortedArrayToBST(nums);
    return 0;
};