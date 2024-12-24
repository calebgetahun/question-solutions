def eval_operation(oper):
    if oper.count("-"):
        return -1
    else:
        return 1
        
if __name__ == "__main__":
    n = int(input())
    solution = 0
    for i in range(n):
        solution += eval_operation(input())
    print(solution)

# TC: O(N) for N operations
# SC: O(1)