def way_too_long_words(word):
    if len(word) > 10:
        abb = [word[0], str(len(word)-2),word[len(word)-1]]
        print("".join(abb))
    else:
        print(word)
        
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        way_too_long_words(input())

