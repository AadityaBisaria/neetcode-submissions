class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache=[0]*(amount+1)
        cache[0]=1
        for i in range(len(coins)-1,-1,-1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1
            for a in range(1,(amount)+1):
                nextDP[a]=cache[a]
                if a-coins[i]<0:
                    continue
                nextDP[a]+=nextDP[a-coins[i]]
            cache=nextDP
        return cache[amount]