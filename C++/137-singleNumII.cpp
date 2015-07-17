#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int one = 0, two = 0, three = 0;
        for(int i = 0; i < nums.size(); i++){
           two |= nums[i] & one;
           one ^= nums[i];
           three = ~(two & one);
           two &= three;
           one &= three;
        };
        // cout << "bin: " << (one & 1) << endl;
        return one;
    }
};

int main(int argc, char *argv []){
    Solution s;
    int arr[] = {1,1,1,2,2,2,3};
    vector<int> int_arr(arr, arr + 7);
    // for (vector<int>::iterator it = int_arr.begin(); it != int_arr.end(); it++) cout << *it << ',';
    // cout << endl;
    cout << "ans: " << s.singleNumber(int_arr) << endl;
    return 0;
};