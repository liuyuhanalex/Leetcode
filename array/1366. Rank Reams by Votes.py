from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]
        hash_table = {}
        for i in votes:
            for index, v in enumerate(i):
                hash_table.setdefault(v, []).append(index)
        res = []
        for k, v in hash_table.items():
            v_sorted = ''.join([str(i) for i in sorted(v)])
            res.append((k, v_sorted))
        sorted_res = sorted(res, key=lambda x: (x[1], x[0]))
        return ''.join([i[0] for i in sorted_res])

    def rankTeams1(self, votes: List[str]) -> str:
        s = {}
        if len(votes) == 1:
            return votes[0]
        for v in votes:
            for inx, i in enumerate(v):
                if i not in s:
                    s[i] = [inx]
                else:
                    s[i].append(inx)
        for k, v in s.items():
            # print(k, v, sorted(s[k]))
            s[k] = ''.join([str(i) for i in sorted(s[k])])
        sorted_res = sorted(s.items(), key=lambda x: (x[1], x[0]))
        print(s, sorted_res, ''.join([k[0] for k in sorted_res]))
        print(sorted_res, ''.join([k[0] for k in sorted_res]))
        return ''.join([k[0] for k in sorted_res])



if __name__ == '__main__':
    pass