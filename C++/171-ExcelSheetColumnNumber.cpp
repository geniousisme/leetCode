#include <iostream>
#include <string>
#include <math.h>

using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int end = s.size() - 1;
        int str_num, res = 0;
        for (int i = end; i > -1; i--) {
             str_num = s[i];
             res += (str_num - 64) * pow(26, end - i);
        };
        return res;
    }
};

int main(void){
    Solution s;
    cout << "A: " << s.titleToNumber("A") << endl;
    cout << "Z: " << s.titleToNumber("Z") << endl;
    cout << "AA: " << s.titleToNumber("AA") << endl;
    cout << "AB: " << s.titleToNumber("AB") << endl;
    cout << "BA: " << s.titleToNumber("BA") << endl;
    cout << "AJHX: " << s.titleToNumber("AJHX") << endl;
    return 0;
};