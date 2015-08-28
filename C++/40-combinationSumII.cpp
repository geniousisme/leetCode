#include "include/common.h"

class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int>& candidates, int target) {
                        vector<vector<int> > res;
                        if (!candidates.empty()) {
                            vector<int> comb;
                            sort(candidates.begin(), candidates.end());
                            combSumHelper(res, candidates, comb, target, 0);
                        };
                        return res;
    }
private:
    void combSumHelper(vector<vector<int> >& res, vector<int>& candidates, vector<int>& comb, int target, int start) {
         if (target == 0) {
             res.push_back(comb);
         };
         for (int i = start; i < candidates.size(); i++) {
              if (i > start && candidates[i] == candidates[i - 1]) {
                  continue;
              };
              if (target >= candidates[i]) {
                  comb.push_back(candidates[i]);
                  combSumHelper(res, candidates, comb, target - candidates[i], i + 1);
                  comb.pop_back();
              };
         };
    }
};

int main(void) {
    Solution s;
    Utils utils;
    int arr [] = {10,1,2,7,6,1,5};
    vector<int> test(arr, arr + sizeof(arr) / sizeof(arr[0]));
    utils.printInt2DVector(s.combinationSum2(test, 8));
    return 0;
};