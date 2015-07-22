#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
         unordered_map<int, int> num_idx_table;
         for (int i = 0; i < nums.size(); i++) {
              if (num_idx_table.count(nums[i]) == 0) {
                  num_idx_table[nums[i]] = i;
              } else {
                  if (k >= i - num_idx_table[nums[i]]) {
                      return true;
                  } 
                  // else {
                  //     num_idx_table[nums[i]] = i;
                  // };
              };
         };
         return false;
    }
};

int main(void) {
    Solution s;
    int arr [] = {1, 2, 3, 4, 2, 2};
    vector<int> test(arr, arr + sizeof(arr) / sizeof(arr[0]));
    cout << s.containsNearbyDuplicate(test, 1) << endl;
    return 0;
};