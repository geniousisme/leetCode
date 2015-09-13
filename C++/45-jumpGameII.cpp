#include "include/common.h"
class Solution {
public:
    int jumpWithDP(vector<int>& nums) {
        int max = numeric_limits<int>::max();
        vector<int> minSteps(1, 0);
        for (int i = 1; i < nums.size(); i ++) {
             minSteps.push_back(max);
             for (int j = 0; j < i; j++) {
                  if (nums[j] != max && nums[j] + j >= i) {
                      minSteps[i] = minSteps[j] + 1;
                      break;
                  };
             };
        };
        return minSteps[nums.size() - 1];
    }
    int jump(vector<int>& nums) {
        int farthest = nums[0], start = 1, end = farthest, jumps = 0;
        while (start < nums.size()) {
               jumps++;
               for (int i = start; i <= end; i++) {
                    if (i + nums[i] > farthest) {
                        farthest = i + nums[i];
                    };
               };
               start = end + 1;
               end = farthest;
        };
        return jumps;  
    }  
};

int main(void) {
    Solution s;
    int iarr [] = {2, 3, 1, 1, 4};
    vector<int> nums(iarr, iarr + sizeof(iarr) / sizeof(iarr[0]));
    cout << s.jump(nums) << endl;
    int iarr2 [] = {2, 10, 1, 1, 1, 5};
    vector<int> nums2(iarr2, iarr2 + sizeof(iarr2) / sizeof(iarr2[0]));
    cout << s.jump(nums2) << endl;
    return 0;
};