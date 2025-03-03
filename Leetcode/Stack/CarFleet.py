from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda pair: pair[0], reverse=True)

        dist = []
        for i in range(len(pairs)):
            distance_to_target = (target - pairs[i][0])/pairs[i][1]
            dist.append(distance_to_target)
        
        stack = [dist[0]]
        for i in range(1, len(dist)):
            popped = stack.pop()
            if dist[i] <= popped:
                stack.append(max(dist[i], popped))
            else:
                stack.append(popped)
                stack.append(dist[i])

        return len(stack)                

if __name__ == "__main__":
    sol = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]

    print(sol.carFleet(target, position, speed))

# TC: O(NlogN), as sorting is the dominant term
# SC: O(N), to create our stack and the distance array