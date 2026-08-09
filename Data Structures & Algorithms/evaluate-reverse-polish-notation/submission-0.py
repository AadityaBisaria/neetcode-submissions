class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c=='+':
                a,b=stack.pop(),stack.pop()
                stack.append(a+b)
            elif c=='-':
                b,a=stack.pop(),stack.pop()
                stack.append(a-b)
            elif c=='*':
                b,a=stack.pop(),stack.pop()
                stack.append(a*b)
            elif c=='/':
                b,a=stack.pop(),stack.pop()
                stack.append(int(float(a)/b))
            else:
                stack.append(int(c))
        return stack[0]