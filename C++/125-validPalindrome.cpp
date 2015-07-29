#include "include/common.h"

class Solution {
public:
    bool isPalindrome(string s) {
         int end = s.size() - 1, start = 0;
         // int end_int, start_int;
         while (end >= start) {
                if (!isAlphabetic(s[end]) && !isNumeric(s[end])) {
                    end--;
                    continue;
                };
                if (!isAlphabetic(s[start]) && !isNumeric(s[start])) {
                    start++;
                    continue;
                };
                if (tolower(s[start]) != tolower(s[end])) {
                    return false;
                } 
                else {
                    end--;
                    start++;
                };
         };
         return true;
    }
    bool isAlphabetic(char c) {
         int int_c = c;
         if (int_c < 97) {
             int_c += 32;
         }
         if (int_c > 122 || int_c < 97) {
             return false;
         };
         return true;
    }
    bool isNumeric(char c) {
         int int_c = c;
         if (int_c > 57 || int_c < 48) {
             return false;
         };
         return true;
    }

};

int main(void) {
    char a = 'a', z = 'z', A = 'A', Z = 'Z', c0 = '0', c9= '9';
    int int_a = a, int_z = z, int_A = A, int_Z = Z, int_0 = c0, int_9 = c9;
    cout << "a: " << int_a << endl; // 97
    cout << "z: " << int_z << endl; // 122
    cout << "A: " << int_A << endl; // 65
    cout << "Z: " << int_Z << endl; // 90
    cout << "0: " << int_0 << endl; // 90
    cout << "9: " << int_9 << endl; // 90

    Solution s;
    cout << s.isPalindrome("A man, a plan, a canal: Panama") << endl;
    cout << s.isPalindrome("race a car") << endl;
    cout << s.isPalindrome("cabac") << endl;
    cout << s.isPalindrome("bb") << endl;
    cout << s.isPalindrome("b") << endl;
    cout << s.isPalindrome("") << endl;
    cout << s.isPalindrome("1a2") << endl;
    // cout << s.isPalindrome(".a") << endl;


    return 0;
};