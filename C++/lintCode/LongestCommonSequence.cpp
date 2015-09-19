#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * @param A, B: Two strings.
     * @return: The length of longest common subsequence of A and B.
     */
    int longestCommonSubsequence(string A, string B) {
        // write your code here
        int alen = A.length() + 1, blen = B.length() + 1, currMax = 0;
        vector<vector<int> > seqTable(alen, vector<int>(blen, 0));
        for (int i = 1; i < alen; i++) {
            for (int j = 1; j < blen; j++) {
                seqTable[i][j] = A[i - 1] == B[j - 1] ? seqTable[i - 1][j - 1] + 1 : max(seqTable[i - 1][j], seqTable[i][j - 1]);
                currMax = max(currMax, seqTable[i][j]);
            };
        };
        return currMax;
    }
};

int main(void) {
    Solution s;
    cout << s.longestCommonSubsequence("ABCD", "EDCA") << endl;
    cout << s.longestCommonSubsequence("ABCD", "EACB") << endl;
    return 0;
};

