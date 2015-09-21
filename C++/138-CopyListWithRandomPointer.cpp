#include "include/common.h"
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        RandomListNode *dummy = head, *nxt, *duplicate, *start = new RandomListNode(0);
        // duplcate each node twice first.
        while(dummy) {
            duplicate = new RandomListNode(dummy->label);
            nxt = dummy->next;
            dummy->next = duplicate;
            duplicate->next = nxt;
            dummy = nxt;
        };
        // cuplicate ramdom ptr for each node.
        dummy = head;
        while (dummy && dummy->next) {
            if (dummy->next && dummy->random)
                dummy->next->random = dummy->random->next;
            dummy = dummy->next->next;
        };
        // seperate duplicate nodes
        dummy = head;
        head  = start;
        while (dummy) {
            start->next = dummy->next;
            dummy->next = dummy->next->next;
            dummy = dummy->next;
            start = start->next;
        };
        return head->next;
    }
};

int main(void) {
    Solution s;
    Utils u;
    RandomListNode *l1 = new RandomListNode(1);
    RandomListNode *l2 = new RandomListNode(2);
    RandomListNode *l3 = new RandomListNode(3);
    l1->next = l2;
    l2->next = l3;
    u.printRandomList(s.copyRandomList(l1));
    return 0;
};