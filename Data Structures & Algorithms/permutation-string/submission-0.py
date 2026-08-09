from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(s1==None):
            return True
        l,r=0,len(s1)
        item=Counter(s1).items()
        while(r!=(len(s2)+1)):
            substring=s2[l:r]
            if(item==Counter(substring).items()):
                return True
            l+=1
            r+=1
        return False