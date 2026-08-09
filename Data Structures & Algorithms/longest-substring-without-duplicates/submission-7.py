class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap=defaultdict(int)
        l,r=0,0
        maxlen=0
        for r in range(len(s)):
            hmap[s[r]] += 1
            while hmap[s[r]]>1:
                hmap[s[l]]-=1
                l+=1
                if not hmap[s[l]]:
                    del hmap[s[l]]
            maxlen=max(maxlen,r-l+1)
        return maxlen
