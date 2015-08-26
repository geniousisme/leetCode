#include "Utils.h"

// Chris::TODO:make this shit work!!

Utils::Utils() {
}

Utils::~Utils() {
}


void Utils::printLinkedList(ListNode* head) {
     while (head) {
            cout << head->val;
            if (head->next) {
                cout << " -> "; 
            };
            head = head->next;
     };
     cout << endl;
}

void Utils::printIntVector(vector<int> nums) {
     for(int i = 0; i < nums.size(); i++) cout << nums[i] << " ";
     cout << endl;
}

void Utils::printStrVector(vector<string> strs) {
     for(int i = 0; i < strs.size(); i++) cout << strs[i] << " ";
     cout << endl;
}