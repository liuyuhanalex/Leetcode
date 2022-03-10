class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memory_table = {}
        res = []
        for i in range(lo, hi+1):
            cnt = 0
            num = i
            m_list = []
            flag = False
            while num != 1:
                if memory_table.get(num) is not None:
                    flag = True
                    res.append((i, cnt + memory_table.get(num)))
                    cnt = cnt + memory_table.get(num)
                    break
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                cnt += 1
                m_list.append((num, cnt))
            for j in m_list:
                memory_table[j[0]] = cnt - j[1]
            if not flag:
                res.append((i, cnt))
        res = sorted(res, key=lambda x: (x[1], x[0]))
        return res[k-1][0]


if __name__ == '__main__':
    Solution().getKth(lo=10, hi=20, k=5)