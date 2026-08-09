class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        print(nums)
        total=float("-inf")
        l=0
        while l<len(nums):
            r=l+1
            while r<len(nums) and nums[r]==nums[r-1]+1:
                total=max(total,r-l+1)
                r+=1
            l=r
        return total if total!=float("-inf") else 1