class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp={}
        reach=sum(nums)/2
        def dfs(i,total):
            if i>=len(nums):
                if total==reach:
                    return True
                else:
                    return False
            return dfs(i+1,total+nums[i]) or dfs(i+1,total)
        return dfs(0,0)