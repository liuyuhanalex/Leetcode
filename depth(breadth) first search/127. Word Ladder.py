from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = [beginWord]
        level = 1
        seen = set()
        while q:
            q_len = len(q)
            for _ in range(q_len):
                w = q.pop(0)
                if w == endWord:
                    return level
                for i in wordList:
                    cnt = 0
                    for w_1, w_2 in zip(w, i):
                        if cnt > 1:
                            break
                        if w_1 != w_2:
                            cnt += 1
                    if cnt == 1:
                        if i not in seen:
                            q.append(i)
                            seen.add(i)
            level += 1
        return 0




if __name__ == '__main__':
    print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog","lot","log","cog"]))
    print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))