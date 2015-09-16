#include "include/common.h"

class Solution {
public:
    bool wordBreak(string s, unordered_set<string>& wordDict) {
      vector<bool> dp(s.length() + 1, false);
      unordered_set<string>::const_iterator got;
      dp[0] = true;
      for (int i = 1; i < s.length() + 1; i++) {
        for (int j = 0; j < i; j++) {   
          got = wordDict.find(s.substr(j, i - j));
          if (dp[j] && got != wordDict.end()) {
            dp[i] = true;
          };
        };
      };
      return dp[s.length()];
    }
};

int main(void) {
  Solution s;
  string test = "leetcode";
  unordered_set<string> dict = { "leetcode" };
  cout << s.wordBreak(test, dict) << endl;
  string test1 = "ab";
  unordered_set<string> dict1 = { "a", "b" };
  cout << s.wordBreak(test1, dict1) << endl;
  string test2 = "a";
  unordered_set<string> dict2 = { "a"};
  cout << s.wordBreak(test2, dict2) << endl;
  return 0;
};