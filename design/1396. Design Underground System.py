class UndergroundSystem:

    def __init__(self):
        self.custom = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.custom[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.custom.get(id)
        duration = t - checkin_time
        if self.stations.get((checkin_station, stationName)) is None:
            self.stations[(checkin_station, stationName)] = [duration]
        else:
            self.stations[(checkin_station, stationName)] = self.stations.get((checkin_station, stationName)) + [duration]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        res_list = self.stations.get((startStation, endStation))
        return sum(res_list) / len(res_list)