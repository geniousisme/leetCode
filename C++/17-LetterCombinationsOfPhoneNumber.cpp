#include "include/common.h"

class Solution {
public:
    vector<string> letterCombinations(string digits) {
                   vector<string> comb;
                   if (digits.length() > 0) {
                       init();
                       dfs(comb, digits, digits.length(), "", 0);
                   };
                   return comb;
    }
private:
    unordered_map<char, string> letters;
    void init(void) {
         letters['2'] = "abc";
         letters['3'] = "def";
         letters['4'] = "ghi";
         letters['5'] = "jkl";
         letters['6'] = "mno";
         letters['7'] = "pqrs";
         letters['8'] = "tuv";
         letters['9'] = "wxyz";
         return;
    }
    void dfs(vector<string>& comb, string digits, int maxlength, string numbers, int idx) {
         if (numbers.length() == maxlength) {
             comb.push_back(numbers);
             return;
         };
         for (int i = 0; i < letters[digits[idx]].length(); i++) {
              dfs(comb, digits, maxlength, numbers + letters[digits[idx]][i], idx + 1);
         };
    }
};

int main(void) {
    Solution s;
    Utils utils;
    utils.printStrVector(s.letterCombinations("23"));
    utils.printStrVector(s.letterCombinations("4"));
    utils.printStrVector(s.letterCombinations("234"));
    return 0;
};