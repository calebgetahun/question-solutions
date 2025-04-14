def concat(s):
    output = []
    for word in s:
        output.append(word[0])

    return "".join(output)

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        case = input().split(" ")
        print(concat(case))