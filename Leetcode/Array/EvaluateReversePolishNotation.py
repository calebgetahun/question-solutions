import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {'+', '*', '/', '-'}
        ops = {"+": operator.add, 
               "-": operator.sub, 
               "*": operator.mul, 
               "/": operator.truediv}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                result = int(ops[token](second, first))
                stack.append(result)
        
        return stack[0]
        
if __name__ == "__main__":
    sol = Solution()
    equation_1 = ["2","1","+","3","*"]
    equation_2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(equation_1))
    print(sol.evalRPN(equation_2))

# TC: O(N) for iterating through equation
# SC: O(N) for stack