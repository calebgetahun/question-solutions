def sounds(p, s):
    if p == s:
        return "YES"
    
    if p[0] != s[0]:
        return "NO"
    
    i, j = 0, 0
    while i < len(p) and j < len(s):
        curr = p[i]
        i_range, j_range = i, j
        while i_range < len(p) and p[i_range] == curr:
            i_range += 1
        
        while j_range < len(s) and s[j_range] == curr:
            j_range += 1
        
        if (i_range - i) > (j_range - j) or (j_range - j) > 2 * (i_range - i):
            return "NO"

        i = i_range
        j = j_range
    
    if i != len(p) or j != len(s):
        return "NO"


    return "YES"
    

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        p = input()
        s = input()
        print(sounds(p, s))