#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int hashSingleNumber(vector<int>& nums) {
        unordered_map<int, bool> hash;
        for (int i = 0; i < nums.size(); i++){
            if (!hash.count(nums[i])){
               hash[nums[i]] = true;
            } else {
              hash.erase(nums[i]);
            };
        };
        return hash.begin()->first;
    }
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < nums.size(); i++)   ans ^= nums[i];
        return ans;
    }
};

int main(void){
    Solution s;
    int arr[] = {1,1,2,2,3,3,4};
    vector<int> int_arr(arr, arr + 7);
    for (vector<int>::iterator it = int_arr.begin(); it != int_arr.end(); it++) cout << *it << endl;
    cout << s.singleNumber(int_arr) << endl;
    return 0;
};
