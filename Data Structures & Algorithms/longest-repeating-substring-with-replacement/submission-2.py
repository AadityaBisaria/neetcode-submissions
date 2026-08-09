class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        hmap=defaultdict(int)
        maxlen=0
        for r in range(len(s)):
            hmap[s[r]]+=1
            while(sum(hmap.values())-max(hmap.values()))>k:
                hmap[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen