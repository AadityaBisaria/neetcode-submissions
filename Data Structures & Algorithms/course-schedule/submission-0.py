class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        visited=set()

        for crc, prereq in prerequisites:
            premap[crc].append(prereq)

        def dfs(crc):
            if crc in visited:
                return False
            if premap[crc]==[]:
                return True
            
            visited.add(crc)
            for pre in premap[crc]:
                if not dfs(pre):
                    return False
            visited.remove(crc)
            premap[crc]=[]
            return True
        
        for crc in range(numCourses):
            if not dfs(crc):
                return False
            
        return True