#include "include/common.h"

// Chris:NTR!

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0, candidate = -9999;
        for (int i = 0; i < nums.size(); i++){
             if (count == 0) {
                 candidate = nums[i];
                 count++;
             }
             else if (candidate == nums[i]) {
                      count++;
             } 
             else {
                count--;
             };
        };
        return candidate;
    }
};

int main(void) {
    Solution s;
    int arr [] = {1, 2, 1, 1, 0, 1};
    vector<int> test(arr, arr + 6);
    cout << s.majorityElement(test) << endl;
    return 0;
};