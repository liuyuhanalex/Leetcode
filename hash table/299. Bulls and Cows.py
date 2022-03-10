

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        s_list, g_list = {}, {}
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                if s_list.get(s) is not None:
                    num = s_list.get(s)
                    s_list[s] = num + 1
                else:
                    s_list[s] = 1
                if g_list.get(g) is not None:
                    num = g_list.get(g)
                    g_list[g] = num + 1
                else:
                    g_list[g] = 1
        for key, value in g_list.items():
            if s_list.get(key) is not None:
                cows += min(s_list.get(key), g_list.get(key))
        return str(bulls) + 'A' + str(cows) + 'B'


if __name__ == '__main__':
    print(Solution().getHint(secret="1123", guess="0111"))