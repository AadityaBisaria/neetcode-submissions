class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #gives me bfs vibes cuz we have to check each level at every second
        rows,cols=len(grid),len(grid[0])
        q=collections.deque()
        visited=set()
        time,fresh = 0,0
        
        def addcell(r,c):
            if r<0 or r==rows or c<0 or c==cols or (r,c) in visited or grid[r][c]==0:
                return
            nonlocal fresh
            fresh-=1
            visited.add((r,c))
            q.append([r,c])
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    visited.add((r,c))
                    q.append([r,c])
        
        while  fresh>0 and q:
            length=len(q)
            for notfresh in range(length):
                row,col=q.popleft()
                
                addcell(row-1,col)
                addcell(row+1,col)
                addcell(row,col+1)
                addcell(row,col-1)
            time+=1

        return time if fresh==0 else -1          
