def infected(n, m, l, r):
    if m == n:
        return f"{l} {r}"
    
    left, right = 0, 0
    for i in range(m):
        if left <= l:
            right += 1
        elif right >= r:
            right += 1
        else:
            left -= 1
    
    return f"{left} {right}"

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        n, m, l, r = map(int, input().split(" "))
        print(infected(n, m, l, r))