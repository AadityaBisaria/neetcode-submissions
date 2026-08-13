class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        visit=set()

        def dfs(row,col,cur):
            if cur==word:
                return True
            if row<0 or row>=rows or col<0 or col>=cols or (row,col) in visit :
                return False
            x=False
            visit.add((row,col))
            x= x or dfs(row+1,col,cur+board[row][col])
            x= x or dfs(row-1,col,cur+board[row][col])
            x= x or dfs(row,col+1,cur+board[row][col])
            x= x or dfs(row,col-1,cur+board[row][col])
            visit.remove((row,col))
            return x

        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,""):
                    return True
        
        return False