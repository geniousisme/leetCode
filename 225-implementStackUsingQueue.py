class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        self.queue.pop()
        

    # @return an integer
    def top(self):
        return self.queue[-1]
        

    # @return an boolean
    def empty(self):
        return not self.queue
        