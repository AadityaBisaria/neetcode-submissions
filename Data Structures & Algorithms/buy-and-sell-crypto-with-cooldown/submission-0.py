class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache={}
        def dfs(stock,buy):
            if stock>=len(prices):
                return 0
            if (stock,buy) in cache:
                return cache[(stock,buy)]
            cooldown=dfs(stock+1,buy)
            if buy:
                net=dfs(stock+1,not buy)- prices[stock]
            else:
                net=dfs(stock+2,not buy)+prices[stock]
            cache[(stock,buy)]=max(cooldown,net)
            return cache[(stock,buy)]
        return dfs(0,True)
