#include "include/common.h"

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int start = 0, end = nums.size() - 1, mid;
        if (nums.size() < 2) {
            return 0;
        };
        while (start < end) {
               // if (start == end) {
               //     return start;
               // }
               if (end == start + 1) {
                   return nums[end] > nums[start] ? end : start;
               };
               mid = (start + end) / 2;
               if (nums[mid] > nums[mid + 1]) {
                   end = mid;
               }
               else if (nums[mid] < nums[mid + 1]) {
                        start = mid;
               }
               else {
                   start = mid;
               };
        };
        return -1;
    }
};

int main(void) {
    Solution s;
    Utils u;
    // int iarr [] = {1, 2, 3, 1};
    int iarr [] = {1, 2, 3};
    // int iarr [] = {1, 2, 1, 3, 4, 5, 7, 6};
    vector<int> nums(iarr, iarr + sizeof(iarr) / sizeof(iarr[0]));
    cout << s.findPeakElement(nums) << endl;
    return 0;
}