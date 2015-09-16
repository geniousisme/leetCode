#include "include/common.h"

class Solution {
public:
    int minDistance(string word1, string word2) {
        int length1 = word1.length() + 1, length2 = word2.length() + 1, one;
        vector<vector<int> > editCounts(length1, vector<int>(length2, 0));
        for (int i = 0; i < length1; i++) {
             editCounts[i][0] = i;
        };
        for (int j = 0; j < length2; j++) {
             editCounts[0][j] = j;
        };
        for (int i = 1; i < length1; i++) {
            for (int j = 1; j < length2; j++) {  
                one = word1[i - 1] != word2[j - 1];
                editCounts[i][j] = min(editCounts[i - 1][j - 1] + one, min(editCounts[i - 1][j] + 1, editCounts[i][j - 1] + 1));
            };
        };
        return editCounts[length1 - 1][length2 - 1];      
    }
};

int main(void) {
    Solution s;
    cout << s.minDistance("mart", "karma") << endl;
    return 0;
};