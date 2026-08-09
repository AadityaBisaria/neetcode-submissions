class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache=[amount+1]*(amount+1)
        cache[0]=0

        for a in range(1,amount+1):
            for coin in coins:
                if (a-coin)>=0:
                    cache[a]=min(cache[a],1+cache[a-coin])

        return cache[amount] if cache[amount]!=(amount+1) else -1
        