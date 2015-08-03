#include "include/common.h"

class Queue {
public:
    // Push element x to the back of queue.
    void push(int x) {
         stk.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
         while (!stk.empty()) {
                tmpV.push_back(stk.top());
                stk.pop();
         };
         tmpV.pop_back();
         for (int i = tmpV.size() - 1; i > -1; i--) {
              stk.push(tmpV[i]);
              tmpV.pop_back();
         };
    }

    // Get the front element.
    int peek(void) {
        while (!stk.empty()) {
               tmpV.push_back(stk.top());
               stk.pop();
        };
        int top = tmpV.back();
        for (int i = tmpV.size() - 1; i > -1; i--) {
             stk.push(tmpV[i]);
        };
        tmpV.clear();
        return top;
    }
    // Return whether the queue is empty.
    bool empty(void) {
         return stk.empty();  
    }
private:
    stack<int> stk;
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