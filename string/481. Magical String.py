class Solution:
    def magicalString(self, n: int) -> int:
        start_str = '122'
        new_string = ''
        sign = 1
        for i in range(n):
            if len(new_string) >= n:
                new_string = new_string[:n]
                return new_string.count('1')
            if i <= 2:
                num = int(start_str[i])
            else:
                num = int(new_string[i])
            if sign == 1:
                new_string += '1' * num
            else:
                new_string += '2' * num
            sign = 1 - sign

    def magicalString1(self, n: int) -> int:
        start_str = '122'
        pointer1, pointer2 = 2, 2
        sign = 1
        while pointer2 < n:
            if sign == 0:
                start_str += int(start_str[pointer1]) * '2'
            else:
                start_str += int(start_str[pointer1]) * '1'
            pointer1 += 1
            pointer2 += int(start_str[pointer1])
            sign = 1 - sign
        start_str = start_str[:n+1]
        return start_str.count('1')

    def magicalString2(self, n: int) -> int:
        start_str = '122'
        pointer1, pointer2 = 2, 2
        sign = 1
        total_cnt, ones_cnt = 3, 1
        while pointer2 < n:
            if sign == 0:
                start_str += int(start_str[pointer1]) * '2'
                total_cnt += int(start_str[pointer1])
            else:
                start_str += int(start_str[pointer1]) * '1'
                total_cnt += int(start_str[pointer1])
                if total_cnt >= n:
                    ones_cnt += total_cnt - n
                else:
                    ones_cnt += int(start_str[pointer1])
            pointer1 += 1
            pointer2 += int(start_str[pointer1])
            sign = 1 - sign
        return ones_cnt





if __name__ == '__main__':
    print(Solution().magicalString1(n = 4))