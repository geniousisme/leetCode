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
    ListNode* removeNthFromEndI(ListNode* head, int n) {
        Utils u;
        int listLen = 0, flag;
        ListNode *dummy = head, *start;
        while(dummy != nullptr) {
            dummy = dummy->next;
            listLen++;
        };
        int count = 0;
        // cout << "listLen: " << listLen << endl;
        flag = listLen - n;
        ListNode tmp(-1);
        dummy       = &tmp;
        dummy->next = head;
        start       = dummy;
        while (count < flag && dummy->next != nullptr) {
            // cout << "here?" << endl;
            dummy = dummy->next;
            count++;
        };
        dummy->next = dummy->next->next;
        // u.printLinkedList(dummy->next);
        return start->next;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *slow, *fast, *dummy;
        dummy = new ListNode(0);
        dummy->next = head;
        head = dummy, slow = dummy, fast = dummy;
        /* make fast exceed slow n steps*/
        for (int i = 0; i <= n; i++) {
            fast = fast->next;
        };

        while (fast != nullptr) {
            fast = fast->next;
            slow = slow->next;
        };
        slow->next = slow->next->next;
        return head->next;
    }
};


int main(void) {
    Solution s;
    Utils u;
    ListNode l1(1);
    ListNode l2(2);
    ListNode l3(3);
    ListNode l4(4);
    ListNode l5(5);
    (&l1)->next = (&l2);
    (&l2)->next = (&l3);
    (&l3)->next = (&l4);
    (&l4)->next = (&l5);
    u.printLinkedList(&l1);
    // u.printLinkedList(s.removeNthFromEnd(&l1, 2));
    // u.printLinkedList(s.removeNthFromEnd(&l1, 3));
    // u.printLinkedList(s.removeNthFromEnd(&l1, 4));
    u.printLinkedList(s.removeNthFromEnd(&l1, 5));
    // u.printLinkedList(s.removeNthFromEnd(&l1, 1));



    return 0;
};