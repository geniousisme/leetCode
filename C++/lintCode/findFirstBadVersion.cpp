#include "../include/common.h"

/**
 * class VersionControl {
 *     public:
 *     static bool isBadVersion(int k);
 * }
 * you can use VersionControl::isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/

class VersionControl {
public:
      static bool isBadVersion(int k) {
                  bool versions [] = {false, false, true, true};
                  // bool versions [] = {false};
                  return versions[k - 1];
      }
};

class Solution {
public:
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    int findFirstBadVersion(int n) {
        int start = 1, end = n, mid;
        VersionControl v;
        while(start < end) {
              mid = (end + start) / 2;
              if (v.isBadVersion(mid) == true) {
                  end = mid;
              }
              else { // mid = false && mid = false
                  start = mid + 1;
              }
        };
        // cout << "start: " << start << " is it? " << v.isBadVersion(start) << endl;
        if (v.isBadVersion(start)) {
            return start;
        }
        else {
            return end;
        };
    }
};

int main(void) {
    Solution s;
    cout << s.findFirstBadVersion(4) << endl;
    return 0;
};