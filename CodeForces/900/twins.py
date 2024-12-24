def twins(values: list):
    total = sum(values)
    curr_total = 0
    coin_total = 0
    i = len(values) - 1

    while curr_total <= total and i >= 0:
        curr_total += values[i]
        coin_total += 1
        total -= values[i]
        i -= 1

    return coin_total

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split(" ")))
    values.sort()

    print(twins(values))

# TC: O(NlogN) because of sorting at beginning
# SC: O(N) also because of sorting