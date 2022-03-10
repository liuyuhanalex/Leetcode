class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        k = 0
        s = list(s)
        while i < len(s):
            j = i
            while s[j] != ' ' and j != len(s)-1:
                j += 1
            s[i:j+1] = s[i:j+1][::-1]
            while s[j] == ' ' and j != len(s) - 1:
                j += 1
            i = j
            print(len(s), i, j, s)
        print(s)




if __name__ == '__main__':
    print(Solution().reverseWords('a good   example'))