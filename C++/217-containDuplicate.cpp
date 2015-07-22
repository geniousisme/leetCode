#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    bool containsDuplicateI(vector<int>& nums) {
         if (nums.size() == 0 || nums.size() == 1) {
            return false;
         } 
         unordered_map<int, bool> num_table;
         for (int i = 0; i < nums.size(); i++) {
              if (num_table[nums[i]]){
                  return true;
              } else {
                  num_table[nums[i]] = true;
              };
         };
         return false;
    }
    // Chris: Use the advantage that array reading time is faster than unordered_map
    // declare a arr with maximum int size, store the number with the value as index.
    bool containsDuplicate(vector<int>& nums) {
         bool array[0xFFFFF] = {};
         for(int i = 0; i< nums.size(); i++) {
             if(array[nums[i]]) {
                return true;
             } else {
                array[nums[i]] = true;
             };
         }
        return false;
    }

    bool containsDuplicateII(vector<int>& nums) {
         sort(nums.begin(), nums.end());
         int len=nums.size();
         for(int i=1; i<len; i++){
            if(nums[i-1]==nums[i]){
                return true;
            }
         }
         return false;
    }
};

int main(void) {
    Solution s;
    int arr [] = {1, 2, 3, 4, 2, 5};
    vector<int> test(arr, arr + sizeof(arr) / sizeof(arr[0]));
    cout << s.containsDuplicate(test) << endl;
    return 0;
};