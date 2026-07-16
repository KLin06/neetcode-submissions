class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < temp:
                _, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((temp, i))

        return result
            


        