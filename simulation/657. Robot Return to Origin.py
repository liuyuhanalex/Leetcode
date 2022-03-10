from collections import Counter

class Solution:
    def judgeCircle1(self, moves: str) -> bool:
        # 垃圾方法
        cur = [0, 0]
        hash_table = {
            'U': [0, 1],
            'D': [0, -1],
            'L': [-1, 0],
            'R': [1, 0]
        }
        for i in moves:
            x, y = hash_table.get(i)
            cur = [cur[0] + x, cur[1] + y]
        if cur == [0, 0]:
            return True
        return False

    def judgeCircle2(self, moves: str) -> bool:
        hash_table = {'U': 0, 'D':0, 'L':0, 'R':0}
        for i in moves:
            hash_table[i] = hash_table.get(i) + 1
        return hash_table.get('U') == hash_table.get('D') and hash_table.get('L') == hash_table.get('R')

    def judgeCircle3(self, moves: str) -> bool:
        counter = Counter(moves)
        return counter.get('U') == counter.get('D') and counter.get('R') == counter.get('L')

    def judgeCircle(self, moves: str) -> bool:
        c_x, c_y = 0, 0
        if len(moves) % 2 != 0:
            return False
        for i in moves:
            if i == 'D':
                c_x -= 1
            elif i == 'U':
                c_x += 1
            elif i == 'L':
                c_y -= 1
            else:
                c_y += 1
        return c_y == c_x == 0



if __name__ == '__main__':
    Solution().judgeCircle("UD")
