class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while target != 1:
            if maxDoubles > 0:
                if target % 2 == 0:
                    target = target//2
                    maxDoubles -= 1
                else:
                    target -= 1
                cnt += 1
            else:
                cnt += target - 1
                break
        return cnt


if __name__ == '__main__':
    print(Solution().minMoves(target = 19, maxDoubles = 2))
