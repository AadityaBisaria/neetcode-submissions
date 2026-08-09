class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        map={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        

        def backtrack(i,cur):
            if len(cur)==len(digits):
                res.append("".join(cur.copy()))
                return

            for digit in map[digits[i]]:
                cur+=digit
                backtrack(i+1,cur)
                cur.pop()
        if digits:
            backtrack(0,[])
        return res
