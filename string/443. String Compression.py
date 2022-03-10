from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        fixchar = chars[0]
        result =''
        count = 1
        for c in chars[1:]:
            if c != fixchar:
                if count == 1:
                    result += fixchar
                else:
                    result += fixchar + str(count)
                count = 1
                fixchar = c
            else:
                count += 1
        if count == 1:
            result += fixchar
        else:
            result += fixchar + str(count)
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)



if __name__ == '__main__':
    print(Solution().compress(["a"]))
