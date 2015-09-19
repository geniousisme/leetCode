#include "include/common.h"

class Solution {
public:
    int numDistinct(string s, string t) {
      // Utils u;
      int tlen = t.length() + 1, slen = s.length() + 1;
      if (tlen == 1) {
        return 0;
      };
      vector<vector<int> > stTable(slen, vector<int>(tlen, 0));
      for (int i = 0; i < slen; i++) {
        stTable[i][0] = 1;
      };
      for (int j = 1; j < tlen; j++) {
        stTable[0][j] = 0;
      };
      for (int i = 1; i < slen; i++) {
        for (int j = 1; j < tlen; j++) {
          stTable[i][j] = stTable[i - 1][j] + (s[i - 1] == t[j - 1]) * stTable[i - 1][j - 1];
        };
      };
      // u.print2DIntVector(stTable);
      return stTable[slen - 1][tlen - 1];
    }
};

int main(void) {
  Solution s;
  cout << s.numDistinct("rabbbit", "rabit") << endl;
  return 0;
};