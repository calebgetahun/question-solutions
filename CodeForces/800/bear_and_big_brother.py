def years(a, b) -> int:
    year = 0
    while a <= b:
        a = a * 3
        b = b * 2
        year += 1
    return year
        
if __name__ == "__main__":
    a, b = input().split(" ")
    print(years(int(a), int(b)))
