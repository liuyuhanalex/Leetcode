
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        pos = True if n > 0 else False
        n = abs(n)
        res_pos = 1 if n%2 == 0 or x > 0 else -1
        print(res_pos)
        x = x if x>=0 else abs(1/x)
        print(x)
        while -10000 <= res <= 10000:
            if round(res, 5) == 0:
                break
            if n >= 1:
                n -= 1
                last_res = res
                res *= x
                if last_res == res:
                    break
            else:
                break
        return round(res_pos*res, 5)


if __name__ == '__main__':
    print(Solution().myPow(x=-13.00000, n=3))