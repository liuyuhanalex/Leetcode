from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = {}
        for index, i in enumerate(wordsDict):
            self.dict.setdefault(i, []).append(index)

    def shortest(self, word1: str, word2: str) -> int:
        word1_pos = self.dict.get(word1)
        word2_pos = self.dict.get(word2)
        min_distance = 1000000
        for i in word1_pos:
            for j in word2_pos:
                if abs(i-j) < min_distance:
                    min_distance = abs(i-j)
        return min_distance


if __name__ == '__main__':
    wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(wd.shortest("coding", "makes"))