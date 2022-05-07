from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        p_hash = {}
        all_players = set()
        for i in matches:
            p_hash[i[1]] = p_hash.get(i[1], 0) + 1
            all_players.add(i[0])
            all_players.add(i[1])
        return [sorted(list(all_players - p_hash.keys())), sorted([i[0] for i in p_hash.items() if i[1] == 1])]





if __name__ == '__main__':
    print(Solution().findWinners(matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]))