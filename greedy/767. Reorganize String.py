from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        counter_list = sorted([(v, k) for k, v in counter.items()])
        res = '0'
        while len(counter_list) > 0:
            counter_list = sorted(counter_list)
            ele = counter_list[-1][1]
            if ele != res[-1]:
                res += ele
                (count, element) = counter_list.pop()
                if count - 1 == 0:
                    pass
                else:
                    counter_list.append((count-1, element))
            else:
                if len(counter_list) < 2:
                    return ''
                (next_count, next_element) = counter_list.pop(-2)
                res += next_element
                if next_count - 1 == 0:
                    pass
                else:
                    counter_list.append((next_count-1, next_element))
        return res[1:]







if __name__ == '__main__':
    Solution().reorganizeString(s = "aaab")