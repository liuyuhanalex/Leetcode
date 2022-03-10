from typing import List


class Solution:
    def numRabbits1(self, answers: List[int]) -> int:
        hash_table = {}
        for i in answers:
            hash_table[i] = hash_table.get(i, 0) + 1
        total_num = 0
        for k, v in hash_table.items():
            if k == 0:
                total_num += v
                continue
            if v <= k+1:
                total_num += k+1
            else:
                while v > k + 1:
                    total_num += k + 1
                    v = v - k - 1
        return total_num

    def numRabbits(self, answers: List[int]) -> int:
        hash_table = {}
        for i in answers:
            hash_table[i] = hash_table.get(i, 0) + 1
        total_num = 0
        hash_list = [(k, v) for k, v in hash_table.items()]
        while len(hash_list) > 0:
            k, v = hash_list.pop(0)
            if k == 0:
                total_num += v
                continue
            if v <= k + 1:
                total_num += k+1
            else:
                total_num += k + 1
                hash_list.append((k, v-k-1))
        return total_num






if __name__ == '__main__':
    print(Solution().numRabbits([0, 0, 1, 1, 1]))