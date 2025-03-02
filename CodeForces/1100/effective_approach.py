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
