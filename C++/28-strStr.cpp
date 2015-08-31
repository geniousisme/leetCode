#include "include/common.h"

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack == nullptr) {
            return -1;
        };
        if (haystack.length() < needle.length()) {
                return -1;
        };
        if (needle.length() == 0) {
            return 0;
        };
        if (haystack.length() > 0 && needle.length() > 0) {
            int j = 0;
            for (int i = 0; i < haystack.length(); i++) {
                 if (haystack[i] == needle[0]) {
                     for (j = 1; j < needle.length(); j++) {
                          if (haystack[i + j] != needle[j]) {
                              break;
                          };
                     };
                     if (j == needle.length()) {
                         return i;
                     }
                 };
            };
        };
        return -1;
    }
};

int main(void) {
    Solution s;
    string haystack = "fgjsdhsi123ijj";
    string needle   = "1234";
    cout << s.strStr(haystack, needle) << endl;
    return 0;
};