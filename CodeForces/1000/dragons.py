from typing import List

def dragons(s, dragon_strengths: List):
    curr = s
    dragon_strengths.sort()
    for i, j in dragon_strengths:
        if curr <= i:
            return "NO"
        else:
            curr += j

    return "YES"

if __name__ == "__main__":
    s, n = map(int, input().split(" "))
    strengths = []
    for _ in range(n):
        strength, boost = map(int, input().split(" "))
        strengths.append((strength, boost))
    
    print(dragons(s, strengths))
