if __name__ == "__main__":
    #center at 2, 2
    for i in range(5):
        row = input().split(" ")
        if row.count('1'):
            col = row.index('1')
            diff = abs(i-2) + abs(int(col)-2)
            print(diff)
            break
