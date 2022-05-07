

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, pointer = 0, 0
        while i < len(abbr):
            num = ''
            if abbr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                while i < len(abbr) and abbr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    num += abbr[i]
                    i += 1
                num = int(num)
                pointer += num
            else:
                if abbr[i] == word[pointer]:
                    i += 1
                    pointer += 1
                else:
                    return False
        return pointer == len(word) and i == len(abbr)






if __name__ == '__main__':
    #print(Solution().validWordAbbreviation(word = "internationalization", abbr = "i12iz4n"))
    print(Solution().validWordAbbreviation("internationalization", "i5a11o1"))