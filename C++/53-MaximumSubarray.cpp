#include "include/common.h"


// Chris::NTR!
class Solution {
public:
    int maxSubArrayI(vector<int>& nums) {
        int last_sum = 0, max_sum = -9999;
        for (int i = 0; i < nums.size(); i++) {
             if (last_sum < 0) {
                 last_sum = 0;
             };
             last_sum += nums[i];
             max_sum = max(last_sum, max_sum);
        };
        return max_sum;
    }
    int maxSubArray(vector<int>& nums) {
        int last_sum = 0, max_sum = -9999;
        for (int i = 0; i < nums.size(); i++) {
             last_sum = max(last_sum + nums[i], nums[i]);
             max_sum = max(last_sum, max_sum);
        };
        return max_sum;
    }

};

int main(void) {
    Solution s;
    int arr [] = {-2,1,-3,4,-1,2,1,-5,4};
    vector<int> iarr(arr, arr + sizeof(arr) / sizeof(arr[0]));
    cout << s.maxSubArray(iarr) << endl;
    return 0;
};