
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <=1:
            return x
        start, end = 0, x
        while True:
            pivot = start + (end-start)//2
            if pivot * pivot > x:
                end = pivot
            else:
                start = pivot
            if end - start == 1:
                return start





if __name__ == '__main__':
    print(Solution().mySqrt(x=8))