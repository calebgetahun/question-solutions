def ways_to_win(people, fingers):
    total = sum(fingers)
    ans = 0

    for i in range(1, 6):
        if (total + i) % (people + 1) != 1:
            ans += 1
    print(ans)
    
if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split(" ")))
    ways_to_win(people=n, fingers=values)
