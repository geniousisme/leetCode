#include "include/common.h"

class Solution {
public:
    vector<vector<int> > subsetsWithDup(vector<int>& nums) {
                         vector<vector<int> > res;
                         if (!nums.empty()) {
                             vector<int> comb;
                             sort(nums.begin(), nums.end());
                             subsetHelper(res, nums, comb, 0);
                         };
                         return res;
    }

private:
    void subsetHelper(vector<vector<int> >& res, vector<int>& nums, vector<int>& comb, int start) {
         res.push_back(comb);
         for (int i = start; i < nums.size(); i++) {
              if (i > start && nums[i] == nums[i - 1]) {
                  continue;
              };
              comb.push_back(nums[i]);
              subsetHelper(res, nums, comb, i + 1);
              comb.pop_back();
         };
         return;
    }
};

int main(void) {
    Solution s;
    Utils utils;
    int arr [] = {1, 2, 2, 2};
    vector<int> nums(arr, arr + sizeof(arr) / sizeof(arr[0]));
    utils.print2DIntVector(s.subsetsWithDup(nums));
    return 0;
};