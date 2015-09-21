#include "include/common.h"
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        Utils u;
        ListNode *dummy = new ListNode(-1), *larger = new ListNode(0), *largeStart;
        dummy->next = head;
        head        = dummy; // notice here!, dont use dummy->next
        largeStart  = larger;  // notice here!, dont use larger->next
        while (dummy->next != nullptr) {
            if (dummy->next->val < x) {
                dummy = dummy->next;
            } else {
                ListNode *next = dummy->next->next;
                dummy->next->next = nullptr;
                larger->next = dummy->next;
                dummy->next = next;
                larger = larger->next;
            };
        };
        dummy->next = largeStart->next;
        return head->next;
    }
};

int main(void) {
    Solution s;
    Utils u;
    ListNode l1(1);
    ListNode l2(4);
    ListNode l3(3);
    ListNode l4(2);
    ListNode l5(5);
    ListNode l6(2);
    (&l1)->next = (&l2);
    (&l2)->next = (&l3);
    (&l3)->next = (&l4);
    (&l4)->next = (&l5);
    (&l5)->next = (&l6);
    u.printLinkedList(s.partition(&l1, 3));
    return 0;
}