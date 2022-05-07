class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        c_h, c_m = [int(i) for i in current.split(':')]
        cor_h, cor_m = [int(i) for i in correct.split(':')]
        cnt = 0
        if cor_m >= c_m:
            cnt += cor_h - c_h
            m_diff = cor_m - c_m
        else:
            cnt += cor_h - c_h - 1
            m_diff = 60 - c_m + cor_m
        f_cnt = m_diff // 15
        remain = m_diff % 15
        s_cnt = remain // 5
        remain = remain % 5
        return cnt + f_cnt + s_cnt + remain




if __name__ == '__main__':
    # 1, 5, 15, or 60
    print(Solution().convertTime(current = "09:41", correct = "10:34"))