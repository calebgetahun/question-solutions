if __name__ == "__main__":
    n = int(input())
    stones = list(input())
    removed = 0
    for i in range(n-1):
        if stones[i] == stones[i+1]:
            removed += 1
    print(removed)

# TC: O(N)
# SC: O(1)