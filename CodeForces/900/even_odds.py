def even_odds(k, n):
    if k <= (n + 1) // 2:
        return (k * 2) - 1
    else:
        return (k - (n + 1) // 2) * 2

if __name__ == "__main__":
    n, k = map(int, input().split(" "))
    print(even_odds(k, n))
