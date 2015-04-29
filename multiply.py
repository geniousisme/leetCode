class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def builtInMultiply(self, num1, num2):
        return str(int(num1) * int(num2))

    def multiply(self, num1, num2):
        if num2 > num1:
           return self.multiply(num2, num1)
        