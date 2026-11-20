timetable = {
    "12631": {
        "name": "Superfast Express",
        "stops": [
            ("StationA", "06:00", "06:05"),
            ("StationB", "08:10", "08:15"),
            ("StationC", "10:30", "10:35"),
            ("StationD", "12:00", "12:05")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },
    "12632": {
        "name": "Intercity Express",
        "stops": [
            ("StationB", "07:00", "07:05"),
            ("StationC", "09:15", "09:20"),
            ("StationE", "11:40", "11:45")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },
    "12633": {
        "name": "Passenger Train",
        "stops": [
            ("StationA", "05:00", "05:10"),
            ("StationB", "06:30", "06:35"),
            ("StationC", "08:00", "08:05"),
            ("StationF", "10:00", "10:05")
        ],
        "days": {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
    },
    "12634": {
        "name": "Express Special",
        "stops": [
            ("StationC", "12:00", "12:05"),
            ("StationD", "13:30", "13:35"),
            ("StationE", "15:00", "15:05")
        ],
        "days": {"Friday", "Sunday"}
    },
    "12635": {
        "name": "Night Mail",
        "stops": [
            ("StationA", "20:00", "20:05"),
            ("StationC", "23:00", "23:05"),
            ("StationF", "02:00", "02:05")
        ],
        "days": {"Monday", "Wednesday", "Saturday"}
    }
}

def find_trains_at_station_on_day(tt, station_name, day_name):
    result = []
    for train_no, data in tt.items():
        if day_name in data["days"]:
            for stop in data["stops"]:
                if stop[0] == station_name:
                    result.append((train_no, data["name"], stop[2]))
                    break
    return sorted(result, key=lambda x: x[2])

print("Trains stopping at StationC on Monday:")
for t in find_trains_at_station_on_day(timetable, "StationC", "Monday"):
    print(t)
