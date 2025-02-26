def B(s: str):
    if len(s) < 3:
        print("0")
        return
    top = bottom = 0
    for char in s:
        if char == "-":
            top += 1
        else:
            bottom += 1
    
    if top < 2:
        print("0")
        return
    
    if top % 2 == 0:
        print(bottom * (top // 2) * (top // 2))
        return
    else:
        print(bottom * (top // 2) * ((top // 2) + 1))
        
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        n = int(input())
        s = input()
        B(s)
