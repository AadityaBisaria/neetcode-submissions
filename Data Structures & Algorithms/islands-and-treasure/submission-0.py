class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        q= collections.deque()

        def addcell(row,col):
            if row<0 or row==rows or col<0 or col == cols or (row,col) in visited or grid[row][col]==-1:
                return 
            visited.add((row,col))
            q.append([row,col])
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    q.append([row,col])
                    visited.add((row,col))
                
        dist=0
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                grid[row][col]=dist
                addcell(row-1,col)
                addcell(row+1,col)
                addcell(row,col-1)
                addcell(row,col+1)
            dist+=1