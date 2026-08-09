class Solution:
    def jump(self, nums: List[int]) -> int:
        dp={i: float('inf') for i in range (len(nums))}
        dp[len(nums)-1]=0
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+nums[i],i,-1):
                if j>=len(nums)-1:
                    dp[i]=1
                    break
                dp[i]=min(dp[i],1+dp[j])
        return dp[0] if dp[0] is not float('inf') else -1