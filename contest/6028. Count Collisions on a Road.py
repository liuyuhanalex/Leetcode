

class Solution:
    def countCollisions(self, directions: str) -> int:
        cnt = 0
        directions = list(directions)
        for index, i in enumerate(directions):
            print(directions, cnt)
            if index >= 1:
                if i == 'L':
                    if directions[index-1] == 'S':
                        cnt += 1
                        directions[index] = 'S'
                    elif directions[index - 1] == 'R':
                        cnt += 2
                        directions[index] = 'S'
                elif i == 'S':
                    if directions[index-1] == 'R':
                        cnt += 1
                        directions[index] = 'S'
        for index, i in enumerate(directions):
            if index >= 1:
                if i == 'L':
                    if directions[index-1] == 'S':
                        cnt += 1
                        directions[index] = 'S'
                    elif directions[index - 1] == 'R':
                        cnt += 2
                        directions[index] = 'S'
                elif i == 'S':
                    if directions[index-1] == 'R':
                        cnt += 1
                        directions[index] = 'S'
        return cnt





if __name__ == '__main__':
    #Solution().countCollisions(directions = "RLRSLL")
    #print(Solution().countCollisions("LLRR"))
    print(Solution().countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"))