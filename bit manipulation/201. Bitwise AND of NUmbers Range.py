class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        total = left
        for i in range(left+1, right+1):
            total &= i
        print(total)



if __name__ == '__main__':
    Solution().rangeBitwiseAnd(left = 5, right = 7)