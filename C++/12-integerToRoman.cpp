#include "include/common.h"

class Solution {
public:
    string intToRomanI(int num) {
           init();
           string res = "";
           while (num > 0) {
                  if (num >= 1000) {
                      num -= 1000;
                      res += intTable[1000];
                  }
                  else if (num < 1000 && num >= 100) {
                           if (num >= 500) {
                               if (num >= 900) {
                                   num -= 900;
                                   res += intTable[900];
                               }
                               else { // num < 900
                                   num -= 500;
                                   res += intTable[500];
                               };
                           }
                           else { // num < 500
                              if (num >= 400) {
                                  num -= 400;
                                  res += intTable[400];
                              }
                              else { // num < 400
                                  num -= 100;
                                  res += intTable[100];
                              }
                           };
                  }
                  else if (num < 100 && num >= 10) {
                           if (num >= 50) {
                               if (num >= 90) {
                                   num -= 90;
                                   res += intTable[90]; 
                               } 
                               else { // num < 90
                                   num -= 50;
                                   res += intTable[50]; 
                               };
                           }
                           else { // num < 50
                               if (num >= 40) {
                                   num -= 40;
                                   res += intTable[40];
                               }  // num < 40
                               else {
                                   num -= 10;
                                   res += intTable[10];
                               }
                           };
                  }
                  else {
                      if (num >= 5) {
                          if (num >= 9) {
                              num -= 9;
                              res += intTable[9];
                          }
                          else {
                              num -=  5;
                              res += intTable[5];
                          };
                      }
                      else {
                          if (num >= 4) {
                              num -= 4;
                              res += intTable[4];
                          }
                          else {
                              num -= 1;
                              res += intTable[1];
                          };
                      };
                  };
           };
           return res;
    }
    string intToRoman(int num) {
           string romanLst [] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
           int intLst [] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
           string res = "";
           for (int i = 0; i < 13; i++) {
                while (num >= intLst[i]) {
                       num -= intLst[i];
                       res += romanLst[i];
                };
           };
           return res;
    }
private:
    string intTable[1001];
    void init(void) {
         intTable[1] = "I", intTable[4] = "IV", intTable[5] = "V";
         intTable[9] = "IX", intTable[10] = "X", intTable[40] = "XL";
         intTable[50] = "L", intTable[90] = "XC", intTable[100] = "C";
         intTable[400] = "CD", intTable[500] = "D", intTable[900] = "CM";
         intTable[1000] = "M";
    }
};

int main(void) {
    Solution s;
    cout << "1000: " << s.intToRoman(1000) << endl;
    cout << "14: " << s.intToRoman(14) << endl;
    cout << "17: " << s.intToRoman(17) << endl;
    cout << "60: " << s.intToRoman(60) << endl;
    cout << "199: " << s.intToRoman(199) << endl;
    cout << "3333: " << s.intToRoman(3333) << endl;
    return 0;
};