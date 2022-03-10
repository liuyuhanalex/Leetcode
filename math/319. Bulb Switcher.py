class Solution:
    def bulbSwitch(self, n: int) -> int:
        p = 1
        count = 1
        while p < n:
            count += 1
            p = count * count
        return count-1 if count > 1 else 1



if __name__ == '__main__':
    print(Solution().bulbSwitch(1))
