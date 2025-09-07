if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    taxis = 0

    i = 0
    while i < len(arr):
        if arr[i] == 4:
            taxis += 1
        else:
            break
        
        i += 1
    
    j = len(arr) - 1

    while j >= i:
        curr_sum = arr[i]
        i += 1

        while i <= j and curr_sum + arr[j] <= 4:
            curr_sum += arr[j]
            j -= 1

        taxis += 1 

    print(taxis)

# TC: O(NlogN)
# SC: O(1) for in place sort, not including variable space
