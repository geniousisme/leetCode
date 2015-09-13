#include "../include/common.h"

class Solution {
public:
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    int longestIncreasingSubsequenceI(vector<int> nums) {
        // write your code here
        vector<int> dp(nums.size(), 1);
        int maxLeng = 0;
        for (int i = 1; i < nums.size(); i++) {
             for (int j = 0; j < i; j++) {
                 if (nums[i] >= nums[j]) { // front > back elem in the array.
                     dp[i] = max(dp[j] + 1, dp[i]); // find it then dp[j] should + 1, compare with dp[i]
                     maxLeng = max(dp[i], maxLeng);
                 };
             };
        };
        return maxLeng;
    }
    int longestIncreasingSubsequence(vector<int> nums) {
        // write your code here
        int pos;
        if (nums.size() == 0) {
            return 0;
        };
        vector<int> dp(1, nums[0]);
        for (int i = 1; i < nums.size(); i++) {
             if (nums[i] >= dp.back()) {
                 dp.push_back(nums[i]);
             }
             else {
                 dp[binarySearch(dp, nums[i])] = nums[i];
             };
        };
        return dp.size();
    }
private:
    int binarySearch(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1, mid;
        while (start < end) {   
               mid = (start + end) / 2;
               if (nums[mid] < target) {
                   start = mid + 1;
               }    
               else {
                   end = mid;
               };
        };
        return start;
    }
};

int main(void) {
    Solution s;
    int arr [] = { 10, 22, 9, 33, 21, 50, 41, 60, 80 };
    // int arr [] = { 1, 4, 8, 13, 24, 30, 35};
    vector<int> nums(arr, arr + sizeof(arr) / sizeof(arr[0]));
    cout << s.longestIncreasingSubsequence(nums) << endl;
    // cout << s.binarySearch(nums, 0) << endl;
    // cout << s.binarySearch(nums, 2) << endl;
    // cout << s.binarySearch(nums, 20) << endl;
    // cout << s.binarySearch(nums, 29) << endl;

    return 0;
};
