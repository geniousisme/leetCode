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
                vector<int> res;
                if (nums.empty()) {
                    res.push_back(-1);
                    res.push_back(-1);
                }
                else {
                    // cout << "findRightMost: " << findRightMost(nums, 0, nums.size() - 1, target) << endl;
                    // cout << "findLeftMost : " << findLeftMost(nums,  0, nums.size() - 1, target) << endl;
                    res.push_back(findLeftMost(nums,  0, nums.size() - 1, target));
                    res.push_back(findRightMost(nums, 0, nums.size() - 1, target));
                    // cout << "res: " << res[0] << " " << res[1] << endl;
                };
                return res;
    }
private:
    int p_target;
    vector<int> res;
    int findRightMost(vector<int>& nums, int start, int end, int target) {
        int mid;
        while (start < end - 1) {
               mid = (start + end) / 2;
               if (nums[mid] < target) {
                   start = mid;                   
               }
               else if (nums[mid] > target) {
                        end = mid;
               }
               else {
                   start = mid;
               };
        };
        if (nums[end] == target) {
            return end;
        };
        if (nums[start] == target) {
            return start;
        };
        return -1;
    }

    int findLeftMost(vector<int>& nums, int start, int end, int target) {
        int mid;
        while (start < end - 1) {
               mid = (start + end) / 2;
               if (nums[mid] < target) {
                   start = mid;                   
               }
               else if (nums[mid] > target) {
                        end = mid;
               }
               else {
                   end = mid;
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
    int arr [] = {3, 8, 8, 8, 8, 10, 10};
    vector<int> iarr(arr, arr + sizeof(arr) / sizeof(arr[0]));
    s.searchRange(iarr, 10);
    s.searchRange(iarr, 8);

    return 0;
};