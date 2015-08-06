#include "include/common.h"
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// try to use 
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
              vector<int> nums;
              while (head) {
                     nums.push_back(head->val);
                     head = head->next;
              };
              return buildTree(nums, 0, nums.size() - 1);
    }
private:
    TreeNode* buildTree(vector<int>& nums, int start, int end) {
              if (end < start) {
                  return nullptr;
              };
              int mid        = (start + end) / 2;
              TreeNode *root = new TreeNode(nums[mid]);
              root->left     = buildTree(nums, start, mid - 1);
              root->right    = buildTree(nums, mid + 1, end);
              return root;
    }
};