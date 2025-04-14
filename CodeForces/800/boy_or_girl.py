def main():
    name = input()
    chars = set()

    for char in name:
        chars.add(char)
    
    return "CHAT WITH HER!" if len(chars) % 2 == 0 else "IGNORE HIM!"

if __name__ == "__main__":
    print(main())