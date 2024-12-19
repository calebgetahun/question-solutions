if __name__ == "__main__":
    inputs = list(map(int, input().split(" ")))
    n = inputs[0]
    iterations = inputs[1]
    line = list(input())

    for i in range(iterations):
        curr = 0
        while curr < n-1:
            if line[curr] == 'B' and line[curr+1] == 'G':
                line[curr], line[curr+1] = line[curr+1], line[curr]
                curr += 1
            curr += 1
    
    print("".join(line))
