class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        rows,cols=len(board),len(board[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,row,col):

            if i==len(word):
                return True
            if row==rows or row<0 or col== cols or col<0 or (row,col) in visited:
                return False

            visited.add((row, col)) 
            if board[row][col]==word[i]:

                q=False
                for r,c in directions:
                    q=q or dfs(i+1,row+r,col+c)
                if q :
                    return q
                else:
                    visited.remove((row, col))
                    return False
            else:
                visited.remove((row, col))
                return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col]==word[0]:
                    visited.clear()
                    if dfs(0,row,col):
                        return True
             
        return False
