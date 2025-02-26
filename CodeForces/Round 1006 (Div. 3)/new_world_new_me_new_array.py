def new_world(n, k, p):
    k_mag = abs(k)
    if k_mag / p > n:
        print("-1")
        return

    if k_mag % p == 0:
        print(k_mag // p)
    else:
        print(k_mag // p + 1)
    
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        n, k, p = list(map(int, input().split(" ")))
        new_world(n, k , p)
        