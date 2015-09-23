#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        // if you robber the first one, then you can't robber the last one
        vector<int> nums1(nums.begin(), nums.end() - 1);
        // if you robber the last one, then you can't robber the first one
        vector<int> nums2(nums.begin() + 1, nums.end());
        return max(robberLinear(nums1), robberLinear(nums2));
    }
private:
    int robberLinear(vector<int>& nums) {
        if (nums.empty())
            return 0;
        if (nums.size() == 1)
            return nums[0];

        vector<int> dp = {nums[0], nums[1]};

        for (int i = 2; i < nums.size(); i++)
            dp.push_back(max(dp[i - 2] + nums[i], dp[i -1]));
        
        return dp[dp.size() - 1];
    }
};

int main(void) {
    Solution s;
    vector<int> nums = {4, 5, 7, 9, 11, 12};
    cout << s.rob(nums) << endl;
    return 0;
};