def hq9plus(s: str):
    commands = {"H", "Q", "9"}
    for char in s:
        if char in commands:
            return("YES")
    return("NO")

if __name__ == "__main__":
    command = input()
    print(hq9plus(command))

# TC: O(N)
# SC: O(1)