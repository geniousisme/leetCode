class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        numIdxDict = {} # num value to index diction
        for idx, n in enumerate(num):
            if target - n in numIdxDict:
                return (numIdxDict[target - n] + 1, idx + 1)
            numIdxDict[n] = idx
            