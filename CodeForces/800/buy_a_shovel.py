def main():
    k, r = map(int, input().split(" "))

    shovels = 1
    total = k

    while shovels < 10:
        if total % 10 == r or total % 10 == 0:
            return shovels
        total += k
        shovels += 1
    
    return shovels

if __name__ == "__main__":
    print(main())