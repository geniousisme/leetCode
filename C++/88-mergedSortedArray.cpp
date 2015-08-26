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
         if (idx2 < n) {
             nums1[total_len + idx2 - n] = nums2[idx2];
             idx2++;
         };
    }
};