#include "include/common.h"

// Chris:TODO::NTR!!

class Solution {
public:
    vector<int> grayCodeI(int n) {
                int highestBit = 0;
                vector<int> res(1, 0);
                for(int i = 0; i < n; i++) {
                    highestBit = pow(2, i);
                    for (int k = res.size() - 1; k > -1; k--) {
                         res.push_back(res[k] + highestBit);
                    };
                };
                // for(int i = 0; i < res.size(); i++) cout << res[i] << endl;
                return res;
    }
    vector<int> grayCode(int n) {
                vector<int> res;
                int size = 1 << n;
                // cout << "size: " << size << endl;
                for(int i = 0; i < size; i++) {
                    res.push_back((i >> 1) ^ i);
                };
                return res;
    }
};

int main(void) {
    Solution s;
    Utils utils;
    utils.printIntVector(s.grayCode(2));
    return 0;
};