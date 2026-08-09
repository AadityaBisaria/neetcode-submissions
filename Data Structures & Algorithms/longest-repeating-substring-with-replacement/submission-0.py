from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s==None:
            return 0
        l,r=0,1
        maxlen=0
        while(l<r and r!=len(s)+1):
            substring=s[l:r]
            sub=max(Counter(substring).values())
            if(len(substring)-sub<=k):
                if(maxlen<len(substring)):
                    maxlen=len(substring)
                r+=1
            else:
                l+=1
        return maxlen