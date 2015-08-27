#include "include/common.h"

// Chris : NTR

class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> stack;
        int last = -1, maxParentLen = 0;
        for (int i = 0; i < s.length(); i++) {
             if (s[i] == '(') {
                 stack.push_back(i);
             }
             else {
                 if (stack.empty()) {
                     last = i;
                 }
                 else {
                     stack.pop_back();
                     if (stack.empty()) {
                         maxParentLen = maxParentLen > i - last ? maxParentLen : i - last;
                     }
                     else {
                         maxParentLen = maxParentLen > i - stack[stack.size() - 1] ? maxParentLen : i - stack[stack.size() - 1];
                     };
                 };
             };
        };
        return maxParentLen;
    }
};

int main(void) {
    Solution s;
    cout << s.longestValidParentheses("()()") << endl;
    cout << s.longestValidParentheses("(()") << endl;
    cout << s.longestValidParentheses(")()()(") << endl;
    return 0;
};