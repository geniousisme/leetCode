#include "../include/common.h"

class Solution {
public:    
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    int longestCommonSubstring(string A, string B) {
        // write your code here
        Utils u;
        int alen = A.length() + 1, blen = B.length() + 1, maxleng = 0;
        vector<vector<int> > lengthTable(alen, vector<int>(blen, 0));

        for (int i = 1; i < alen; i++) {
            for (int j = 1; j < blen; j++) {
                lengthTable[i][j] = A[i - 1] == B[j - 1] ? lengthTable[i - 1][j - 1] + 1 : 0;
                maxleng = max(maxleng, lengthTable[i][j]);
            };
        };
        // u.print2DIntVector(lengthTable);
        return maxleng;
    }
};

int main(void) {
    Solution s;
    // cout << s.longestCommonSubstring("ABCD", "CBCE") << endl;
    // cout << s.longestCommonSubstring("ABCD", "BBBB") << endl;
    cout << s.longestCommonSubstring("www.lintcode.com code", "www.ninechapter.com code") << endl;

    return 0;
};
