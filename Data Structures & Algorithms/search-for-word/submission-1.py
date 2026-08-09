class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        visit=set()
        directions=[(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(r,c,w):
            if word ==w:
                return True
            if 0>r or r>=rows or 0>c or c>=cols or (r,c) in visit:
                return False
            
            visit.add((r,c))
            w+="".join(board[r][c])
            for lr,lc in directions:
                if dfs(r+lr,c+lc,w):
                    return True
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,""):
                    return True
        return False