class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adj[a].append(b)
        visit,cycle=set(),set()
        output=[]
        def solution(coursea):
            
            if coursea in cycle:
                return False

            if coursea in visit:
                return True

            cycle.add(coursea)
            for course in adj[coursea]:
                
                if  not solution(course):
                    return False

            cycle.remove(coursea)
            visit.add(coursea)
            output.append(coursea)
            return True
        
        for c in range(numCourses):
            if solution(c)==False:
                return []
        
        return output