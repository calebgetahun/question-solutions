if __name__ == "__main__":
    weight = int(input("Give me a weight for the watermelon: "))
    if weight % 2 == 0 and weight > 2:
        print("YES")
    else:
        print("NO")

# TC: O(1)
# SC: O(1)
