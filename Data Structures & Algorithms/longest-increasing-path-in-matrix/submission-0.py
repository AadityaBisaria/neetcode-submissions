class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        ROW,COL=len(matrix),len(matrix[0])

        dp=[[1]*COL for _ in range(ROW)]
        dp={}
        visit=set()
        print(dp)
        neighbours=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j,value):
            if i<0 or i==ROW or j<0 or j==COL:
                return 0
            if (i,j,value) in dp:
                return dp[(i,j,value)]
            
            res=0
            if value<matrix[i][j]:
                for nei,neij in neighbours:
                    res=max(res,1+dfs(i+nei,j+neij,matrix[i][j]))
            
            dp[(i,j,value)]=res
            return dp[(i,j,value)]
    
        val=0
        for i in range(ROW):
            for j in range(COL):
                val=max(val,dfs(i,j,-1))
        return val