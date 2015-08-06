#include "include/common.h"

class Solution {
public:
    int findMin(vector<int>& nums) {
        // return binarySearchI(nums, nums[0], 0, nums.size() - 1);
        // return binarySearchII(nums, 0, nums.size() - 1);
        return binarySearchIII(nums);

    }
private:
    int binarySearchI(vector<int>& nums, int currMin, int start, int end) {
        if (end == start) {
            return currMin;
        };
        int mid = (start + end) / 2;
        if (nums[mid] < nums[end]) {
            currMin = nums[mid];
            return binarySearchI(nums, currMin, start, mid); // the minmum wont be in [mid+1:end], search [start:mid]
        } 
        else {
            currMin = currMin > nums[end] ? nums[end] : currMin;
            return binarySearchI(nums, currMin, mid + 1, end); // the minimum wont be in [start:mid], search [mid+1:end]
        };
    }
    int binarySearchII(vector<int>& nums, int start, int end) {
        if (end == start) {
            return nums[start];
        } 
        if (nums[end] > nums[start]) {
            return nums[start];
        }
        else {
            int mid = (start + end) / 2;
            if (nums[mid] < nums[end]) {    
                return binarySearchII(nums, start, mid); // the minmum wont be in [mid+1:end], search [start:mid]
            } 
            else {
                return binarySearchII(nums, mid + 1, end); // the minimum wont be in [start:mid], search [mid+1:end]
            };
        };
    }
    int binarySearchIII(vector<int>& nums) {
        int start = 0, end = nums.size() - 1;
        while(start < end) {
              if (nums[start] < nums[end]) {
                  return nums[start];
              }
              else {
                  int mid = (start + end) / 2;
                  if (nums[start] < nums[mid]) {
                      start = mid + 1;  
                  } 
                  else { // nums[start] > nums[mid]
                      end = mid;
                      start++;
                  };  
              };
        }
        return nums[start];
        
    }
};
int main(void) {
    Solution s;
    int iarr [] = {4, 5, 0, 1, 2};
    vector<int> test(iarr, iarr + sizeof(iarr)/sizeof(iarr[0])); 
    cout << s.findMin(test) << endl;
    int iarr2 [] = {1, 2, 3, 4};
    vector<int> test1(iarr2, iarr2 + sizeof(iarr2)/sizeof(iarr2[0])); 
    cout << s.findMin(test1) << endl;
    int iarr3 [] = {2, -1, 1};
    vector<int> test2(iarr3, iarr3 + sizeof(iarr3)/sizeof(iarr3[0])); 
    cout << s.findMin(test2) << endl;
    int iarr4 [] = {99};
    vector<int> test3(iarr4, iarr4 + sizeof(iarr4)/sizeof(iarr4[0])); 
    cout << s.findMin(test3) << endl;
    return 0;
};