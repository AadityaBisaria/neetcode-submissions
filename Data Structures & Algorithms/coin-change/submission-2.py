class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp={}
        def dfs(i,total):

            if total==amount:
                return 0
            if total>amount or i==len(coins):
                return float("inf")
            
            if (i,total) in dp:
                return dp[(i,total)]
            
            include=1+dfs(i,total+coins[i])
            skip=dfs(i+1,total)
            dp[(i,total)]=min(include,skip)
            
            return dp[(i,total)]
        return dfs(0,0) if dfs(0,0)!= float("inf") else -1