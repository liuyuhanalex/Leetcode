class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        nums = [abs(ord(m) - ord(n)) for m, n in zip(s, t)]
        N = len(nums)
        left, right = 0, 0
        sums = 0
        res = 0
        while right < N:
            sums += nums[right]
            while sums > maxCost:
                sums -= nums[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == '__main__':
    print(Solution().equalSubstring(s = "krrgw", t= "zjxss", maxCost = 19))