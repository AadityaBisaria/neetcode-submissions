class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
               
        def backtrack(summation,combination,start):
            if(summation==target):
                res.append(list(combination))
            elif(summation<target):
                for i in range(start,len(nums)):
                    combination.append(nums[i])
                    backtrack(summation+nums[i],combination,i)
                    combination.pop()
            else:
                return
        backtrack(0,[],0)
        return res
