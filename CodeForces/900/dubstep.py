def main():
    song = input()
    original = []

    i = 0
    while i < len(song):
        if i + 3 <= len(song) and song[i:i+3] == "WUB":
            i += 3
        else:
            #use window to check substring
            j = i
            while j <= len(song):
                if j + 3 <= len(song) and song[j:j+3] == "WUB":
                    original.append(song[i:j])
                    i = j
                    break
                else:
                    j += 1
                    if j == len(song):
                        original.append(song[i:])
                        i = j
                        break

    return " ".join(original)

if __name__ == "__main__":
    print(main())