class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.table = {}

    # @return nothing
    def add(self, number):
        self.table[number] = self.table.get(number, 0) + 1

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for num in self.table:
            diff = value - num
            self.table.get(diff)
            if (num == diff and self.table.get(diff, 0) > 1) or (num != diff and self.table.get(diff, 0) >= 1):
               return True
        return False


if __name__ == '__main__':
   s = TwoSum()
   s.add(1)
   s.add(3)
   s.add(5)
   print s.find(4)
   print s.find(7)
   print s.find(5)
   print s.find(8)
   s.add(0)
   print s.find(0)
   s.add(0)
   print s.find(0)

        