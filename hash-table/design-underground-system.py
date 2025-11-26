class UndergroundSystem:
    """
    example 1 = [
        "UndergroundSystem",[],
        "checkIn",[45,"Leyton",3],
        "checkIn",[32,"Paradise",8],
        "checkIn",[27,"Leyton",10],
        "checkOut",[45,"Waterloo",15],
        "checkOut",[27,"Waterloo",20],
        "checkOut",[32,"Cambridge",22],
        "getAverageTime",["Paradise","Cambridge"], --> 22-8=14
        "getAverageTime",["Leyton","Waterloo"], --> ((15-3) + (20-10)) / 2 = 11
        "checkIn",[10,"Leyton",24],
        "getAverageTime",["Leyton","Waterloo"], --> ((15-3) + (20-10)) / 2 = 11
        "checkOut",[10,"Waterloo",38],
        "getAverageTime",["Leyton","Waterloo"], --> ((15-3) + (20-10) + (38-24)) / 3 = 12
    ]
    
    1. from start to "getAverageTime",["Paradise","Cambridge"] and "getAverageTime",["Leyton","Waterloo"]:
        hashmap = {
            45: [3-Leyton,15-Waterloo]
            32: [8-Paradise,22-Cambridge]
            27: [10-Leyton,20-Waterloo]
        }
        time_map = {
            Leyton: {
                Waterloo: {cnt: 2, total_time: 22}
            },
            Paradise: {
                Cambridge: {cnt: 1, total_time: 14}
            }
        }
    2. "checkIn",[10,"Leyton",24],
        hashmap = {
            10: 24,Leyton
        }
        "getAverageTime",["Leyton","Waterloo"]
            - get data from time_map
    3. "checkOut",[10,"Waterloo",38],
        hashmap = {
            10: 24,Leyton # exist
        }
        -> new data to store: Leyton->Waterloo (t=38-24=14)
        -> update time_map
            time_map = {
                Leyton: {
                    Waterloo: {cnt: 3, total_time: 36}
                },
                Paradise: {
                    Cambridge: {cnt: 1, total_time: 14}
                }
            }
        -> del hashmap[24]
    """

    def __init__(self):
        self.user_map = {}
        self.time_map = defaultdict(lambda: defaultdict(lambda: [0,0]))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.user_map:
            raise Error("MUST checkIn first")
        
        self.user_map[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.user_map:
            raise Error("MUST checkOut first")

        station_in, time_in = self.user_map[id]
        travel_time = t - time_in
        # update new time + count
        total_cnt, total_time = self.time_map[station_in][stationName]
        self.time_map[station_in][stationName] = [total_cnt+1, total_time + travel_time]

        del self.user_map[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_cnt, total_time = self.time_map[startStation][endStation]
        return total_time / total_cnt

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)