class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag = False
        for index, i in enumerate(word):
            if flag is False and ord(i) >= ord('a'):
                flag = True
            if ord(i) < ord('a') and index > 0 and flag:
                return False
        return True



if __name__ == '__main__':
    print(Solution().detectCapitalUse(word = "FLAG"))