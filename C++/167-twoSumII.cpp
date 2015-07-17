#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0, end = numbers.size() - 1;
        vector<int> res;
        while (end > start){
              if (numbers[end] + numbers[start] > target)  end -= 1;
              else if (numbers[end] + numbers[start] < target) start += 1;
              else {
                // cout << "start: " << (start + 1) << " ";
                res.push_back(start + 1);
                // cout << "end: " << (end + 1) << endl;
                res.push_back(end   + 1);
                break;
              };   
        };
        return res;
    }
};

int main(int argc, char *argv []){
    Solution s;
    int arr [] = {2, 7, 11, 12, 15};
    vector<int> test(arr, arr + sizeof(arr) / sizeof(arr[0]));
    s.twoSum(test, 23);
    return 0;
};