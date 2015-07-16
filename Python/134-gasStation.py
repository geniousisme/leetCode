class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    # Chris::TODO:need to know the detail better.
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas): return -1
        diff = start = 0
        for i in xrange(len(gas)):
            # diff = gas[i - 1] - cost[i - 1]
            if diff + gas[i] < cost[i]:
               start = i + 1
               diff = 0
            else:
               diff += gas[i] - cost[i]
        return start




