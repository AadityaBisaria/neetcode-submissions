from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap=Counter(nums)
        sorted_items=sorted(hmap.items(),key= lambda x: x[1],reverse=True)
        return [item[0] for item in sorted_items[:k]] 