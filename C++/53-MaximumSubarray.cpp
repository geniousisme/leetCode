#include "include/common.h"


// Chris::NTR!
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> res;
        int pre_sum = 0, max_sum = -9999;
        // res.push_back(nums[0]);
        for (int i = 0; i < nums.size(); i++){
            // pre_sum = 
            // int tmp [] = {res[i - 1], nums[i], pre_sum};
            if (pre_sum < 0) {
                pre_sum = 0;
            };
            // res.push_back(max(, ));
            pre_sum += nums[i];
            max_sum = max(pre_sum, max_sum);
            // cout << "max_sum " << max_sum << endl;
            // pre_sum += nums[i];
        };
        // for (int i = 0; i < res.size(); i++) cout << res[i] << " ";
        // cout << endl;
        // return res[nums.size() - 1];
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