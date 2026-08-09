class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stk.append(int(token))  
            else:
                val1,val2=stk.pop(),stk.pop()
                if token=="+":
                    stk.append(val1+val2)
                elif token=="-":
                    stk.append(val2-val1)
                elif token=="*":
                    stk.append(val1*val2)
                elif token=="/":
                    stk.append(int(float(val2)/val1))
        return stk[-1]      
