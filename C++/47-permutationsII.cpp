#include "include/common.h"

class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int>& nums) {
                        vector<vector<int> > res;
                        if (!nums.empty()) {
                            vector<int> perm, visited(nums.size(), 0);
                            sort(nums.begin(), nums.end());
                            permuteHelper(res, nums, visited, perm, nums.size());
                        };
                        return res;
    }
private:
    void permuteHelper(vector<vector<int> >& res, vector<int>& nums, vector<int>& visited, vector<int>& perm, int totalLen) {
         Utils u;
         if (perm.size() == totalLen) {
             res.push_back(perm);
             return;
         };
         // 跟 Permutations的解法一样，就是要考虑“去重”。先对数组进行排序，这样在DFS的时候，可以先判断前面的一个数是否和自己相等，
         // 相等的时候则前面的数必须使用了，自己才能使用，这样就不会产生重复的排列了。
         for (int i = 0; i < nums.size(); i++) {
              if (visited[i] == 0) {
                  if (i > 0 && visited[i - 1] == 0 && nums[i] == nums[i - 1]) { 
                      // the back two conditions wil cause that the program to visit the same again, 
                      // cause the duplication.
                      continue;
                  };
                  visited[i] = 1;
                  perm.push_back(nums[i]);
                  permuteHelper(res, nums, visited, perm, totalLen);
                  perm.pop_back();
                  visited[i] = 0;
              };
         };
    }
};

int main (void) {
    Solution s;
    Utils u;
    int iarr [] = {1, 1, 2};
    vector<int> nums(iarr, iarr + sizeof(iarr) / sizeof(iarr[0]));
    u.print2DIntVector(s.permuteUnique(nums));
    return 0;
};