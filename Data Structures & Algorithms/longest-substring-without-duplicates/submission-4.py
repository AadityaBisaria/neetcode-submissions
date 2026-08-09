from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        l=0
        r=0
        maxlen=0
        while(r<len(s)):
            Map=Counter(s[l:r+1])
            while max(Map.values())!=1:
                Map[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
            
                