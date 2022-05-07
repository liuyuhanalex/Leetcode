
class HitCounter:

    def __init__(self):
        self.hit_map = {}

    def hit(self, timestamp: int) -> None:
        self.hit_map[timestamp] = self.hit_map.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        cnt = 0
        for i in self.hit_map.keys():
            if timestamp - 300 <= i <=timestamp:
                cnt += self.hit_map.get(i)
        return cnt

