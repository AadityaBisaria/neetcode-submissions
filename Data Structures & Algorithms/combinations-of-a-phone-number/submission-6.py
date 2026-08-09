class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        word=[]
        if not digits:
            return []
        digitToChar ={
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
        }   
        def backtrack(idx):
            if idx==len(digits):
                res.append("".join(word.copy()))
                return
            for char in digitToChar[digits[idx]]:
                word.append(char)
                backtrack(idx+1)
                word.pop()
        backtrack(0)
        return res
