class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        dp={}
        def dfs(i,left):
            if left<0:
                return False
            if i==n:
                return left==0

            if (i,left) in dp:
                return dp[(i,left)]
            
            if s[i]=="(":
                result=dfs(i+1,left+1)
            elif s[i]==")":
                result=dfs(i+1,left-1)
            else:
                result = (dfs(i+1,left) or dfs(i+1,left-1) or dfs(i+1,left+1))
            dp[(i,left)]=result
            return dp[(i,left)]
        return dfs(0,0)