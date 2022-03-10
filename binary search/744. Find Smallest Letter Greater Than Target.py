from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        if target >= letters[-1]:
            return letters[0]
        while start < end:
            mid = start + (end-start)//2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return letters[end]




if __name__ == '__main__':
    print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="a"))