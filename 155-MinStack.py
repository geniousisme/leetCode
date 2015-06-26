class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.hash = {'min_stack':[], 'stack':[]}
    
    def push(self, x):
        self.hash['stack'].append(x)
        if self.hash['min_stack']:
           if x <= self.hash['min_stack'][-1]:
              self.hash['min_stack'].append(x)
        else:
           self.hash['min_stack'].append(x)

    # @return nothing
    def pop(self):
        top = self.hash['stack'].pop()
        if top == self.hash['min_stack'][-1]:
           self.hash['min_stack'].pop()
        
    # @return an integer
    def top(self):
        return self.hash['stack'][-1]
        

    # @return an integer
    def getMin(self):
        return self.hash['min_stack'][-1]

if __name__ == '__main__':
   m = MinStack()
   m.push(2)
   m.push(0)
   m.push(3)
   m.push(0)
   print m.hash
   print m.getMin()
   m.pop()
   print m.getMin()
   m.pop()
   print m.getMin()
   m.pop()
   print m.getMin()
   