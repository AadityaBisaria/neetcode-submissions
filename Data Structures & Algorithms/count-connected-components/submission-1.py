class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        parent=[i for i in range(n)]
        rank=[1]*n
        def find(i):
            while i!=parent[i]:
                i=parent[parent[i]]
            return i
        
        def union(left,right):
            x=find(left)
            y=find(right)
            if rank[x]==rank[y] or rank[x]>rank[y]:
                parent[y]=x
                rank[x]+=rank[y]
            else:
                parent[x]=y
                rank[y]+=rank[x]

        for node1,node2 in edges:
            union(node1,node2)

        return len(set(find(x) for x in range(n)))