class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hash_table1, hash_table2 = {}, {}
        for i in word1:
            hash_table1[i] = hash_table1.get(i, 0) + 1
        for i in word2:
            hash_table2[i] = hash_table2.get(i, 0) + 1
        if hash_table1 == hash_table2:
            return True
        if hash_table1.keys() != hash_table2.keys():
            return False
        if sorted(list(hash_table2.values())) == sorted(list(hash_table1.values())):
            return True
        return False


if __name__ == '__main__':
    #print(Solution().closeStrings(word1 = "cabbba", word2 = "abbccc"))
    print(Solution().closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))