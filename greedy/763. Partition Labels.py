from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        all_al = set(list(s))
        res = []
        for w in all_al:
            start, end = 0, len(s)-1
            while s[start] != w or s[end]!=w:
                if s[start] != w:
                    start += 1
                if s[end] != w:
                    end -= 1
            res.append([start, end])
        sorted_res = sorted(res, key=lambda x: x[0])
        last = sorted_res.pop(0)
        total_res = [last]
        while sorted_res:
            [next_start, next_end] = sorted_res.pop(0)
            [this_start, this_end] = last
            if next_start < this_end:
                new_one = [this_start, max(next_end, this_end)]
                last = new_one
                total_res.pop()
                total_res.append(new_one)
            else:
                last = [next_start, next_end]
                total_res.append(last)
        return [i[1]-i[0]+1 for i in total_res]







if __name__ == '__main__':
    print(Solution().partitionLabels("caedbdedda"))