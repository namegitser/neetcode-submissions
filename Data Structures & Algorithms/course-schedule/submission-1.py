class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited: #cycle
                return False
            
            if graph[course] == []: #no_prerequisite
                return True
            
            visited.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(course)
            graph[course] = [] #gone through this course, remove all pre

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
            