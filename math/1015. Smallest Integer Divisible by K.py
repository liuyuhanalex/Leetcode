class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if set(str(k)) == {'1'}:
            return len(str(k))
        length = len(str(k))
        start_num = int('1' * length)
        remainder = start_num
        remainder_set = set()
        while True:
            if start_num < k:
                start_num = int('1' * (length + 1))
                remainder = start_num
                if remainder % k == 0:
                    return length
                length += 1
            else:
                if remainder % k == 0:
                    print('i am here')
                    return length
                remainder = remainder%k * 10 + 1
                length += 1
                if remainder % k == 0:
                    return length
                else:
                    if remainder not in remainder_set:
                        remainder_set.add(remainder)
                    else:
                        return -1





if __name__ == '__main__':
    print(Solution().smallestRepunitDivByK(11))