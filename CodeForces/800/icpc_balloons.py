def number_of_balloons(count: int, problems: str):
    seen = set()
    total = 0
    for problem in problems:
        if problem in seen:
            total += 1
        else:
            seen.add(problem)
            total += 2
        
    return total

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        length = int(input())
        problems = input()
        print(number_of_balloons(length, problems))


# TC: O(N), where N is the length of the string that denotes that problems have been solved
# SC: O(N), because of our set