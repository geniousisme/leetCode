#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string convertToTitle(int n) {
           string title = "";
           char letter = '\0';
           while (n > 0) {
                  // key skill: move all num left by 1 unit and use plussing 65 
                  // to achieve the original result.
                  letter = 65 + (n - 1) % 26; 
                  title = letter + title; // notice the order of new char to put/
                  n = (n - 1) / 26;
           };
           return title;
    }
};

int main(void){
    Solution s;
    cout << "1: " << s.convertToTitle(1) << endl;
    cout << "26: " << s.convertToTitle(26) << endl;
    cout << "27: " << s.convertToTitle(27) << endl;
    cout << "28: " << s.convertToTitle(28) << endl;
    cout << "53: " << s.convertToTitle(53) << endl;
    cout << "24568: " << s.convertToTitle(24568) << endl;
    return 0;
};