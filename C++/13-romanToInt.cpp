#include "include/common.h"

class Solution {
public:
    int romanToInt(string s) {
        int res = 0;
        init();
        for (int i = 0; i < s.size(); i++) {
             if (romanTable[s[i + 1]] > romanTable[s[i]]) {
                 res -= romanTable[s[i]]; 
             } 
             else {
                 res += romanTable[s[i]];
             }
        };
        // res += romanTable[s[s.size() - 1]];
        return res;
    }
private:
    // really fast way to use initialize table.
    int romanTable[255];
    void init(void) {
         romanTable['I'] = 1, romanTable['V'] = 5, romanTable['X'] = 10;
         romanTable['L'] = 50, romanTable['C'] = 100, romanTable['D'] = 500;
         romanTable['M'] = 1000;
    };
    // unordered_map is slower.
    // unordered_map<char, int> romanTable =                                  \
    //           {                                                            \
    //            {'I', 1},  {'V', 5},   {'X', 10},                           \
    //            {'L', 50}, {'C', 100}, {'D', 500},                          \
    //            {'M', 1000}                                                 \
    //           };
};

int main(void) {
    Solution s;
    cout << s.romanToInt("XIV") << endl;
    cout << s.romanToInt("XVII") << endl;
    cout << s.romanToInt("LX") << endl;
    cout << s.romanToInt("CXCIX") << endl;
    cout << s.romanToInt("MMMCCCXXXIII") << endl;
    return 0;
};