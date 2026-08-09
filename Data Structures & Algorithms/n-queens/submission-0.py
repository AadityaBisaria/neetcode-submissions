class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        print(board)
        res=[]
        def isSafe(r:int, c:int,board):
            row=r-1
            while row>=0:
                if board[row][c]=="Q":
                    return False
                row-=1

            row,col=r-1,c-1
            while col>=0 and row>=0:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1

            row,col=r-1,c+1
            while row>=0 and col<n:
                if board[row][col]=="Q":
                    return False
                row-=1
                col+=1
            return True

        def backtracking(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return 
            for c in range(n):
                if isSafe(r,c,board):
                    board[r][c]='Q'
                    backtracking(r+1)
                    board[r][c]="."
        backtracking(0)
        return res

        