class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visited=set()
        direction=[(0,-1),(1,0),(0,1),(-1,0)]
        def dfs(r,c):

            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited or grid[r][c]=="0":
                return False

            visited.add((r,c))
            for dr,dc in direction:
                dfs(dr+r,dc+c)
            return True
        
        res=0 

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row,col):
                    res+=1
        return res