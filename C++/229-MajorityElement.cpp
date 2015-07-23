#include "include/common.h"

// Chris:NTR!

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
                int candidate1 = 0, candidate2 = 0, count1 = 0, count2 = 0;
                for (int i = 0; i < nums.size(); i++) {
                     if (candidate1 == nums[i]) { 
                         // notice: this should put above, since the repeated value will 
                         // not replace the candidate2.
                         count1++;
                     }
                     else if (candidate2 == nums[i]) {
                              count2++;
                     }
                     else if (count1 == 0) {
                              candidate1 = nums[i];
                              count1 = 1;
                     }
                     else if (count2 == 0) {
                              candidate2 = nums[i];
                              count2 = 1;
                     }
                     else {
                         count1--;
                         count2--;    
                     };
                };
                
                count1 = count2 = 0;
                vector<int> res;
                
                for (int i = 0; i < nums.size(); i++) {
                     if (nums[i] == candidate1) {
                         count1++;
                     }
                     else if (nums[i] == candidate2) {
                              count2++;                              
                     };
                }; 
                if (count1 > nums.size() / 3) {
                    res.push_back(candidate1);
                };
                if (count2 > nums.size() / 3) {
                    res.push_back(candidate2);
                };
                return res;
    }
};

int main(void) {
    Solution s;
    int arr [] = {8,8,7,7,7};
    vector<int> iarr(arr, arr + sizeof(arr) / sizeof(arr[0]));
    s.majorityElement(iarr);
    return 0;
}