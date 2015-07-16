class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if not tokens: return 0
        stack = []; i = 0
        while i < len(tokens):
              if tokens[i] != '*' and tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '/':
                 stack.append(int(tokens[i]))
              else:
                 first  = stack.pop()
                 second = stack.pop()
                 if tokens[i] == '*':
                    stack.append(second * first)
                 elif tokens[i] == '/':
                      stack.append(self.divide(first, second))
                 elif tokens[i] == '+':
                      stack.append(second + first)
                 elif tokens[i] == '-':
                      stack.append(second - first)
              i += 1
        return stack[0]

    def divide(self, divisor, dividend):
        if dividend * divisor < 0:
           return -(-dividend / divisor)
        else:
           return dividend / divisor


if __name__ == '__main__':
   s = Solution()
   # print s.evalRPN(["4", "13", "5", "/", "+"])
   # print s.evalRPN(["2", "1", "+", "3", "*"])
   # print s.evalRPN(['5', '1', '2', '+', '4', '*', '+', '3', '-'])
   print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
   # print s.evalRPN([])
   # print s.evalRPN(['18'])
        