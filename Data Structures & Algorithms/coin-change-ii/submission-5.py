class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        coins.sort()
        def dfs(total,idx):
            
            if total==amount:
                return 1
            if idx==len(coins) or total+coins[idx]>amount:
                return 0
            if (total,idx) in cache:
                return cache[(total,idx)]
            
            res=0
            res+=dfs(total+coins[idx],idx)
            res+=dfs(total,idx+1)   
            cache[(total,idx)]=res         
            return cache[(total,idx)]
        return dfs(0, 0)