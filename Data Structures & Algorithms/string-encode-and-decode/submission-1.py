class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}_{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        original = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            l = int(s[i: j])
            original.append(s[j + 1: j + l + 1])
            i = j + l + 1
        return original
