def football(n: str):
    if len(n) < 7:
        return "NO"
    
    curr_val = n[0]
    count = 1
    i = 1
    while i < len(n):
        if n[i] == curr_val:
            while i < len(n) and n[i] == curr_val:
                count += 1
                i += 1
            if count >= 7:
                return "YES"
        else:
            if int(curr_val):
                curr_val = '0'
            else:
                curr_val = '1'
            i += 1
            count = 1
        
    return "NO"
        
if __name__ == "__main__":
    n = input()
    print(football(n))
    
# TC: O(N)
# SC: O(1)