from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        arr2 = sorted(arr2)
        for i in arr1:
            left, right = 0, len(arr2)-1
            min_diff = 1000000
            while left <= right:
                mid = left + (right-left)//2
                if arr2[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1
                if abs(i - arr2[mid]) < min_diff:
                    min_diff = abs(i - arr2[mid])
            if min_diff > d:
                cnt += 1
        return cnt





if __name__ == '__main__':
    print(Solution().findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
    print(Solution().findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
    print(Solution().findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6))
    print(Solution().findTheDistanceValue([4,-3,-7,0,-10], [10], 69))