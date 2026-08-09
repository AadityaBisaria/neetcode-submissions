class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def rec(n):
            if n<=1:
                return 0
            if n in dp:
                return dp[n]
            
            dp[n]=min(rec(n-1)+cost[n-1],rec(n-2)+cost[n-2])
            return dp[n]
        return rec(len(cost))