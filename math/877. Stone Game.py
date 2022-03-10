from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        sorted_piles = sorted(piles)
        alice_total  = 0
        for i in range(len(sorted_piles)):
            if i % 2 != 0:
                alice_total += sorted_piles[i]
        if alice_total > sum(piles) //2:
            return True
        return False



if __name__ == '__main__':
    print(Solution().stoneGame(piles = [5,3,4,5]))