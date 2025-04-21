def brute_force(arr):
    largest_xor = 0
    
    for i in range(len(arr)):
        curr_xor = 0
        for j in range(len(arr)):
            curr_xor += arr[i] ^ arr[j]
        largest_xor = max(largest_xor, curr_xor)

    return largest_xor

def using_bitmasks(arr):
    n = len(arr)
    bit_count = [0] * 30
    for num in arr:
        for j in range(30):
            if num & (1 << j):
                bit_count[j] += 1

    max_xor = 0
    for k in range(n):
        curr_xor = 0
        for j in range(30):
            if arr[k] & (1 << j):
                #we have a 1 in that bit position, meaning we'd need a 0 to make our xor
                curr_xor += (n - bit_count[j]) * (1 << j)
            else:
                #there is a 0 at this position, meaning we'd need a 
                curr_xor += bit_count[j] * (1 << j)
        max_xor = max(max_xor, curr_xor)

    return max_xor

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        curr_input = list(map(int, input().split(" ")))

        print(using_bitmasks(curr_input))

# TC: O(30N) as we are going through each each value in our list once and for each number, going through each of the 30 bits.
# SC: O(30) => O(1)
