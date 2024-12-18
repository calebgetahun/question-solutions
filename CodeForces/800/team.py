if __name__ == "__main__":
    n = int(input())
    solved = 0
    for i in range(n):
        problem_results = input().split(" ")
        if problem_results.count('1') >= 2:
            solved += 1
        
    print(solved)
