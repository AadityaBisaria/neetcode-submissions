class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #intervals=[[1,100],[11,22],[1,11],[2,12]]
        intervals.sort(key= lambda x: x[1])

        dp={}

        def dfs(i):

            if i in dp:
                return dp[(i)]
            res=1
            for j in range(i+1,len(intervals)):
                if intervals[i][1] <= intervals[j][0]:
                    res= max(res,1+dfs(j))
            
            dp[i]=res
            return res
        return len(intervals)-dfs(0)