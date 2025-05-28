def lucky_division(n):
    if is_lucky(n):
        return "YES"
    
    #pre-computed based on problem constraints
    lucky_nums = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

    for lucky_num in lucky_nums:
        if n % lucky_num == 0:
            return "YES"

    return "NO"

def is_lucky(num):
    while num > 0:
        rem = num % 10
        if rem != 4 and rem != 7:
            return False
        num //= 10

    return True

def lucky_division_no_arr(n):
    for i in range(1, n+1):
        if is_lucky(i):
            if n % i == 0:
                return "YES"
            
    return "NO"

        
if __name__ == "__main__":
    n = int(input())
    print(lucky_division_no_arr(n))

# TC: O(logN) in precomputed case, O(NlogN) with no precomputation
# SC: O(1) in both cases