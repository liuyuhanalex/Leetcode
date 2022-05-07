from typing import List


class ATM:

    def __init__(self):
        self.banknotes = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}
        self.list = [500, 200, 100, 50, 20]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, j in zip(banknotesCount, reversed(self.list)):
            self.banknotes[j] = self.banknotes[j] + i


    def withdraw(self, amount: int) -> List[int]:
        final_list = [0 for _ in range(5)]
        for i in self.list:
            num = amount // i
            amount = amount % i
            if num >= 3:
                return [-1]
            final_list.append(num)
        if amount !=0 :
            return [-1]
        return reversed(final_list)