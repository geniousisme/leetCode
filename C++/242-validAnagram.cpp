#include "include/common.h"

class Solution {
public:
    bool isAnagram(string s, string t) {
         if (s.length() != t.length()) {
             return false;
         };
         sort(s.begin(), s.end());
         sort(t.begin(), t.end());
         for(int i = 0; i < s.length(); i++) {
             if (s[i] != t[i]) {
                 return false;
             };
         };
         return true;
    }
};

int main(void) {
    Solution s;
    string test1 = "bdac", test2 = "abcd";
    cout << s.isAnagram(test1, test2) << endl; 
    test1 = "car", test2 = "rat";
    cout << s.isAnagram(test1, test2) << endl; 
    return 0;
};