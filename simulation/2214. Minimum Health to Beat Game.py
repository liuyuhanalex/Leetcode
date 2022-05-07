from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        sorted_damage = sorted(damage)
        start, end = 0, len(sorted_damage) - 1
        if armor == 0:
            return sum(damage) + 1
        while start < end:
            mid = start + (end - start) // 2
            if sorted_damage[mid] >= armor:
                end = mid
            else:
                start = mid + 1
        if armor < sorted_damage[start]:
            return sum(damage) - armor + 1
        return sum(damage) - sorted_damage[start] + 1





if __name__ == '__main__':
    #print(Solution().minimumHealth(damage = [2,5,3,4], armor = 7))
    #print(Solution().minimumHealth([2,7,4,3], 4))
    print(Solution().minimumHealth([3], 1))