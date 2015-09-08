#include "include/common.h"
class Solution {
public:
    bool canJumpWithDP(vector<int>& nums) { // TLE
         vector<bool> jumpAble(nums.size(), false);
         jumpAble[0] = true;
         for (int i = 1; i < nums.size(); i++) {
              for (int j = 0; j < i; j++) {
                   if (jumpAble[j] && j + nums[j] >= i) {
                       jumpAble[i] = true;
                       break; 
                   };
              };
         };
         return jumpAble[nums.size() - 1];
    }
    bool canJump(vector<int>& nums) { // Greedy
         int farthest = nums[0], i = 1;
         while (i < nums.size() - 1 && i <= farthest) {
                if (farthest <= i + nums[i]) {
                    farthest = i + nums[i];
                };
                i++;
         };
         return farthest >= nums.size() - 1;
    }
};

int main(void) {
    Solution s;
    int jumps1 [] = {2, 3, 1, 1, 4};
    vector<int> nums1(jumps1, jumps1 + sizeof(jumps1) / sizeof(jumps1[0]));
    cout << s.canJump(nums1) << endl;
    int jumps2 [] = {3, 2, 1, 0, 4};
    vector<int> nums2(jumps2, jumps2 + sizeof(jumps2) / sizeof(jumps2[0]));
    cout << s.canJump(nums2) << endl;
    int jumps3 [] = {2, 10, 0, 0, 1};
    vector<int> nums3(jumps3, jumps3 + sizeof(jumps3) / sizeof(jumps3[0]));
    cout << s.canJump(nums3) << endl;
    return 0;
};