#include "include/common.h"

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
         int idx1 = 0, idx2 = 0, i = 0, total_len = m + n;
         while (idx1 < m) {
                nums1.push_back(nums1[idx1]);
                idx1++;
         };
         nums1.erase(nums1.begin(), nums1.begin() + m);
         idx1 = n;
         while (idx1 < nums1.size() && idx2 < n) {
                if (nums1[idx1] < nums2[idx2]) {
                    nums1[i] = nums1[idx1];
                    idx1++;
                }
                else {
                    nums1[i] = nums2[idx2];
                    idx2++;
                };
                i++;
         };
         // cout << "idx2: " << idx2 << endl;
         // cout << nums2[idx2] << endl;
         // cout << "n: " << n << endl;         
         while (idx2 < n) {
                // cout << "nums2[" << idx2 << "]: " << nums2[idx2] << endl;
                nums1[total_len + idx2 - n] = nums2[idx2];
                idx2++;
         };
    }
};

int main(void) {
    Solution s;
    Utils utils;
    int arr1 [] = {1, 2, 3, 0, 0, 0};
    vector<int> nums1(arr1, arr1 + sizeof(arr1) / sizeof(arr1[0]));
    int arr2 [] = {2, 5, 6};
    vector<int> nums2(arr2, arr2 + sizeof(arr2) / sizeof(arr2[0]));
    s.merge(nums1, 3, nums2, 3);
    utils.printIntVector(nums1);
    return 0;
};