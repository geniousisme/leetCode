#include "include/common.h"

class Solution {
public:
    vector<int> recSearchRange(vector<int>& nums, int target) {
                p_target = target;
                res.push_back(startBinarySearch(nums, 0, nums.size()));
                res.push_back(endBinarySearch(nums,   0, nums.size()));
                return res;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
                p_target = target;
                res.push_back(findLeftMost(nums,  target));
                res.push_back(findRightMost(nums, target));
                // cout << "res: " << res[0] << " " << res[1] << endl;
                return res;
    }
private:
    int p_target;
    vector<int> res;
    int findRightMost(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        while (start <= end) {
               int mid = start + (end - start) / 2;
               if (nums[mid] > target) {
                   end = mid - 1;
               }
               else {
                   start = mid + 1;
               };
        };
        if (end >= 0 && end < nums.size() && nums[end] == target) {
            return end;
        }
        else {
            return -1;
        };
    }
    int findLeftMost(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        while (start <= end) {
               int mid = start + (end - start) / 2;
               if (target > nums[mid]) {
                   start = mid + 1;
               }
               else {
                   end = mid - 1;
               }
        };
        if (start >= 0 && start < nums.size() && nums[start] == target) {
            return start;
        }
        else {
            return -1;
        };
    }
    int startBinarySearch(vector<int>& nums, int start, int end) {
        if (end - start == 1) {
            if  (nums[end] == p_target && nums[start] < p_target) {
                 return end;
            }
            else if (nums[start] == p_target) {
                 return start;
            }
            else {
                 return -1;
            };
        }; 
        int mid = (end + start) / 2;
        if (nums[mid] >= p_target) {
            return startBinarySearch(nums, start, mid);
        }
        else {
            return startBinarySearch(nums, mid, end);
        };   
    }

    int endBinarySearch(vector<int>& nums, int start, int end) {
        if (end - start == 1) {
            if (nums[start] == p_target && nums[end] > p_target) {
                return start;
            }
            else if (nums[end - 1] == p_target) { // deal with the boundary
                return end - 1;
            }
            else {
                return -1;
            };
        };
        int mid = (end + start) / 2;
        if (nums[mid] > p_target) {
            return endBinarySearch(nums, start, mid);
        }
        else {
            return endBinarySearch(nums, mid, end);
        };
    }
};

int main(void) {
    Solution s;
    int arr [] = {5, 7, 7, 8, 8, 10};
    vector<int> iarr(arr, arr + sizeof(arr) / sizeof(arr[0]));
    s.searchRange(iarr, 5);
    return 0;
};