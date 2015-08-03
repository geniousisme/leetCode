#include "include/common.h"

class Queue {
public:
    // Push element x to the back of queue.
    void push(int x) {
         myStack.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
         while (!myStack.empty()) {
                tmpV.push_back(myStack.top());
                myStack.pop();
         };
         tmpV.pop_back();
         for (int i = tmpV.size() - 1; i > -1; i--) {
              myStack.push(tmpV[i]);
              tmpV.pop_back();
         };
    }

    // Get the front element.
    int peek(void) {
        while (!myStack.empty()) {
               tmpV.push_back(myStack.top());
               myStack.pop();
        };
        int peek = tmpV.back();
        for (int i = tmpV.size() - 1; i > -1; i--) {
             myStack.push(tmpV[i]);
        };
        tmpV.clear();
        return peek;
    }
    // Return whether the queue is empty.
    bool empty(void) {
         return myStack.empty();  
    }
private:
    stack<int> myStack;
    vector<int> tmpV;
};

int main(void) {
    Queue q;
    for (int i = 0; i < 10; i++)    q.push(i);
    q.pop();
    cout << "top: " << q.peek() << endl;
    cout << "empty: " << q.empty() << endl;
    return 0;
};