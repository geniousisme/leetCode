class Stack {
public:
    // Push element x onto stack.
    void push(int x) {
         myQueue.push(x);
    }
    // Removes the element on top of the stack.
    void pop() {
         while (!myQueue.empty()) {
                tmpV.push_back(myQueue.front());
                myQueue.pop();
         };
         tmpV.pop_back();
         for (int i = 0; i < tmpV.size(); i++) {
              myQueue.push(tmpV[i]);
         };
         tmpV.clear();
    }
    // Get the top element.
    int top() {
        while (!myQueue.empty()) {
                tmpV.push_back(myQueue.front());
                myQueue.pop();
         };
         int top = tmpV.back();
         for (int i = 0; i < tmpV.size(); i++) {
              myQueue.push(tmpV[i]);
         };
         tmpV.clear();
        return top;
    }
    // Return whether the stack is empty.
    bool empty() {
         return myQueue.empty();        
    }
private:
    queue<int> myQueue;
    vector<int> tmpV;
};