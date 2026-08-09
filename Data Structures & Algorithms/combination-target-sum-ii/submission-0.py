class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,arr=[],[]
        candidates.sort()

        def backtrack(i):
            nonlocal arr
            nonlocal res
            if i==len(candidates):
                if sum(arr)==target and arr[:]not in res:
                    res.append(arr[:])
                return

            arr.append(candidates[i])
            backtrack(i+1)
            arr.pop()
            backtrack(i+1)
        backtrack(0)
        return res