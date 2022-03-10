from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        result = [True] * n
        result[0], result[1] = False, False
        sqrt_int = int(sqrt(n))
        for i in range(2, sqrt_int + 1):
            if result[i]:
                q = 2
                while q * i < n:
                    result[q*i] = False
                    q += 1
        return sum(result)



if __name__ == '__main__':
    print(Solution().countPrimes(10))