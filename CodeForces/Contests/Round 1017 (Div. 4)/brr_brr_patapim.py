def permutation(n, grid):
    values = set()
    for i in range(1, n+1):
        values.add(i)
    
    res = [0] * n
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res[i+j+1] = grid[i][j]
            if res[i+j+1] in values:
                values.remove(res[i+j+1])
    
    res[0] = values.pop()
    return res

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        grid = []
        for i in range(n):
            line = list(map(int, input().split(" ")))
            grid.append(line)
        print(" ".join(map(str, permutation(2 * n, grid))))
        