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
    void reorderList(ListNode* head) {
         if (head == nullptr) {
            return;
         };
         ListNode *slow = head, *fast = head;
         ListNode *right, *left, *start, *nxt;
         // get the middle
         while(fast->next && fast->next->next) {
            fast = fast->next->next;
            slow = slow->next;
         };
         right      = slow->next;
         slow->next = nullptr;
         left       = head;
         //reverse right part
         start      = nullptr;
         while (right) {
            nxt         = right->next;
            right->next = start; // key steps!!
            start       = right;
            right       = nxt;
         };
         right = start; // key steps!!
         
         // merge two list together
         ListNode *new_head = new ListNode(0);
         ListNode *new_dummy = new_head;
         while (left) {
            new_dummy->next = left;
            left = left->next;
            new_dummy = new_dummy->next;
            if (right) {
                new_dummy->next = right;
                right = right->next;
                new_dummy = new_dummy->next;
            };
         };
         head = new_head->next;
    }
};

int main(void) {
    Solution s;
    Utils u;
    ListNode l1(1);
    ListNode l2(2);
    ListNode l3(3);
    ListNode l4(4);
    (&l1)->next = &l2;
    (&l2)->next = &l3;
    (&l3)->next = &l4;
    s.reorderList(&l1);
    u.printLinkedList(&l1);
    return 0;
};