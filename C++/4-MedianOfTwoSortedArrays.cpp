#include "include/common.h"

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
           inf = numeric_limits<double>::infinity();
           // cout << "inf " << inf << endl;
           if ((nums1.size() + nums2.size()) % 2 == 1) {
               return findKth(nums1, nums2, 0, 0, (nums1.size() + nums2.size()) / 2 + 1);
           }
           else {
               // cout << findKth(nums1, nums2, 0, 0, (nums1.size() + nums2.size()) / 2) << endl;
               // cout << findKth(nums1, nums2, 0, 0, (nums1.size() + nums2.size()) / 2 + 1) << endl;
               return (findKth(nums1, nums2, 0, 0, (nums1.size() + nums2.size()) / 2) + findKth(nums1, nums2, 0, 0, (nums1.size() + nums2.size()) / 2 + 1)) * 0.5;
           };
    }
private:
    // Chris : NTR
    double key1, key2, inf;
    int findKth(vector<int>& nums1, vector<int>& nums2, int start1, int start2, int k) {
        if (start1 >= nums1.size()) {
            return nums2[start2 + k - 1];
        };
        if (start2 >= nums2.size()) {
            return nums1[start1 + k - 1];
        };
        if (k == 1) {
            return nums1[start1] < nums2[start2] ? nums1[start1] : nums2[start2];
        };
        key1 = start1 + k / 2 - 1 < nums1.size() ? nums1[start1 + k / 2 - 1] : inf;
        key2 = start2 + k / 2 - 1 < nums2.size() ? nums2[start2 + k / 2 - 1] : inf;

        if (key1 < key2) {
            return findKth(nums1, nums2, start1 + k / 2, start2, k - k / 2);
        }
        else {
            return findKth(nums1, nums2, start1, start2 + k / 2, k - k / 2);
        };
    }
};

int main (void) {
    Solution s;
    int iarr1 [] = {1};
    vector<int> nums1(iarr1, iarr1 + sizeof(iarr1) / sizeof(iarr1[0]));
    int iarr2 [] = {2, 3, 4, 5, 6};
    // 1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7
    vector<int> nums2(iarr2, iarr2 + sizeof(iarr2) / sizeof(iarr2[0]));
    cout << s.findMedianSortedArrays(nums1, nums2) << endl;
    return 0;
};