# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        length = len(intervals)
        intervals.append(newInterval)
        # for i in xrange(length):
        #     if intervals[i].start >= newInterval.start:
        #        intervals.insert(i, newInterval)
        #        newInterval = None
        #        break
        # if newInterval:
        #    intervals.append(newInterval)
        # self.print_intervals(intervals)
        intervals.sort(key=lambda start : start.start)

        last = length
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
   intervals = [Interval(1, 3), Interval(6, 9)]
   s.print_intervals(s.insert(intervals, Interval(7, 10)))
   intervals = [Interval(1, 5)]
   s.print_intervals(s.insert(intervals, Interval(0, 3)))
   intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
   s.print_intervals(s.insert(intervals, Interval(4, 9)))


 


    
