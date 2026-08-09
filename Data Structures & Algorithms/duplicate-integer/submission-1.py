class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            return max(Counter(nums).values())>1
        else:
            return False    
        
