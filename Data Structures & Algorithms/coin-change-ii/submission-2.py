class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        
        def dfs(a, idx):
            if a == 0:
                return 1
            if (a, idx) in cache:
                return cache[(a, idx)]
            res = 0
            for i in range(idx, len(coins)):
                if a - coins[i] >= 0:
                    res += dfs(a - coins[i], i)
            cache[(a, idx)] = res
            return res

        return dfs(amount, 0)