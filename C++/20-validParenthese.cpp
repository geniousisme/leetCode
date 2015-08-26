#include "include/common.h"

class Solution {
public:
    bool isValid(string s) {
         vector<char> stack;
         if (s.length() % 2 == 1) {
             return false;
         };
         stack.push_back(s[0]);
         for (int i = 1; i < s.length(); i++) {
              if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                  stack.push_back(s[i]);
              }
              else {
                if (s[i] == ')' && stack[stack.size() - 1] != '(') {
                    return false;
                }
                else if (s[i] == '}' && stack[stack.size() - 1] != '{') {
                         return false;
                }
                else if (s[i] == ']' && stack[stack.size() - 1] != '[') {
                         return false;
                }
                else {
                    stack.pop_back();
                };
              };
         };
         return stack.empty();
    }
};

int main(void) {
    Solution s;
    cout << s.isValid("()[]{}") << endl;
    cout << s.isValid("([)]") << endl;
    cout << s.isValid(")") << endl;
    cout << s.isValid(")}{({))[{{[}") << endl;

    return 0;
};