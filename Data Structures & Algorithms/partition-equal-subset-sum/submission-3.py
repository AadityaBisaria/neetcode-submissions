class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp={}
        n=len(nums)
        reach=sum(nums)/2
        def dfs(i,total):
            if total == reach:
                return True
            if i >= n or total>reach:
                return False
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)]= dfs(i+1,total+nums[i]) or dfs(i+1,total)
            return dp[(i,total)]
        return dfs(0,0)
 