#include "include/common.h"

class Solution {
public:
    int minCutI(string s) {
        if (s.length() == 0 || s == "") {
          return 0;
        };
        vector<int> cutCount;
        // init
        for (int i = 0; i < s.length() + 1; i++) {
          cutCount.push_back(i - 1);
        };
        palindromeTable = getIsPalindrome(s);
        // get min cut
        for (int i = 1; i < s.length() + 1; i++) {
          for (int j = 0; j < i; j++) {
            if (palindromeTable[j][i - 1]) { // see if s[j:i] is palindrome or not
              cutCount[i] = min(cutCount[i], cutCount[j] + 1);
            };
          };
        };
        return cutCount[s.length()];
    }
    int minCut(string s) {
        if (s.length() == 0 || s == "") {
          return 0;
        };
        vector<int> cutCount;
        for (int i = 0; i < s.length() + 1; i++) {
          cutCount.push_back(i - 1);
        };

        // init
        vector<vector<bool> > isPalindromeTable(s.length(), vector<bool>(s.length(), false));
        for (int i = 0; i < s.length(); i++) {
          isPalindromeTable[i][i] = true;
        };
        for (int i = 1; i < s.length() + 1; i++) {
          for (int j = 0; j < i; j++) {
            if (s[j] == s[i] && (i - j < 2 || isPalindromeTable[j + 1][i - 1])) {
              isPalindromeTable[j][i] = true;
              cutCount[i] = min(cutCount[i], cutCount[j] + 1);
            };
          };
        };
        return cutCount[s.length()];
    }
private:
    vector<vector<bool> > palindromeTable;
    
    // judge id it is a palindrome or not.
    bool isPalindrome (string s, int start, int end) {
         for (int i = start, j = end; i < j; i++, j--) {
              if (s[i] != s[j]) {
                  return false;
              };
         };
         return true;
    }

    vector<vector<bool> > getIsPalindrome(string s) {
      vector<vector<bool> > isPalindromeTable(s.length(), vector<bool>(s.length(), false));
      // for length = 1, must be palindrome
      int length = s.length();
      for (int i = 0; i < length; i++) {
        isPalindromeTable[i][i] = true;
      };
      // for length = 2, check if they are same in the neighbor
      for (int i = 0; i < length - 1; i++) {
        isPalindromeTable[i][i + 1] = s[i] == s[i + 1];
      };
      // for length > 2, Dynamic Programming
      for (int range = 2; range < length; range++) {
        for (int start = 0; start + range < length; start++) {
          isPalindromeTable[start][start + range] =                            
                            isPalindromeTable[start + 1][start + range - 1] && 
                            s[start] == s[start + range];
        };    
      };
      return isPalindromeTable;
    }
};

int main(void) {
  Solution s;
  string test = "aab";
  cout << s.minCut(test) << endl;

  string test1 = "aacbb";
  cout << s.minCut(test1) << endl;

  string test2 = "aba";
  cout << s.minCut(test2) << endl;

  
  return 0;
};