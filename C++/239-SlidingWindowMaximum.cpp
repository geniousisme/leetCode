#include <iostream>
#include <string>
#include <vector>


class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
                     std::vector<int> res;
                     if (!nums.empty()){
                        for (int i = 0; i < nums.size() - k + 1; i++){
                            int arr [k];
                            for (int j = 0; j < k; j++) arr[j] = nums[i + j];
                            res.push_back(*std::max_element(arr, arr + k));
                        };
                     };
                     return res;
    }
};

int main(int argc, char *argv []){
    Solution s;
    int arr [] = {1,3,-1,-3,5,3,6,7};
    std::vector<int> iarr(arr, arr + sizeof(arr) / sizeof(arr[0]));
    std::vector<int> res = s.maxSlidingWindow(iarr, 3);
    for (int i = 0; i < res.size(); i ++){
        std::cout << res[i] << " ";
    };
    std::cout << std::endl;
    return 0;
};