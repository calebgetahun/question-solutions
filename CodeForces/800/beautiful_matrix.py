if __name__ == "__main__":
    #center at 2, 2
    for i in range(5):
        row = input().split(" ")
        if row.count('1'):
            col = row.index('1')
            diff = abs(i-2) + abs(int(col)-2)
            print(diff)
            break

# TC: O(N^2) worst case assuming N is the size in the NxN matrix and we must read through entire matrix
# SC: O(1)