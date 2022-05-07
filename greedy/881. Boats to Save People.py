from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cnt = 0
        people_sorted = sorted(people, reverse=True)
        end_pointer = len(people) - 1
        start_pointer = 0
        while start_pointer <= end_pointer:
            if people_sorted[start_pointer] + people_sorted[end_pointer] <= limit:
                end_pointer -= 1
            cnt += 1
            start_pointer += 1
        return cnt


if __name__ == '__main__':
    Solution().numRescueBoats(people = [3,5,3,4], limit = 5)