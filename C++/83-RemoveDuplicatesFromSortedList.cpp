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
    ListNode* deleteDuplicates(ListNode* head) {
              struct ListNode dummy(-9999);
              struct ListNode *tmp = &dummy;
              tmp->next = head;
              while (tmp->next) {
                     if (tmp->val == tmp->next->val) {
                         tmp->next = tmp->next->next;
                     } else {
                        tmp = tmp->next;
                     };
              };
              return head;
    }
    void printLinkedList(ListNode *head) {
         string llst = "";
         while (head) {
                cout << head->val;
                if (head->next) {
                    cout << " <- "; 
                };
                head = head->next;
         };
         cout << endl;   
    }
};

int main(void) {
    Solution s;
    struct ListNode test(1);
    struct ListNode t1(1);
    struct ListNode t2(2);
    struct ListNode t3(3);
    struct ListNode t4(3);
    (&test)->next = &t1;
    (&test)->next->next = &t2;
    (&test)->next->next->next = &t3;
    (&test)->next->next->next->next = &t4;
    s.printLinkedList(s.deleteDuplicates(&test));
    return 0;
};