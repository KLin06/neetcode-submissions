class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        connected_nodes = set()
        redundant = None 
        parents = [i for i in range(n)]

        def find_parent(parents, a): 
            if parents[a] == a: return a
            parents[a] = find_parent(parents, parents[a])
            return parents[a]

        def union(parents, a, b):
            root_a = find_parent(parents, a)
            root_b = find_parent(parents, b)
            if root_a != root_b:
                parents[root_b] = root_a

        def is_connected(parents, a, b):
            root_a = find_parent(parents, a)
            root_b = find_parent(parents, b)
            return root_a == root_b

        for edge in edges:
            a, b = edge[0] - 1, edge[1] - 1
            if is_connected(parents, a, b):
                redundant = edge
                continue
            
            union(parents, a, b)


        return redundant
        