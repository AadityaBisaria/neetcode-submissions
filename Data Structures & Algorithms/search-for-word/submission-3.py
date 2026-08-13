class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        visit=set()

        def dfs(row,col,i):
            if i==len(word):
                return True
            if row<0 or row>=rows or col<0 or col>=cols or (row,col) in visit or board[row][col]!=word[i]:
                return False
            x=False
            visit.add((row,col))
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                result = dfs(row+dr,col+dc,i+1)
                if result == True:
                    return True
            visit.remove((row,col))
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        
        return False