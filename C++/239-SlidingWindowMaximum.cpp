#include <iostream>
#include <string>
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindowWithMaxFunc(vector<int>& nums, int k) {
                vector<int> res;
                if (!nums.empty()){
                   for (int i = 0; i < nums.size() - k + 1; i++){
                       int arr [k];
                       for (int j = 0; j < k; j++) {
                           arr[j] = nums[i + j];
                       };
                       res.push_back(*max_element(arr, arr + k));
                   };
                };
                return res;
    }
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
                vector<int> res;
                deque<int> dq;
                for (int i = 0; i < nums.size(); i++){
                    // let the latest element compare with the current elems in window
                    // notice that dequeu(windown) only store the index of nums, not the value.
                    // if the latest one bigger than current elems, remove the current element
                     while (!dq.empty() && nums[dq.back()] <= nums[i]) {
                            dq.pop_back();
                     };
                     // keep the length of window
                     dq.push_back(i);
                     if (dq.front() == i - k) {
                         dq.pop_front();
                     };
                     // since above code, the biggest one is always at the beginning of window
                     if (i - k + 1 >= 0) {
                         res.push_back(nums[dq[0]]);
                     };
                };
                return res;
    }
};

int main(int argc, char *argv []){
    Solution s;
    int arr [] = {7,2,4};
    vector<int> iarr(arr, arr + sizeof(arr) / sizeof(arr[0]));
    vector<int> res = s.maxSlidingWindow(iarr, 2);
    for (int i = 0; i < res.size(); i ++){
        cout << res[i] << " ";
    };
    cout << endl;
    return 0;
};