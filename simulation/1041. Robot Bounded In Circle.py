class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        length = len(instructions)
        instructions = instructions*4
        pos = [0, 0]
        cur_direction = 0
        direction_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for index, i in enumerate(instructions):
            if i == 'G':
                pos[0] += direction_list[cur_direction][0]
                pos[1] += direction_list[cur_direction][1]
            elif i == 'L':
                cur_direction -= 1
                if cur_direction < 0:
                    cur_direction = 3
            elif i == 'R':
                cur_direction += 1
                if cur_direction > 3:
                    cur_direction = 0
            if pos == [0, 0] and (index+1)%length == 0:
                return True
        return False


if __name__ == '__main__':
    print(Solution().isRobotBounded(instructions = "GL"))