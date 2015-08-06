#include "include/common.h"

class Solution {
public:
    int findMin(vector<int>& nums) {
        // return binarySearchI(nums, 0, nums.size() - 1);
        return binarySearchII(nums);

    }
private:
    int binarySearchI(vector<int>& nums, int start, int end) {
        if (end == start) {
            return nums[start];
        };
        if (nums[end] > nums[start]) {
            return nums[start];
        }
        else {
            int mid = (start + end) / 2;
            if (nums[mid] > nums[start]) {
                return binarySearchI(nums, mid + 1, end);
            }
            else if (nums[mid] < nums[start]) {
                return binarySearchI(nums, start, mid);
            }
            else {
                return binarySearchI(nums, start + 1, end);
            };
        };
    }
    int binarySearchII(vector<int>& nums) {
        int start = 0, end = nums.size() - 1, mid = 0;
        while(start < end) {
              mid = (start + end) / 2;
              if (nums[end] > nums[mid]) {
                  end = mid;
              } 
              else if (nums[end] < nums[mid]) {
                       start = mid + 1;
              }
              else {
                  end--;
              }
        };
        return nums[start];
    }
};

int main(void) {
    Solution s;
    int iarr [] = {3, 4, 5, 0, 1, 2, 3};
    vector<int> test(iarr, iarr + sizeof(iarr)/sizeof(iarr[0])); 
    cout << s.findMin(test) << endl;
    int iarr2 [] = {4, 1, 2, 3, 4};
    vector<int> test1(iarr2, iarr2 + sizeof(iarr2)/sizeof(iarr2[0])); 
    cout << s.findMin(test1) << endl;
    int iarr3 [] = {10, 1, 10, 10, 10};
    vector<int> test2(iarr3, iarr3 + sizeof(iarr3)/sizeof(iarr3[0])); 
    cout << s.findMin(test2) << endl;
    int iarr4 [] = {99};
    vector<int> test3(iarr4, iarr4 + sizeof(iarr4)/sizeof(iarr4[0])); 
    cout << s.findMin(test3) << endl;
    return 0;
};