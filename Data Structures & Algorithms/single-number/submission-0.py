class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val=nums[0]
        for num in range(1,len(nums)):
            val=val ^ nums[num]
        return val