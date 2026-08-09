class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands=0
        visit=set()
        row,col=len(grid),len(grid[0])
        
        def dfs(r,c):
            if ( r not in range(row)
             or c not in range(col)
             or grid[r][c]=="0"
             or (r,c) in visit):
                return 
            visit.add((r,c))
            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                dfs(r+dr,dc+c)


        for r in range(row):
            for c in range(col):
                if grid[r][c] =="1" and (r,c) not in visit:
                    islands+=1
                    dfs(r,c)
        
        return islands


