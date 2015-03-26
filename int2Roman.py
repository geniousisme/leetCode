class Solution:
    # @return a string
    # Symbol  Value
    # I       1
    # V       5
    # X       10
    # L       50
    # C       100
    # D       500
    # M       1,000
    
    def intToRoman(self, num):
        M_count = num / 1000
        D_count = num % 1000 / 500
        C_count = num % 1000 % 500 / 100
        L_count = num % 1000 % 500 % 100 / 50
        X_count = num % 1000 % 500 % 100 % 50 / 10
        V_count = num % 1000 % 500 % 100 % 50 % 10 / 5
        I_count = num % 1000 % 500 % 100 % 50 % 10 % 5
