class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        dp[1]=1
        dp[0]=1
        def step(n):
            if n in dp:
                return dp[n]
            
            if n>=2:
                dp[n]= step(n-1)+step(n-2)
                return dp[n]
        return step(n)