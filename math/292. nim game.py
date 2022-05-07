class Solution:
    def canWinNim(self, n: int) -> bool:
        remain = n % 4
        if remain == 0:
            return False
        return True