#include "include/common.h"

class Solution {
public:
    vector<vector<int> > subsets(vector<int>& nums) {
                        vector<vector<int> > res;
                        if (!nums.empty()) {     
                            sort(nums.begin(), nums.end());
                            vector<int> list;
                            dfs(res, nums, list, 0);
                        };
                        return res;
    }
private:
    void dfs(vector<vector<int> >& res, vector<int>& nums, vector<int>& list, int startPos) {
         res.push_back(list);
         for (int i = startPos; i < nums.size(); i++) {
              list.push_back(nums[i]);
              dfs(res, nums, list, i + 1);
              list.pop_back();
         };
         return;
    }
};

int main(void) {
    Solution s;
    vector<int> test;
    s.subsets(test);
    return 0;
};