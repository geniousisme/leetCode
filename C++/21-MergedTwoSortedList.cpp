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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
              ListNode dummy(-1);
              ListNode *newStart = &dummy, *tmp, *tmplst;
              tmp = newStart;
              while (l1 && l2) {
                     if (l1->val < l2->val) {
                         tmplst = l1;
                         l1 = l1->next;
                         tmplst->next = nullptr;
                         tmp->next = tmplst;
                     }
                     else {
                         tmplst = l2;
                         l2 = l2->next;
                         tmplst->next = nullptr;
                         tmp->next = tmplst;
                     }  
                     tmp = tmp->next;
              };
              if (l1) {
                  tmp->next = l1;
              }
              if (l2) {
                  tmp->next = l2;
              }
              return newStart->next;
    }
};

int main(void) {
    ListNode t11(1), t12(4), t13(6), t14(10);
    ListNode t21(2), t22(3), t23(7), t24(13);
    Solution s;
    Utils utils;
    (&t11)->next = (&t12);
    (&t11)->next->next = (&t13);
    (&t11)->next->next->next = (&t14);
    (&t21)->next = (&t22);
    (&t21)->next->next = (&t23);
    (&t21)->next->next->next = (&t24);
    utils.printLinkedList(s.mergeTwoLists(&t11, &t21));
    return 0;
};