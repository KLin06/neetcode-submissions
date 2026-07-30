class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # count the number of incoming and outgoing edges
        # if there aren't the same number, then it must be the start or the end
        # for all the ones that are the same number, you can go to any of them
        # just check which one is the lowest lexographically
        # every time we go to a node, we remove them from the list of connections and their number of connections
        # since tickets aren't unique, we can't use a set. 
        # from_to_count stores (incoming, outgoing)
        # if there's zero outgoings just don't go there
        adj_list = {}

        for from_i, to_i in tickets:
            adj_list.setdefault(from_i, []).append(to_i)

        for src in adj_list:
            adj_list[src] = deque(sorted(adj_list[src]))

        stack = ["JFK"]
        path = []
        
        while stack:
            curr = stack[-1]
            if len(adj_list.get(curr, [])) == 0:
                path.append(curr)
                stack.pop()
                continue
            stack.append(adj_list[curr].popleft())

        return path[::-1]
