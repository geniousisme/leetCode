# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval.start)
        last = len(intervals) - 1
        start = 1
        while start <= last:
            if intervals[start - 1].end >= intervals[start].start:
               intervals[start].start = intervals[start - 1].start
               if intervals[start - 1].end >= intervals[start].end:
                  intervals[start].end = intervals[start - 1].end
               del intervals[start - 1]
               last -= 1
            else:
               start += 1
        return intervals

    def print_intervals(self, intervals):
        interval_str = ""
        for interval in intervals:
            interval_str += '(' + str(interval.start) + ' ' + str(interval.end) + ') '
        print interval_str



if __name__ == '__main__':
   s = Solution()
   intervals = [Interval(1, 4), Interval(1, 4)]
   s.print_intervals(s.merge(intervals))
   intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
   s.print_intervals(s.merge(intervals))


 


    
