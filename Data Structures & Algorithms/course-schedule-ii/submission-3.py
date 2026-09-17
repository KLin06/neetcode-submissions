class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        postreqs = defaultdict(list)
        num_prereqs = [0] * numCourses
        for a, b in prerequisites:
            postreqs[b].append(a)
            num_prereqs[a] += 1
        
        order = []
        q = deque([i for i in range(numCourses) if num_prereqs[i] == 0])

        while q:
            completed_course = q.popleft()
            order.append(completed_course)
            for postreq in postreqs[completed_course]:
                num_prereqs[postreq] -= 1
                if num_prereqs[postreq] == 0:
                    q.append(postreq)

        return order if len(order) == numCourses else []