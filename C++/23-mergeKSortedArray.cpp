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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, compareNode> heapq;
        for (int i = 0; i < lists.size(); i++) {
            if (lists[i]) {
                heapq.push(lists[i]);
            };
        };
        ListNode *dummy = new ListNode(0), *start = dummy, *min_node;
        while (!heapq.empty()) {
            min_node = heapq.top();
            dummy->next = min_node;
            heapq.pop();
            dummy = dummy->next;
            if (min_node->next) {
                heapq.push(min_node->next);
            };
        };
        return start->next;
    }
private:
    struct compareNode {
        bool operator()(ListNode *left, ListNode *right) {
            return left->val > right->val;
        }
    };
};

int main(void) {
    Solution s;
    Utils u;
    ListNode *l1 = new ListNode(2);
    ListNode *l11 = new ListNode(4);
    l1->next = l11;
    ListNode *l2 = new ListNode(3);
    ListNode *l21 = new ListNode(5);
    ListNode *l22 = new ListNode(9);
    l2->next = l21;
    l21->next = l22;
    ListNode *l3 = new ListNode(-1);
    vector<ListNode*> lists;
    lists.push_back(l1);
    lists.push_back(l2);
    lists.push_back(l3);
    u.printLinkedList(s.mergeKLists(lists));
    return 0;
};