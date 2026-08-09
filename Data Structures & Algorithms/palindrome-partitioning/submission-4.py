class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def pal(strng):
            if strng==strng[::-1]:
                return True
            else:
                return False
        
        def backtrack(i,cur):
            if i==len(s):
                res.append(cur.copy())
                return
            for j in range(i+1,len(s)+1):
                if pal(s[i:j]):
                    cur.append(s[i:j])
                    backtrack(j,cur)
                    cur.pop()
            return
        
        backtrack(0,[])
        return res



