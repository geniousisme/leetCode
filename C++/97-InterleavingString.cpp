#include "include/common.h"

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
      int len1 = s1.length() + 1, len2 = s2.length() + 1, len3 = s3.length() + 1;
      if (len1 + len2 != len3 + 1) {
        return false;
      };
      vector<vector<bool> > stringTable (len1, vector<bool>(len2, false));
      stringTable[0][0] = true;
      for (int i = 1; i < len1; i++) {
        stringTable[i][0] = stringTable[i - 1][0] && (s1[i - 1] == s3[i - 1]);
      };
      for (int j = 1; j < len2; j++) {
        stringTable[0][j] = stringTable[0][j - 1] && (s2[j - 1] == s3[j - 1]);
      };
      for (int i = 1; i < len1; i++) {
        for (int j = 1; j < len2; j++) {
          stringTable[i][j] = ((stringTable[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (stringTable[i][j - 1] && s2[j - 1] == s3[i + j - 1]));
        };
      };
      return stringTable[len1 - 1][len2 - 1];
    }
};

int main(void) {
  Solution s;
  cout << s.isInterleave("aabcc", "dbbca", "aadbbcbcac") << endl;
  cout << s.isInterleave("aabcc", "dbbca", "aadbbbaccc") << endl;
  cout << s.isInterleave("", "", "") << endl;
  cout << s.isInterleave("db", "b", "cbb") << endl;


  return 0;
};