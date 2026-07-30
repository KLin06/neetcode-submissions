class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)

        def transformable(str1, str2):
            different = 0
            for i in range(n):
                if str1[i] != str2[i]: different += 1
            return different == 1

        neighbours = {}

        wordList.append(beginWord)

        m = len(wordList)

        for i in range(m):
            str1 = wordList[i]
            for j in range(i + 1, m):
                str2 = wordList[j]
                if transformable(str1, str2):
                    neighbours.setdefault(str1, []).append(str2)
                    neighbours.setdefault(str2, []).append(str1)

        visited = set()

        q = deque([(beginWord, 1)])
        while q: 
            curr, length = q.popleft()
            visited.add(curr)

            if curr == endWord:
                return length

            for neighbour in neighbours.get(curr, []):
                if not neighbour in visited: 
                    q.append((neighbour, length + 1))

            neighbours.pop(curr, None)

        return 0