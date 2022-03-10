from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        sentence = sentence.split(' ')
        result = []
        for word in sentence:
            flag = False
            for index in range(len(word)):
                if word[:index] in dictionary:
                    result.append(word[:index])
                    flag = True
                    break
            if not flag:
                result.append(word)
        return ' '.join(result)


if __name__ == '__main__':
    Solution().replaceWords(dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")