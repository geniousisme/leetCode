#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf1(vector<int>& nums) {
                vector<int> res(nums.size(), 1);
                for (int i = 1; i < nums.size(); i++) {
                     res[i] = nums[i - 1] * res[i - 1];
                };
                int right_product = nums[nums.size() - 1];
                for (int i = nums.size() - 2; i > -1; i--){
                     res[i] *= right_product;
                     right_product *= nums[i];
                };
                // for (int i = 0; i < nums.size(); i++) cout << res[i] << " ";
                // cout << endl;
                return res;
    }
    // following is not really good solution, since you hv to deal with some special case
    // ex. [0, 0], [1, 0]
    vector<int> productExceptSelf(vector<int>& nums) {
                int productSum = 1;
                for (int i = 0; i < nums.size(); i++) {
                    productSum *= nums[i];
                };
                vector<int> res(nums.size(), productSum);
                for (int i = 0; i < nums.size(); i++) {
                     if (nums[i] > 0) {
                         res[i] /= nums[i];
                     };
                };
                // for (int i = 0; i < nums.size(); i++) cout << res[i] << " ";
                // cout << endl;
                return res;
    }
};  

int main(void){
    Solution s;
    int arr [] = {3, 4, 5, 6};
    vector<int> iarr(arr, arr + 4);
    s.productExceptSelf(iarr);
    return 0;
};