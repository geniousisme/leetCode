#include "../include/common.h"

class Solution {
public:
    /**
     * @param nums: The integer nums.
     * @param target: Target number to find.
     * @return: The first position of target. Position starts from 0. 
     */
     // Chris:NTR
    int binarySearch(vector<int> &nums, int target) {
        // write your code here
        if (!nums.empty()) {
            int left = 0, right = nums.size() - 1, mid;
            while (left < right) {
                   mid = (left + right) / 2;
                   if (nums[mid] > target) {
                       right = mid - 1;
                   }
                   else if (nums[mid] < target) {
                            left = mid + 1;
                   } 
                   else {
                       right = mid;
                   };
            };
            if (nums[right] == target) {
                return right;
            }
            if (nums[left] == target) {
                return left;
            }   
        }
        return -1;
    }
};

int main(void) {
    Solution s;
    int iarr [] = {1, 2, 3, 3, 4, 5, 6, 7, 9, 10};
    vector<int> nums(iarr, iarr + sizeof(iarr) / sizeof(iarr[0]));
    cout << s.binarySearch(nums, 3) << endl;
    cout << s.binarySearch(nums, 1) << endl;
    cout << s.binarySearch(nums, 10) << endl;
    cout << s.binarySearch(nums, 8) << endl;
    return 0;
}
