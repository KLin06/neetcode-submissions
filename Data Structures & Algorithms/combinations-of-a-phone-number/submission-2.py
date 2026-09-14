class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        phone_keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        sol = []
        def backtrack(digits, curr, i):
            nonlocal sol
            if i == n: 
                if curr:
                    sol.append("".join(curr))
                return 

            for c in phone_keypad[digits[i]]:
                curr.append(c)
                backtrack(digits, curr, i + 1)
                curr.pop()

        backtrack(digits, [], 0)

        return sol


        
        