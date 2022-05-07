class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            num_list = list(str(-num))
            after_sorted = sorted(num_list, reverse=True)
            return - int(''.join(after_sorted))
        else:
            num_list = sorted(list(str(num)))
            for i in range(len(num_list)):
                if num_list[i] != '0' and i == 0:
                    return int(''.join(num_list))
                else:
                    if num_list[i] != '0' :
                        num_list[0] = num_list[i]
                        num_list[i] = '0'
                        return int(''.join(num_list))
        return 0


if __name__ == '__main__':
    print(Solution().smallestNumber(-7605))