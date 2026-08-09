class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        maxarea=0
        visited=set()
        def dfs(row,col):
            if (row not in range(ROWS)
             or col not in range(COLS)
             or (row,col) in visited 
             or grid[row][col]==0
            ):return 0
            visited.add((row,col))
            area=1
            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            for r,c in directions:
                area+=dfs(row+r,col+c)
            return area
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==1 and (row,col) not in visited:
                    maxarea=max(maxarea,dfs(row,col))
        return maxarea
