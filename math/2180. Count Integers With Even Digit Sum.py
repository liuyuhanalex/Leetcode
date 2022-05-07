class Solution:
    def countEven(self, num: int) -> int:
        cnt = 0
        for i in range(1, num+1):
            s_i = str(i)
            if sum([int(i) for i in s_i]) %2 == 0:
                cnt += 1
        return cnt



if __name__ == '__main__':
    print(Solution().countEven(num = 30))