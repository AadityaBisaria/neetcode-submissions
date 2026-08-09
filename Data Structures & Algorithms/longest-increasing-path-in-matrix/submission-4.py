class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        map={}
        longest=0
        rows=len(matrix)
        cols=len(matrix[0])
        def check(row,col,prev):
            if row>=rows or col>=cols or row<0 or col<0 or prev>=matrix[row][col]:
                return 0
            if (row,col) in map:
                return map[(row,col)]
            x=1
            x=max(x,1+check(row-1,col,matrix[row][col]))
            x=max(x,1+check(row+1,col,matrix[row][col]))
            x=max(x,1+check(row,col+1,matrix[row][col]))
            x=max(x,1+check(row,col-1,matrix[row][col]))
            map[(row,col)]=x

            return map[(row,col)]
        for row in range(rows):
            for col in range (cols):
                check(row,col,-1)
        return max(map.values())