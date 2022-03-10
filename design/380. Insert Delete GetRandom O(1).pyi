from random import randint

class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.arr_list = []


    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            self.arr_list = list(self.set)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            self.arr_list = list(self.set)
            return True
        return False


    def getRandom(self) -> int:
        ri = randint(0, len(self.arr_list)-1)
        return self.arr_list[ri]