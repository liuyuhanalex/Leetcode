from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total_hash = {i:0 for i in range(1, n+2)}
        for i in bookings:
            total_hash[i[0]] = total_hash.get(i[0]) + i[2]
            total_hash[i[1] + 1] = total_hash.get(i[1] + 1) - i[2]
        prefix_sum = 0
        res = []
        for i in sorted(total_hash.keys()):
            prefix_sum += total_hash.get(i)
            res.append(prefix_sum)
        return res[:-1]



if __name__ == '__main__':
    print(Solution().corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))