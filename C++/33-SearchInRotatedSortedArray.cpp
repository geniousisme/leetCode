#include "include/common.h"

class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size() - 1, target);
    }
private:
    int binarySearch(vector<int>& nums, int start, int end, int target) {
        if (end == start) {
            if (nums[start] == target) {
                return start;
            }
            else {
                return -1;
            }
        };
        int mid = (start + end) / 2;
        if (nums[start] > target) {
            if (nums[mid] > nums[end]) {

            } 
            else {

            };
        }
        else if (nums[start] < target){
                 if (nums[mid] > nums[end]) {

                 } 
                 else {

                 };
        }
        else {
            return start;
        };
        
    }
};

int main(void) {
    Solution s;
    int iarr [] = {3, 4, 0, 1, 2};
    vector<int> test(iarr, iarr + sizeof(iarr)/sizeof(iarr[0])); 
    cout << s.search(test, 5) << endl;
    cout << s.search(test, 3) << endl;
    cout << s.search(test, 0) << endl;
    cout << s.search(test, 2) << endl;
    cout << s.search(test, 99) << endl;
    // int iarr2 [] = {4, 1, 2, 3};
    // vector<int> test1(iarr2, iarr2 + sizeof(iarr2)/sizeof(iarr2[0])); 
    // cout << s.search(test1) << endl;
    // int iarr3 [] = {10, 1, 10, 10, 10};
    // vector<int> test2(iarr3, iarr3 + sizeof(iarr3)/sizeof(iarr3[0])); 
    // cout << s.search(test2) << endl;
    // int iarr4 [] = {99};
    // vector<int> test3(iarr4, iarr4 + sizeof(iarr4)/sizeof(iarr4[0])); 
    // cout << s.search(test3) << endl;
    return 0;
};