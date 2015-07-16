class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        degrees  = [0 for i in xrange(numCourses)]
        children = [[] for i in xrange(numCourses)]
        for pre in prerequisites:
            degrees[pre[0]] += 1
            children[pre[1]].append(pre[0])
        courses  = range(numCourses)

        cycle_flag = True
        while cycle_flag and courses != []:
              cycle_flag = False
              removelist = []
              for course in courses:
                  if degrees[course] == 0:
                     for child in children[course]:
                         degrees[child] -= 1
                     removelist.append(course)
                     cycle_flag = True
              for course in removelist:
                  print course
                  courses.remove(course)
        return courses == []


if __name__ == '__main__':
   s = Solution()
   print s.canFinish(2, [[1, 0]])
   print s.canFinish(2, [[0, 1]])
   print s.canFinish(2, [[1, 0], [0, 1]])
   

