#ifndef UTILS_H
#define UTILS_H

#include "library.h"

class Utils { 
public: 
    Utils();
    ~Utils();
    void printLinkedList(ListNode*); 
    void printIntVector(vector<int>);
    void print2DIntVector(vector<vector<int> >);
    void printStrVector(vector<string>);
    void printTree(TreeNode*); 
};

#endif 
