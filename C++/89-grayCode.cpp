#include "include/common.h"

// Chris:TODO::NTR!!

class Solution {
public:
    vector<int> grayCode(int n) {
                int highestBit = 0;
                vector<int> res(1, 0);
                for (int i = 0; i < n; i++) { 
                     highestBit = 1 << i;
                     for (int k = res.size() - 1; k > -1; k--) {
                          res.push_back(res[k] + highestBit);
                     };
                };
                return res;
    }
};

int main(void) {
    Solution s;
    
};