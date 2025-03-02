n = int(input())
arr = list(map(int, input().split(" ")))
seen = dict()
vasya = petya = 0

for i in range(n):
    seen[arr[i]] = i

query_number = int(input())
queries = list(map(int, input().split(" ")))
for q in queries:
    vasya += (seen[q] + 1)
    petya += n - seen[q]

print(vasya, petya)

# TC: O(n + m) where n, m is the number of values in our array and m is the number of queries
# SC: O(n), not including the input arrays: the dictionary to manage our values and their indices for quick lookup
