#include "include/common.h"

class Solution {
public:
    bool isPalindrome(int x) { // use math mehtod to solve
         if (x < 0) {
             return false;
         };
         int divisor = 1;
         while (x / divisor >= 10) {
                divisor *= 10;
         }
         while (x > 0) {
                if ((x / divisor) != (x % 10)) {
                     return false;
                } 
                else {
                    x = x % divisor / 10;
                    divisor /= 100;
                };
         };
         return true;
    }
    bool isPalindromeII(int x) { // use string to solve
         string int_str = to_string(x);
         int end = int_str.size() - 1, start = 0;
         while (start <= end) {
                if (int_str[start] != int_str[end]) {
                    return false;
                };
                start++;
                end--;
         };
         return true;
    }
};

int main(void) {
    Solution s;
    cout << s.isPalindrome(-2) << endl;
    cout << s.isPalindrome(2) << endl;
    cout << s.isPalindrome(24) << endl;
    cout << s.isPalindrome(122) << endl;
    cout << s.isPalindrome(1231) << endl;
    cout << s.isPalindrome(10001) << endl;
    cout << s.isPalindrome(1001) << endl;

    return 0;
};