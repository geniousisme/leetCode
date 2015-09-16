#include "include/common.h"

class Solution {
public:
    int minimumTotal(vector<vector<int> >& triangle) {
        int height = triangle.size();
        for (int i = height - 2; i > -1; i--) {
             for (int j = 0; j < triangle[i].size(); j++) {
                  // triangle[i][j] += triangle[i + 1][j] < triangle[i + 1][j + 1] ? triangle[i + 1][j] : triangle[i + 1][j + 1];
                 triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
             };
        };
        return triangle[0][0];
    }
};