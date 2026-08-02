class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate_parens(s, open, close):
            if open == close == n:
                res.append("".join(s))
                return
            if open < n:
                s.append('(')
                generate_parens(s, open + 1, close)
                s.pop()
            if close < n and open > close:
                s.append(')')
                generate_parens(s, open, close + 1)
                s.pop()

        generate_parens([], 0, 0)
        return res
        