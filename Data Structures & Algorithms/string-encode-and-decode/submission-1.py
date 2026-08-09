class Solution:

    def encode(self, strs: List[str]) -> str:
        final="".join(string+"`" for string in strs)
        return final

    def decode(self, s: str) -> List[str]:
        word=list(s.split("`"))
        word.pop()
        return word