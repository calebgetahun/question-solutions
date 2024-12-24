def find_max(nums: list):
    if len(nums) == 1:
        return nums[0]
    
    p1 = nums[0]
    p2 = find_max(nums[1:])

    if p1 > p2:
        return p1
    else:
        return p2
    
def binary_search(nums: list, val, low, high):
    #tail end recursive method
    # mid = low + (high - low) // 2
    # if nums[mid] == val:
    #     return mid
    # elif low >= high:
    #     return -1
    # else:
    #     return max(binary_search(nums, val, low, mid - 1), binary_search(nums, val, mid + 1, high))
    
    # Another implementation non-tail recursive
    if low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > val:
            return binary_search(nums, val, low, mid-1)
        elif nums[mid] < val:
            return binary_search(nums, val, mid + 1, high)
        else:
            return mid
    else:
        return - 1
    
def sum_nums(nums: list):
    if len(nums) == 1:
        return nums[0]
    
    return nums[0] + sum_nums(nums[1:])

def fibonacci(x):
    if x < 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

def sort_(nums: list, low, high):
    mid =  (low+high) // 2
    if high <= low:
        return [nums[mid]]

    first_half = sort_(nums, low, mid)
    second_half = sort_(nums, mid+1, high)

    return merge(first_half, second_half)
    
def merge(list1, list2):
    merged = list()
    p1, p2 = 0, 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            merged.append(list1[p1])
            p1 += 1
        elif list2[p2] < list1[p1]:
            merged.append(list2[p2])
            p2 += 1
    if p1 == len(list1):
        merged.extend(list2[p2:])
    if p2 == len(list2):
        merged.extend(list1[p1:])

    return merged

def main():
    pass
    #max number
    # nums = [1,2,3,4,5,6,6]
    #ans = find_max(nums)

    #binary search recurion
    # sorted_list = [-2,-1,4,5,6,7,9,11,14,20]
    # n = len(sorted_list) - 1

    # for num in sorted_list:
    #     val = binary_search(sorted_list, num, 0, n)
    #     print(val)

    #sum of list
    # sum_list = [1,2,3,4,5]
    # ans = sum_nums(sum_list)
    # print(ans)

    #fibonacii
    # ans = fibonacci(2)
    # print(ans)

    # l1 = [1,3,4,0,2,-5,6,-1,7,99]
    # print(sort_(l1, 0, len(l1)-1))

if __name__ == "__main__":
    main()