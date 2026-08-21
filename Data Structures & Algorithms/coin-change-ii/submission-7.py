class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        coins.sort()
        if amount==0:
            return 1
        def dfs(amt,i):
            if amt==0:
                return 1
            if (amt,i) in dp:
                return dp[(amt,i)]
            
            count=0
            for j in range(i,-1,-1):
                amount=amt-coins[j]
                if amount<0:
                    continue
                count+=dfs(amount,j)
            dp[(amt,i)]=count
            return count
        dfs(amount,len(coins)-1)
        return max(dp.values())
