

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while n > 0:
            count += (n & 1)
        return count == 1



if __name__ == '__main__':
    print(Solution().isPowerOfTwo(17))