class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        last = None
        count = 0
        list_n = [int(i) for i in list(str(n))]
        for i in list_n:
            if last is None:
                last = i
            else:
                if i < last:
                    break
                else:
                    last = i
            count += 1
        if count == len(list_n):
            return n

        for i in range(count-1, -1, -1):
            if i-1 == -1 or list_n[i] - 1 >= list_n[i-1]:
                list_n[i] = list_n[i] - 1
                i += 1
                while i < len(list_n):
                    list_n[i] = 9
                    i += 1
                break
        return int(''.join([str(i) for i in list_n]))





if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(121))
    #print(Solution().monotoneIncreasingDigits(56493))
    #print(Solution().monotoneIncreasingDigits(332))