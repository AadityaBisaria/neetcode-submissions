class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def backtrack(i,cur,total):
            if total==target and cur not in res:
                res.append(cur.copy())
                return

            
            for j in range(i+1,len(candidates)):
                if total+candidates[j]>target:
                    return
                cur.append(candidates[j])
                backtrack(j,cur,total+candidates[j])
                cur.pop()
        backtrack(-1,[],0)
        return res