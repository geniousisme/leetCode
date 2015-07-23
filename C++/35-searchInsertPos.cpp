#include "include/common.h"

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        p_target = target;
        if (target < nums[0]) {
            return 0;
        }
        else if (target > nums[nums.size() - 1]) {
                 return nums.size();
        }
        else {
            return binarySearch(nums, 0, nums.size());
        };
    
    }
private:
    int p_target;
    int binarySearch(vector<int>& nums, int start, int end) {
        if (end - start == 1 && (p_target > nums[start] && nums[end] >= p_target)) {
            return end;
        };
        int mid = (end + start) / 2;
        if (p_target > nums[mid]) {
            return binarySearch(nums, mid, end);  
        } 
        else if (p_target < nums[mid]) {    
                 return binarySearch(nums, start, mid);
        } 
        else {
            return mid;
        }
    }
};

int main(void) {
    Solution s;
    int arr [] = {1,3,5,6};
    vector<int> iarr(arr, arr + sizeof(arr) / sizeof(arr[0]));
    cout << s.searchInsert(iarr, 5) << endl;
    cout << s.searchInsert(iarr, 2) << endl;
    cout << s.searchInsert(iarr, 7) << endl;
    cout << s.searchInsert(iarr, 0) << endl;
    return 0;
}