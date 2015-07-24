#include "Utils.h"

Utils::Utils() {
}

void Utils::printLinkedList(ListNode* head) {
     while (head) {
            cout << head->val;
            if (head->next) {
                cout << " <- "; 
            };
            head = head->next;
     };
     cout << endl;
}