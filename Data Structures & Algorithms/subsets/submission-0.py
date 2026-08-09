class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack=[]
        res=[]
        def backtracking(i:int):
            if(i>=len(nums)):
                res.append(stack.copy())
                return

            stack.append(nums[i])
            backtracking(i+1)
            stack.pop()
            backtracking(i+1)

        backtracking(0)
        return res