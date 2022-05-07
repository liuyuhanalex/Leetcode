from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        final = []
        for i in nums:
            num = ''
            for j in str(i):
                num += str(mapping[int(j)])
            final.append((int(num), i))
        return [i[1] for i in sorted(final, key=lambda x: x[0])]




if __name__ == '__main__':
    print(Solution().sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]))