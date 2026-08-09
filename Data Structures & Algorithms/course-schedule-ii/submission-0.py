class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}
        visit,cycle=set(),set()
        res=[]

        for crc, prereq in prerequisites:
            premap[crc].append(prereq)

        def dfs(crc):
            if crc in cycle:
                return False
            if crc in visit:
                return True
            
            cycle.add(crc)
            for pre in premap[crc]:
                if dfs(pre)==False:
                    return False
            cycle.remove(crc)
            visit.add(crc)
            res.append(crc)
            return True
        
        for crc in range(numCourses):
            if dfs(crc)==False:
                return []                     
        return res
        