#include "include/common.h"

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int currMax = nums[0], currMin = nums[0], Max = nums[0];
        for (int i = 1; i < nums.size(); i++) {
             int min_tmp = currMin * nums[i];
             int max_tmp = currMax * nums[i];
             int arr []  = {max_tmp, min_tmp, nums[i]};
             currMin = *min_element(arr, arr + 3);
             currMax = *max_element(arr, arr + 3);
             Max     = max(Max, currMax);
        };    
        return Max;
    }
};

int main(void) {
    Solution s;
    int arr [] = {-2,-3,-2,4,2};
    vector<int> iarr(arr, arr + sizeof(arr) / sizeof(arr[0]));
    cout << s.maxProduct(iarr) << endl;
    return 0;
};