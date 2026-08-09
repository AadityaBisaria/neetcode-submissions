class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]   
        dp[0][0]=0           
                
        for r in range(m):
            for c in range(n):
                if r==0 or c==0:
                    dp[r][c]=1
                else:
                    if (c-1)>=0:
                        dp[r][c]+=dp[r][c-1]
                    if (r-1)>=0:
                        dp[r][c]+=dp[r-1][c]
        return dp[m-1][n-1]