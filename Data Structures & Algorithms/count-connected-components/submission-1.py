class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        cnt = 0
        
        adj_list = {}
        for a, b in edges:
            adj_list.setdefault(a, []).append(b)
            adj_list.setdefault(b, []).append(a)
        
        for i in range(n):
            if not visited[i]:
                cnt += 1
                q = deque([i])
                while q:
                    curr = q.popleft()
                    visited[curr] = True
                    for neighbour in adj_list.get(curr, []):
                        if not visited[neighbour]:
                            q.append(neighbour)

        return cnt