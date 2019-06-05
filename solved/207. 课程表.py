"""同210一致，只是返回不同"""
class Solution:
    def canFinish(self, numCourses, prerequisites):
        edges = {}
        degree = {}
        for edge in prerequisites:
            if edge[1] not in edges:
                edges[edge[1]] = set()
            edges[edge[1]].add(edge[0])
            if edge[0] not in degree:
                degree[edge[0]] = 0
            degree[edge[0]] += 1

        ret = []
        queue = [i for i in range(numCourses) if i not in degree]
        while queue:
            course = queue.pop(0)
            ret.append(course)
            if course in edges:
                for nextCourse in edges[course]:
                    degree[nextCourse] -= 1
                    if degree[nextCourse] == 0:
                        queue.append(nextCourse)

        return True if len(ret) == numCourses else False

