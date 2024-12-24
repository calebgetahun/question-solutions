def increasing_money(nums: list):
    increasing = 1
    maxSub = 1
    for i in range(1, len(nums)):
        if nums[i] >= nums[i - 1]:
            increasing += 1
        else:
            increasing = 1
        maxSub = max(maxSub, increasing)

    return maxSub

if __name__ == "__main__":
    n = int(input())

    nums = list(map(int, input().split(" ")))
    
    print(increasing_money(nums))

# TC: O(N)
# SC: O(1)