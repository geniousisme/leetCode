#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

// Chris:NTR

class Solution {
public:
    bool containsNearbyAlmostDuplicateI(vector<int>& nums, int k, int t) {
         if (k < 1 || t < 0) {
             return false;
         };
         unordered_map<int, int> num_table;
         for (int j = 0; j < nums.size(); j++) {
              // cout << "size:" << nums.size() << endl;
              int key = nums[j] / max(1, t);
              int keyArr [] = {key - 1, key, key + 1};
              for (int i = 0; i < 3; i ++) {
                   if (num_table.count(keyArr[i]) > 0) {
                       long int diff = num_table[keyArr[i]] - nums[j]; 
                       // notice, long int will cause a lot of function not working.
                       // and dont put this line before the line above, 
                       // unordered_map will generate the case by itself.
                       // if (j - num_table[keyArr[i]] <= k) { // this condition not that workable, 
                       // since after being divided, some negative number will become 0.
                       if (abs(diff) <= t) {
                           return true;
                       };
                   };
              };
              num_table[key] = nums[j];
              if (j >= k) {
                  num_table.erase(nums[j - k] / max(1, t));
              };
         };
         return false;
    }
private:
    int cmpint(int a, int b) { // 
        return a >= b ? a : b;
    }
};

int main (void) {
    Solution s;
    int arr [] = {1};
    vector<int> iarr(arr, arr + 1);
    // [-1,2147483647], 
    cout << s.containsNearbyAlmostDuplicate(iarr, 1, 1) << endl;
    return 0;
};