
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        cnt = 0
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            index_list = []
            for j in range(len(s)):
                if s[j] == i:
                    index_list.append(j + 1)
            index_list = [0] + index_list + [len(s)+1]
            if len(index_list) > 2:
                for id in range(1, len(index_list)-1):
                    cnt += (index_list[id] - index_list[id-1]) * (index_list[id+1] - index_list[id])
        return cnt




if __name__ == '__main__':
    print(Solution().uniqueLetterString("LEETCODE"))