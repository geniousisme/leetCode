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
    ListNode* reverseList(ListNode* head) {
              ListNode *newHead = nullptr, *headNext;
              while (head) {
                     headNext   = head->next;
                     head->next = newHead;
                     newHead    = head;
                     head       = headNext;
              };
              return newHead;
        
    }
    void printLinkedList(ListNode *head) {
         string llst = "";
         while (head) {
                cout << head->val;
                if (head->next) {
                    cout << " -> "; 
                };
                head = head->next;
         };
         cout << endl;   
    }
};

int main(void) {
    Solution s;
    struct ListNode test(1);
    struct ListNode t1(2);
    struct ListNode t2(3);
    struct ListNode t3(4);
    struct ListNode t4(5);
    (&test)->next = &t1;
    (&test)->next->next = &t2;
    (&test)->next->next->next = &t3;
    (&test)->next->next->next->next = &t4;
    s.printLinkedList(s.reverseList(&test));
    return 0;
};