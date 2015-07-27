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
    bool isPalindrome(ListNode* head) {
         if (head == nullptr) {
             return true;
         };

         // look for the mid point
         struct ListNode *slow = head, *fast = head; 
         while (fast->next && fast->next->next) {
                slow = slow->next;
                fast = fast->next->next;
         };
         
         // reverse the second half linked list 
         struct ListNode *last = nullptr, *tmp = slow->next, *tmpNext;
         while (tmp) {
                tmpNext   = tmp->next;
                tmp->next = last;
                last      = tmp;
                tmp       = tmpNext;
         };

         // then, test if second half llst match all value of the first half llst value.
         // if it meets all then it will ends at null, so check if ptr == null, it is palindrom
         // if it doesn't meet, then it will break and it will not equal to null, return false
         struct ListNode *p1 = last, *p2 = head;
         while (p1 && p1->val == p2->val) {
                p1 = p1->next;
                p2 = p2->next;
         };
         return p1 == nullptr;
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
    // s.isPalindrome(&test);
    cout << s.isPalindrome(&test) << endl;
    return 0;
};