def way_too_long_words(word):
    if len(word) > 10:
        abb = [word[0], str(len(word)-2), word[len(word)-1]] # ['l', '10', 'n']
        print("".join(abb))
    else:
        print(word)
        
if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        way_too_long_words(input())

# TC: O(1)
# SC: O(log base 10 of N) since our auxillary array may grow depending on the amount of characters between the first and last character by a factor of 10

