def main():
    num = int(input())
    lucky_numbers = 0

    while num > 0:
        curr = num % 10
        if curr == 4 or curr == 7:
            lucky_numbers += 1
        
        num = num // 10
    return "YES" if lucky_numbers == 4 or lucky_numbers == 7 else "NO"

if __name__ == "__main__":
    print(main())