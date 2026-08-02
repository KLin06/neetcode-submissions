class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # for each level, have two steps: set a ( and set a )
        res = []
        def generate_parens(s, open, close):
            if len(s) == 2 * n and open == close:
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
        