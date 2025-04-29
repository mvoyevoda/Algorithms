class UndergroundSystem:
    def __init__(self):
        self.averages = {}  # {Station1-Station2: (average, total_trips_recorded)}
        self.enroute = {}  # {id: (station_name, departure_time)}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.enroute[str(id)] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        depart_station, depart_time = self.enroute[str(id)]
        arrive_station, arrive_time = stationName, t
        del self.enroute[str(id)]
        trip_label = f"{depart_station}-{arrive_station}"
        trip_duration = arrive_time - depart_time
        if trip_label in self.averages:
            average, trips = self.averages[trip_label]
            updated_average = (average * trips + trip_duration) / (trips+1)
            self.averages[trip_label] = (updated_average, trips+1)
        else:
            self.averages[trip_label] = (trip_duration, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averages[f"{startStation}-{endStation}"][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)