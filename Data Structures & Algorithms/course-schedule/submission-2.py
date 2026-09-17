class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        num_prereqs = [0] * numCourses

        for a,b in prerequisites:
            # b is a prereq for a
            prereqs[b].append(a)
            num_prereqs[a] += 1
        
        stack = [course for course, count in enumerate(num_prereqs) if count == 0]
        completed = 0

        while stack:
            completed += 1
            completed_course = stack.pop()
            for post in prereqs[completed_course]:
                num_prereqs[post] -= 1
                if num_prereqs[post] == 0:
                    stack.append(post)
        
        return completed == numCourses



