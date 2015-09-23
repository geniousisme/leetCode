#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty())
            return 0;
        if (nums.size() == 1)
            return nums[0];
        
        vector<int> robberVal;
        robberVal.push_back(nums[0]);
        robberVal.push_back(max(nums[0], nums[1]));

        for (int i = 2; i < nums.size(); i++)
            robberVal.push_back(max(robberVal[i - 1], robberVal[i - 2] + nums[i]));
        
        return robberVal[nums.size() - 1];
    }
};

int main(void) {
    Solution s;
    vector<int> nums1 = {4, 5, 7, 9, 11};
    cout << s.rob(nums1) << endl;
    vector<int> nums2 = {4, 5};
    cout << s.rob(nums2) << endl;
    vector<int> nums3 = {10};
    cout << s.rob(nums3) << endl;
    return 0;
};