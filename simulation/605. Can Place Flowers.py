from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        length = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, length+1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                cnt += 1
                if cnt >= n:
                    return True
        if cnt >= n:
            return True
        return False


if __name__ == '__main__':
    Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)