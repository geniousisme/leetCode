#ifndef UTILS_H
#define UTILS_H

#include "library.h"

class Utils { 
public: 
    Utils();
    ~Utils();
    void printLinkedList(ListNode* head); 
    void printIntVector(vector<int>&);
    void printStrVector(vector<string>&);
    void printTree(TreeNode*); 
};

#endif 
