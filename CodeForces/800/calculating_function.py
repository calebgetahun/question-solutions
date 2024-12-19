def calculate_function(n):
    if n % 2 == 0:
        return n // 2
    else:
        return -1*(n//2 + 1)

if __name__ == "__main__":
    n = int(input())
    print(calculate_function(n))
