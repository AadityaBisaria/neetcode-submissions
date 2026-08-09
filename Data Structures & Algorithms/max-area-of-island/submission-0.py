class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        max_size=0
        visit=set()
        row,col=len(grid),len(grid[0])
        
        def dfs(r,c):
            if ( r not in range(row)
             or c not in range(col)
             or grid[r][c]==0
             or (r,c) in visit):
                return 0
            visit.add((r,c))
            size=1
            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                size+=dfs(r+dr,dc+c)
            return size


        for r in range(row):
            for c in range(col):
                if grid[r][c] ==1 and (r,c) not in visit:
                    max_size=max(max_size,dfs(r,c))
        
        return max_size