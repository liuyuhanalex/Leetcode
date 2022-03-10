from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hash_table = {}
        for i in trips:
            hash_table[i[1]] = hash_table.get(i[1], 0) + i[0]
            hash_table[i[2]] = hash_table.get(i[2], 0) - i[0]
        total_person = 0
        for i in sorted(hash_table.keys()):
            total_person += hash_table.get(i)
            if total_person > capacity:
                return False
        return True



if __name__ == '__main__':
    print(Solution().carPooling(trips=[[4,5,6],[6,4,7],[4,3,5],[2,3,5]], capacity=13))
