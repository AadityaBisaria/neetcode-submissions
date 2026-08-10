class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans=[]
        def backtrack(left,right,cur):
            if right>left or left>n:
                return
            
            if right ==n:
                ans.append(cur)
            cur+="("
            backtrack(left+1,right,cur)
            cur=cur[:len(cur)-1]
            if right<left:
                cur+=")"
                backtrack(left,right+1,cur)
                cur=cur[:len(cur)-1]
        backtrack(0,0,"")
        return ans



