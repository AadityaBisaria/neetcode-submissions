class Solution:
    def rob(self, nums: List[int]) -> int:
        map={}

        def robber(position):
            if position >= len(nums):
                return 0
            if position in map:
                return map[position]

            num=max(nums[position] + robber(position+2), robber(position+1))
            map[position]=num
            return num
        
        return robber(0)