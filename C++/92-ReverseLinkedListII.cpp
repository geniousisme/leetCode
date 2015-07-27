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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
              int count = 0;
              struct ListNode start(-1);
              struct ListNode *newHead = &start;
              newHead->next = head;
              while (newHead->next) {
                     count++;
                     if (count == m) {
                         newHead->next = reverseList(newHead->next, count, n);
                         break;
                     }
                     else {
                        newHead = newHead->next;
                     }
              };
              return (&start)->next;
    }
    ListNode* reverseList(ListNode* head, int& count, int n) {
              struct ListNode *newHead = nullptr, *headNext, *newEnd = head;
              while (count < n + 1 && head) {
                     count++;
                     headNext   = head->next;
                     head->next = newHead;
                     newHead    = head;
                     head       = headNext;
              };
              newEnd->next = headNext;
              // tmpHead = newHead;
              // if (headNext) {
              //     while (tmpHead->next) {
              //            tmpHead = tmpHead->next;
              //     };
              //     tmpHead->next = headNext; 
              // };
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
    s.printLinkedList(s.reverseBetween(&test, 1, 4));
    return 0;
};