#include "include/common.h"

class Solution {
public:
    vector<vector<int> > combinationSum(vector<int>& candidates, int target) {
                         vector<vector<int> > res;
                         vector<int> comb;
                         if (!candidates.empty()) {
                             sort(candidates.begin(), candidates.end());
                             combSumHelper(res, candidates, comb, target, 0, 0);
                         };
                         return res;
    }
    // following is a 16ms version, mine get 24 ms since not pruning, check combSumHelperII to see how to prune.
    // vector<vector<int> > combinationSumII(vector<int>& candidates, int target) {
    //                      vector<vector<int> > res;
    //                      vector<int> comb;
    //                      if (!candidates.empty()) {
    //                          sort(candidates.begin(), candidates.end());
    //                          combSumHelperII(res, candidates, comb, target, 0);
    //                      };
    //                      return res;
    // }
private:
    int targetSum;
    void combSumHelper(vector<vector<int> >& res, vector<int>& candidates, vector<int>& comb, int target, int currentSum, int idx) {
         // if (currentSum > target) {
         //     return;
         // }
         if (currentSum == target) {
             res.push_back(comb);
             return;
         };
         for (int i = idx; i < candidates.size(); i++) {
              if (currentSum + candidates[i] <= target) {
                  if (i > idx && candidates[i] == candidates[i - 1]) continue;
                  comb.push_back(candidates[i]);
                  combSumHelper(res, candidates, comb, target, currentSum + candidates[i], i);            
                  comb.pop_back();
              };
         };
    };
    // void combSumHelperII(vector<vector<int> >& res, vector<int>& candidates, vector<int>& comb, int currentSum, int idx) {
    //      if (currentSum == 0) {
    //          res.push_back(comb);
    //          return;
    //      };
    //      for (int i = idx; i < candidates.size(); i++) {
    //           if (candidates[i] <= currentSum) {
    //               if (i > idx && candidates[i] == candidates[i - 1]) {
    //                 continue;
    //               };
    //               comb.push_back(candidates[i]);
    //               combSumHelperII(res, candidates, comb, currentSum - candidates[i], i);            
    //               comb.pop_back();
    //           };
    //      };
    // };
};

int main(void) {
    Solution s;
    Utils utils;
    int arr [] = {8,7,4,3};
    vector<int> test(arr, arr + sizeof(arr) / sizeof(arr[0]));
    utils.printInt2DVector(s.combinationSum(test, 11));
    return 0;
};