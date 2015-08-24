class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int length = nums.size() + 1;
        int sum = (length * (length - 1)) / 2, realSum = 0;
        for (int i = 0; i < nums.size(); i++) {
             realSum += nums[i];
        };
        return sum - realSum;
    }
};