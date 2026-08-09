class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target=sum(nums)//2
        if sum(nums)%2!=0:
            return False
        dp=set()
        nextdp=set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            nextdp=set(dp)
            for t in dp:
                if t+nums[i]==target:
                    return True
                if t+nums[i]<target:
                    nextdp.add(t+nums[i])
            dp=nextdp
        return False

                    