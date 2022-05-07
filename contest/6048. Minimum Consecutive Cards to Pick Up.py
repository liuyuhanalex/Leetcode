from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hash_table = {}
        min_len = len(cards) + 1
        for index, i in enumerate(cards):
            last = hash_table.get(i, index)
            dis = index - last + 1
            hash_table[i] = index
            if dis > 1 and dis < min_len:
                min_len = dis
        return min_len if min_len < len(cards) + 1 else -1


if __name__ == '__main__':
    print(Solution().minimumCardPickup(cards = [3,4,2,3,4,7]))
