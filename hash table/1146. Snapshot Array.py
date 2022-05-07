from copy import copy

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_hash = {i: (0, 0) for i in range(length)}
        self.total_snap = -1
        self.record_hash = {i: 0 for i in range(length)}

    def set(self, index: int, val: int) -> None:
        record_list = self.snap_hash[index]
        if self.record_hash[index] == self.total_snap:
            record_list.pop()
        else:
            self.record_hash[index] = self.total_snap
        record_list.append((self.total_snap, val))
        self.snap_hash[index] = record_list

    def snap(self) -> int:
        self.total_snap += 1
        return self.total_snap

    def get(self, index: int, snap_id: int) -> int:
        search_list = self.snap_hash.get(index)
        return self.binary_search(search_list, snap_id)

    def binary_search(self, search_list, snap_id):
        search_list_1 = [i[0] for i in search_list]
        start, end = 0, len(search_list_1) - 1
        while start < end:
            mid = start + (end - start) // 2
            if search_list_1[mid] >= snap_id:
                start = mid + 1
            else:
                end = mid
        return search_list[start][1]



if __name__ == '__main__':
    print(SnapshotArray(5).binary_search([(0, 0), (2, 4), (3, 12)], 1))