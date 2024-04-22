"""
   There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.

   For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #Here we need use topological sorting with indeegre = num of incoming vertices
        indegree = [0]*numCourses #num of incoming vertices for each edge
        graph = [list() for _ in range(numCourses)] #rudely representing as graph
        
        #Building of our graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        #Edges without incoming vertices
        queue = []
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        visited = 0
        while queue:
            edge = queue.pop()
            visited += 1
            for neighbour in graph[edge]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return visited == numCourses

"""
Time Complexity = Space Complexity = O(n+p)
"""
    
#Example of usage
solution = Solution()
print(solution.canFinish(2, [[1, 0]]))
     
"""
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, 
and to take course 0 you should also have finished course 1. So it is impossible.
"""        