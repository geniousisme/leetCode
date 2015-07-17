#include <iostream>

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while(n){
            count ++;
            n &= (n - 1);
        };
        return count;
    }
};

int main(int argc, char *argv []){
    Solution s;
    std::cout << "count: " << s.hammingWeight(9) << std::endl;
    std::cout << "count: " << s.hammingWeight(7) << std::endl;
    return 0;
};