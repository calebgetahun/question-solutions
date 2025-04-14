from collections import deque

def calculate_rizz(arr):
    rizz = 0
    for i in range(len(arr)):
        rizz += (arr[i] * (i+1))
    return rizz

def perform_operation(arr, op):
    rizz = 0
    if op == 1:
        #cyclic
        last = arr.pop()
        arr.appendleft(last)
        rizz = calculate_rizz(arr)


    if op == 2:
        #reversal
        arr.reverse()
        rizz = calculate_rizz(arr)

    return rizz


if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        arr = deque()
        num_of_operations = int(input())
        rizz = 0
        for _ in range(num_of_operations):
            curr = input()
            if curr[0] == "3":
                values = curr.split(" ")
                k = int(values[1])
                arr.append(k)
                rizz += (len(arr) * k)
            else:
                rizz = perform_operation(arr, int(curr))
            print(rizz)
