#include "include/common.h"
// Chris:NTR
class Solution {
public:
    vector<string> generateParenthesis(int n) {
                   vector<string> res;
                   if (n > 0) {
                       dfsParenthesis(res, "", n, n);
                   };
                   return res;
    }
private:
    void dfsParenthesis(vector<string>& res, string parethese, int left, int right) {
         if (left > right) {
             return;
         };
         if (left == 0 && right == 0) {
             res.push_back(parethese);
         };
         if (left > 0) {
             dfsParenthesis(res, parethese + "(", left - 1, right);
         };
         if (right > 0) {
             dfsParenthesis(res, parethese + ")", left, right - 1);
         };
    }
};

int main(void) {
    Solution s;
    Utils utils;
    utils.printStrVector(s.generateParenthesis(3));
    return 0;
};