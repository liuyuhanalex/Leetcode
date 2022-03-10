from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = [start]
        level = 0
        seen = set()
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                pop_str = queue.pop(0)
                if pop_str == end:
                    return level
                for index, char in enumerate(pop_str):
                    for j in ['A', 'C', 'G', 'T']:
                        if char != j:
                            new_str = pop_str[:index] + j + pop_str[index+1:]
                            if new_str in bank and new_str not in seen:
                                queue.append(new_str)
                                seen.add(new_str)
            level += 1
        return -1


if __name__ == '__main__':
    print(Solution().minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))