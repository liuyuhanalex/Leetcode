from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        house_pointer, heat_pointer = 0, 0
        radius = 0
        while house_pointer < len(houses):
            if heat_pointer < len(heaters) -1 and abs(houses[house_pointer] - heaters[heat_pointer]) > abs(houses[house_pointer] - heaters[heat_pointer+1]):
                heat_pointer += 1
            distance = abs(houses[house_pointer] - heaters[heat_pointer])
            if distance > radius:
                radius = distance
            house_pointer += 1
        return radius



if __name__ == '__main__':
    Solution().findRadius(houses = [1,5], heaters = [2])