class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        re_set = set()
        while self.get_sum(n) != 1:
            n = self.get_sum(n)
            if n in re_set:
                return False
            re_set.add(n)
        return True

    def get_sum(self, n):
        total = 0
        for i in str(n):
            total += int(i) * int(i)
        return total



if __name__ == '__main__':
    print(Solution().isHappy(2))