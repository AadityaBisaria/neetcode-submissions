class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtracking(i, combination):
            if i == len(nums):
                res.append(list(combination))
                return

            combination.append(nums[i])
            backtracking(i + 1, combination)
            
            combination.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1                  
            backtracking(i + 1, combination)
        
        backtracking(0, [])
        return res