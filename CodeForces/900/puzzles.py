def main():
    n, m = map(int, input().split(" "))

    puzzles = list(map(int, input().split(" ")))
    puzzles.sort()

    ans = puzzles[n-1] - puzzles[0]

    for i in range(m-n):
        new_diff = puzzles[i+n] - puzzles[i+1]
        ans = min(ans, new_diff)

    return ans

if __name__ == "__main__":
    print(main())