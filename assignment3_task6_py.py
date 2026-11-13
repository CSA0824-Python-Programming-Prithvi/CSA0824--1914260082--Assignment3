trains = {
    12601: {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:15"),
            ("Katpadi", "08:00", "08:05"),
            ("Bangalore", "11:00", "11:15")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    12602: {
        "name": "Bangalore Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Katpadi", "09:00", "09:05"),
            ("Bangalore", "12:00", "12:15")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    12603: {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Salem", "11:00", "11:05"),
            ("Coimbatore", "13:00", "13:15")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    12604: {
        "name": "Madurai Express",
        "stops": [
            ("Chennai", "09:00", "09:10"),
            ("Trichy", "12:00", "12:05"),
            ("Madurai", "14:00", "14:15")
        ],
        "days": {"Wednesday", "Friday", "Sunday"}
    },

    12605: {
        "name": "Salem Express",
        "stops": [
            ("Chennai", "10:00", "10:10"),
            ("Katpadi", "12:00", "12:05"),
            ("Salem", "14:00", "14:15")
        ],
        "days": {"Monday", "Thursday", "Saturday"}
    }
}

station = input("Enter station: ")
day = input("Enter day: ")

result = []

for number, details in trains.items():

    if day in details["days"]:

        for stop in details["stops"]:

            if stop[0].lower() == station.lower():
                result.append((stop[2], number, details["name"]))
                break

result.sort(key=lambda x: x[0])

print("\nAvailable trains:")

if result:
    for departure, number, name in result:
        print(number, name, "Departure:", departure)
else:
    print("No trains available")
