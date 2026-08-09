class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        l=0
        sublen,res=float("infinity"),[-1,-1]
        s_set,t_set={},{}
        for c in t:
            t_set[c]=1+t_set.get(c,0)

        need,have=len(t_set),0
        for r in range(len(s)):
            c=s[r]
            if(c in t_set):
                s_set[c]=1+s_set.get(c,0)
                if s_set[c]==t_set[c]:
                    have+=1
            while(have==need):
                if(r-l+1)<sublen:
                    res=[l,r]
                    sublen=r-l+1
                if s[l] in t_set:
                    s_set[s[l]]-=1
                if(s[l] in t_set and s_set[s[l]]<t_set[s[l]]):
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1]

