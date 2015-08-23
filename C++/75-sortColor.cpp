#include "include/common.h"

class Solution {
public:
    void sortColorsI(vector<int>& nums) {
         int zeroPtr = 0, i = 0, twoPtr = nums.size() - 1;
         while (i <= twoPtr) {
                if (nums[i] == 0) {
                    swap(nums, i, zeroPtr);
                    zeroPtr++;
                    i++;
                }
                else if (nums[i] == 2) {
                         swap(nums, i, twoPtr);
                         twoPtr--;
                }
                else {
                    i++;
                };
         };
    }
    void sortColors(vector<int>& nums) {
         int count [] = {0, 0, 0};
         for (int i = 0; i < nums.size(); i++) {
              count[nums[i]]++;
         };
         for (int i = 0, j = 0; i < 3 && j < nums.size(); i++) {
              while (count[i] > 0) {
                     nums[j] = i;
                     count[i]--;
                     j++;
              };
         };
    };
private:
    int tmp;
    void swap(vector<int>& nums, int ptr1, int ptr2) {
         tmp        = nums[ptr1];
         nums[ptr1] = nums[ptr2];
         nums[ptr2] = tmp;
         return;
    }
};

int main(void) {
    Utils utils;
    Solution s;
    int iarr [] = {0, 1, 0, 0, 1, 1, 1, 2, 0, 1, 0, 2, 1, 2};
    vector<int> arr(iarr, iarr + sizeof(iarr) / sizeof(iarr[0]));
    s.sortColors(arr);
    utils.printIntVector(arr);
    return 0;

};