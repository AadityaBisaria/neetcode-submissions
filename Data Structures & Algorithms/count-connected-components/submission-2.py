class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank=[1]*n

        def find(i):
            while i!=parent[i]:
                i=parent[parent[i]]
            return parent[i]


        def union(n1,n2):
            x=find(n1)
            y=find(n2)

            if rank[x]>=rank[y]:
                rank[x]+=rank[y]
                parent[y]=x

            else:
                rank[y]+=rank[x]
                parent[x]=y
     

        for a,b in edges:
            union(a,b)
        print(parent)
        print(rank)
        return len(set(find(x) for x in range(n)))
