#include "include/common.h"

// Chris : NTR

class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> stack;
        int last = -1, maxLen = 0, end = 0;
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
                         maxLen = maxLen > i - last ? maxLen : i - last;
                     }
                     else {
                         // end = stack[stack.size() - 1];
                         maxLen = maxLen > i - stack[stack.size() - 1] ? maxLen : i - stack[stack.size() - 1];
                     };
                 };
             }
        };
        return maxLen;
    }
};

int main(void) {
    Solution s;
    cout << s.longestValidParentheses("()()") << endl;
    cout << s.longestValidParentheses("(()") << endl;
    cout << s.longestValidParentheses(")()()(") << endl;
    return 0;
};