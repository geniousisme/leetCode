#include <iostream>

using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
             ListNode *fast = head, *slow = head;
             bool met = false;
             while (slow && fast && fast->next) {
                    if (!met) {
                        slow = slow->next;
                        fast = fast->next->next;
                        if (slow == fast) {
                            met  = true;
                            slow = head;
                        };
                    } else {
                        while (slow != fast) {
                               slow = slow->next;
                               fast = fast->next;
                        };
                        return slow;
                    };
             };
             return nullptr;
    }
};
int main(void) {

    return 0;
};