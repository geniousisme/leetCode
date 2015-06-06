# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def __init__(self):
        self.slope_hash = {'inf': 0}
    
    def maxPoints(self, points):
        length = len(points)
        if length < 3:
           return length
        res = -999999
        for i in xrange(length):
            samePointNum = 1
            slope_hash = {'inf' : 0}
            for j in xrange(i + 1, length):
                if points[i].x == points[j].x and points[i].y != points[j].y:
                   slope_hash['inf'] += 1
                elif points[i].x != points[j].x:
                     slope = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                     # self.addToHashTable(slope, slope_hash)
                     slope_hash[slope] = slope_hash.get(slope, 0) + 1
                else:
                     samePointNum += 1
            res = max(res, max(slope_hash.values()) + samePointNum)
        return res

    # def addToHashTable(self, slope, slope_hash):
    #     try:
    #         slope_hash[slope] += 1
    #     except:
    #         slope_hash.setdefault(slope, 1)

if __name__ == '__main__':
   s = Solution()
   points = [Point(1, 2), Point(2, 4), Point(3, 6), Point(3, 8), Point(4, 8), Point(5, 2)]
   print s.maxPoints(points)







