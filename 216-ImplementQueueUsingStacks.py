class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        self.stack.reverse()
        self.stack.pop()
        self.stack.reverse()

    # @return an integer
    def peek(self):
        return self.stack[0]
        

    # @return an boolean
    def empty(self):
        return self.stack == []
        