n = int(input())
x = y = z = 0

for i in range(n):
    x1, y1, z1 = map(int, input().split(" "))
    x += x1
    y += y1
    z += z1

if x or y or z:
    print("NO")
else:
    print("YES")

# TC: O(n) where n is the number of force vectors given to us
# SC: O(1)