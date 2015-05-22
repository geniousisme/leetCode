class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.hash = {'min_stack':[], 'stack':[]}
    
    def push(self, x):
        self.hash['stack'].append(x)
        if x < self.hash['min']:
           self.hash['min'] = x

    # @return nothing
    def pop(self):
        self.hash['stack'].pop()
        if self.hash['stack']:
           self.hash['min'] = min(self.hash['stack'])
        else:
           self.hash['min'] = float('inf')
    # @return an integer
    def top(self):
        return self.hash['stack'][-1]
        

    # @return an integer
    def getMin(self):
        return self.hash['min']

if __name__ == '__main__':
   m = MinStack()
   m.push(2)
   m.push(0)
   m.push(3)
   m.push(0)
   print m.getMin()
   m.pop()
   print m.getMin()
   m.pop()
   print m.getMin()
   m.pop()
   print m.getMin()
   