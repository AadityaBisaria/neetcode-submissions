class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter=set(nums)

        def is_it(num):
            if num in counter:
                return 1+is_it(num+1)
            else:
                return 0
        
        maxnum=0
        for i in counter:
            maxnum=max(maxnum,is_it(i))
        return maxnum