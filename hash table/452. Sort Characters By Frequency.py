
class Solution:
    def frequencySort(self, s: str) -> str:
        hash_table = {}
        for i in s:
            hash_table[i] = hash_table.get(i, 0) + 1
        sorted_hash = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for i in sorted_hash:
            char, num = i
            res += char * num
        return res



if __name__ == '__main__':
    Solution().frequencySort(s = "tree")