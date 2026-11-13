import random

readings = [round(random.uniform(0, 50), 2) for i in range(365)]

weekly_totals = []

for i in range(0, len(readings), 7):
    weekly_totals.append(sum(readings[i:i+7]))

maximum = max(readings)
minimum = min(readings)

print("Maximum rainfall:", maximum)
print("Maximum day:", readings.index(maximum) + 1)

print("Minimum rainfall:", minimum)
print("Minimum day:", readings.index(minimum) + 1)

moving_average = []

for i in range(len(readings) - 6):
    average = sum(readings[i:i+7]) / 7
    moving_average.append(round(average, 2))

print("First 5 weekly totals:", weekly_totals[:5])
print("First 5 moving averages:", moving_average[:5])

dry_days = []

for i in range(len(readings)):
    if readings[i] == 0:
        dry_days.append(i + 1)

print("Dry days:", dry_days)
print("Total dry days:", len(dry_days))
