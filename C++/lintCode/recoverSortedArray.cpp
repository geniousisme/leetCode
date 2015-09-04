#include "include/common.h"

//Chris:NTR
class Solution {
public:
    void recoverRotatedSortedArray(vector<int> &nums) {
        // write your code here
        if (nums.size() < 2) {
            return;
        };
        int rotated_idx = -1;
        for (int i = 0; i < nums.size() - 1; i++) {
             if (nums[i] > nums[i + 1]) {
                 rotated_idx = i;
                 break;
             };
        };
        // cout << "rotated_idx " << rotated_idx << endl;
        if (rotated_idx > -1) {
            // int start = 0, end = rotated_idx;
            reverse(nums.begin(), nums.begin() + rotated_idx + 1);
            reverse(nums.begin() + rotated_idx + 1, nums.end());
            reverse(nums.begin(), nums.end());
        };
    }
};

int main(void) {
    Solution s;
    Utils u;
    int iarr [] = {4, 5, 1, 2 ,3};
    vector<int> nums(iarr, iarr + sizeof(iarr) / sizeof(iarr[0]));
    s.recoverRotatedSortedArray(nums);
    u.printIntVector(nums);
    return 0;
};
