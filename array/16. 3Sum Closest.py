from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_array = sorted(nums)
        res = set()
        for index, i in enumerate(sorted_array):
            left, right = index + 1, len(sorted_array) - 1
            while left < right:
                total = i + sorted_array[left] + sorted_array[right]
                if total < target:
                    left += 1
                else:
                    right -= 1
                res.add(total)
        res = sorted(list(res))
        min_diff = 1000000
        result = 0
        for i in res:
            diff = abs(target - i)
            if diff < min_diff:
                min_diff = diff
                result = i
        return result

if __name__ == '__main__':
    print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))
