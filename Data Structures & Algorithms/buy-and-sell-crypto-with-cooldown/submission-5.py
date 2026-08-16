class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(cur,buy):
            if cur>=len(prices):
                return 0
            if (cur,buy) in dp:
                return dp[(cur,buy)]
            
            if buy:
                profit=max(dfs(cur+1,False)-prices[cur],dfs(cur+1, True))

            if not buy: 
                profit=max(dfs(cur+2,True)+prices[cur],dfs(cur+1,False))

            dp[(cur,buy)]=profit
            return dp[(cur,buy)]
        dfs(0,True)
        return max(dp[(0,True)],0) 