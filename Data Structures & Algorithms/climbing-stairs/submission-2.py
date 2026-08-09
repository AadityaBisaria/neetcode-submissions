class Solution:
    def climbStairs(self, n: int) -> int:
        map={}
        def start( i):
            if i <= 1:
                return 1
            
            if i in map:
                return map[i]
            x= start(i-1)+start(i-2)
            map[i]=x
            return x
        
        return start(n)