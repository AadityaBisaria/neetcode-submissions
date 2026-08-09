class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def backtrack(total,arr,idx):
            if total==target:
                res.append(arr.copy())
                return
            
            if idx==len(candidates) or total>target:
                return
            
        
            arr.append(candidates[idx])
            backtrack(total+candidates[idx],arr,idx+1)
            arr.pop()
            while idx+1<len(candidates) and candidates[idx]==candidates[idx+1]:
                idx+=1
            backtrack(total,arr,idx+1)
        backtrack(0,[],0)
        return res
