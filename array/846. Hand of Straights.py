from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        sorted_hand = sorted(hand)
        while sorted_hand:
            num = sorted_hand.pop(0)
            for i in range(1, groupSize):
                if num + i not in sorted_hand:
                    return False
                else:
                    sorted_hand.remove(num + i)
        return True






if __name__ == '__main__':
    print(Solution().isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))