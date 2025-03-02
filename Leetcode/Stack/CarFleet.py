from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]):
        position_speed = []
        n = len(position)

        for i in range(n):
            position_speed.append((position[i], speed[i]))
        
        position_speed.sort(key=lambda x:x[0], reversed=True)
        