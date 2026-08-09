class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par=[i for i in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)
        def find(n):
            p=par[n]
            while(p!=par[p]):
                p=par[par[p]]
                p=par[p]
            return p

        def Union(x,y):
            x=find(x)
            y=find(y)
            if x==y:
                return False 
            if rank[x]>rank[y]:
                par[y]=x
                rank[x]+=rank[y]
            
            else:
                par[x]=y
                rank[y]+=rank[x]
            
            return True
        
        for n1,n2 in edges:
            if not Union(n1,n2):
                return [n1,n2]
        
        return []