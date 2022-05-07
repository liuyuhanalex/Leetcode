

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_hash, t_hash = {}, {}
        for i in s:
            s_hash[i] = s_hash.get(i, 0) + 1
        for i in t:
            t_hash[i] = t_hash.get(i, 0) + 1
        cnt = 0
        for k in set(s_hash.keys()).union(set(t_hash.keys())):
            cnt += abs(s_hash.get(k,0) - t_hash.get(k, 0))
        return cnt






if __name__ == '__main__':
    Solution().minSteps(s = "leetcode", t = "coats")