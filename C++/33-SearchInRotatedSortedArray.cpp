#include "include/common.h"

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) {
            return 0;
        };
        return binarySearch(nums, 0, nums.size() - 1, target);
    }
private:
    int binarySearch(vector<int>& nums, int start, int end, int target) {
        int mid;
        while (start < end) {
               mid = (end + start) / 2;
               if (nums[mid] == target) {
                   return mid;
               }
               if (nums[start] > nums[mid]) {
                   if (nums[mid] <= target && target <= nums[end]) {
                       start = mid;
                   }
                   else {
                       end = mid - 1;
                   };
               }
               else {
                   if (nums[start] <= target && target <= nums[mid]) {
                       end = mid;
                   }
                   else {
                       start = mid + 1;
                   };
               };
        };
        if (nums[start] == target) {
            return start;
        };
        if (nums[end] == target) {
            return end;
        };
        return -1;
    }
};

int main(void) {
    Solution s;
    int iarr [] = {3, 4, 5, 0, 1, 2};
    vector<int> test(iarr, iarr + sizeof(iarr)/sizeof(iarr[0])); 
    cout << s.search(test, 5) << endl;
    cout << s.search(test, 3) << endl;
    cout << s.search(test, 0) << endl;
    cout << s.search(test, 1) << endl;
    cout << s.search(test, 2) << endl;
    cout << s.search(test, 99) << endl;
    return 0;
};