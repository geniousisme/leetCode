#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty())
            return 0;
        if (nums.size() == 1)
            return nums[0];
        // if you robber the first one, then you can't robber the last one
        vector<int> nums1(nums.begin(), nums.end() - 1);
        // if you robber the last one, then you can't robber the first one
        vector<int> nums2(nums.begin() + 1, nums.end());
        return max(robberLinearOpt(nums1), robberLinearOpt(nums2));
    }
private:
    int robberLinear(vector<int>& nums) {        
        if (nums.size() == 1) {
            return nums[0];
        };
        
        vector<int> dp = {nums[0], max(nums[0], nums[1])}; // be careful!!!
        
        for (int i = 2; i < nums.size(); i++)
            dp.push_back(max(dp[i - 2] + nums[i], dp[i - 1]));
        
        return dp[dp.size() - 1];
    }

    int robberLinearII(vector<int>& nums) { // add 0 at first for dp, make code simpler
        if (nums.size() == 1) {
            return nums[0];
        };
        
        vector<int> dp(nums.size() + 1, 0); // be careful!!!

        dp[1] = nums[0];
        for (int i = 2; i < nums.size(); i++)
            dp.push_back(max(dp[i - 2] + nums[i - 1], dp[i - 1]));
        
        return dp[dp.size()];
    }
    int robberLinearOpt(vector<int>& nums) {  // space opt to O(1)
        int odd = 0, even = 0;
        
        for (int i = 0; i < nums.size(); i++) {
             if (i % 2)
                odd  = max(odd + nums[i], even);
             else 
                even = max(even + nums[i], odd);
        }; 
        return max(odd, even);
    }
};

int main(void) {
    Solution s;
    vector<int> nums = {1,3,1,3,100};
    cout << s.rob(nums) << endl;
    return 0;
};