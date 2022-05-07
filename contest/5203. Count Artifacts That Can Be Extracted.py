from typing import List

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        cnt = 0
        for i in artifacts:
            pos1 = [i[0], i[1]]
            pos2 = [i[2], i[3]]
            flag = True
            for i in range(pos1[0], pos2[0]+1):
                for j in range(pos1[1], pos2[1]+1):
                    if [i, j] not in dig:
                        flag = False
                        break
            if flag:
                cnt += 1
        return cnt
