
junctions = [
    {
        "Junction ID": "J101",
        "Vehicle Count": 1200,
        "Average Speed": 40,
        "Accident Count": 5,
        "Signal Delay": 15,
        "Pollution Index": 90,
        "Peak Hour Traffic": 1000
    },
    {
        "Junction ID": "J102",
        "Vehicle Count": 800,
        "Average Speed": 50,
        "Accident Count": 2,
        "Signal Delay": 10,
        "Pollution Index": 60,
        "Peak Hour Traffic": 700
    },
    {
        "Junction ID": "J103",
        "Vehicle Count": 1500,
        "Average Speed": 35,
        "Accident Count": 7,
        "Signal Delay": 20,
        "Pollution Index": 110,
        "Peak Hour Traffic": 1300
    }
]

# 1. Calculate Congestion Score

print("========== CONGESTION SCORE ==========")

for j in junctions:
    j["Congestion Score"] = (j["Vehicle Count"] * j["Signal Delay"]) / j["Average Speed"]
    print(j["Junction ID"], "=", round(j["Congestion Score"], 2))

# 2. Rank Junctions

junctions.sort(key=lambda x: x["Congestion Score"], reverse=True)

print("\n========== JUNCTION RANKING ==========")

rank = 1

for j in junctions:
    print(rank, ".", j["Junction ID"], "-", round(j["Congestion Score"], 2))
    rank += 1

# 3. Identify Accident-Prone Areas

print("\n========== ACCIDENT-PRONE AREAS ==========")

found = False

for j in junctions:
    if j["Accident Count"] >= 5:
        print(j["Junction ID"])
        found = True

if not found:
    print("No Accident-Prone Areas")

# 4. Display Heavily Polluted Junctions

print("\n========== HEAVILY POLLUTED JUNCTIONS ==========")

found = False

for j in junctions:
    if j["Pollution Index"] > 80:
        print(j["Junction ID"])
        found = True

if not found:
    print("No Heavily Polluted Junctions")

# 5. Calculate City Average Congestion

total = 0

for j in junctions:
    total += j["Congestion Score"]

average = total / len(junctions)

print("\n========== CITY AVERAGE CONGESTION ==========")
print(round(average, 2))

# 6. Find the Busiest Junction

busy = junctions[0]

for j in junctions:
    if j["Vehicle Count"] > busy["Vehicle Count"]:
        busy = j

print("\n========== BUSIEST JUNCTION ==========")
print(busy["Junction ID"], "-", busy["Vehicle Count"], "Vehicles")

# 7. Generate Traffic Alerts

print("\n========== TRAFFIC ALERTS ==========")

alerts = []

for j in junctions:
    if j["Congestion Score"] > 500:
        alert = "Heavy Traffic at " + j["Junction ID"]
        alerts.append(alert)
        print(alert)

# 8. Save Alerts into File

file = open("traffic_alerts.txt", "w")

for alert in alerts:
    file.write(alert)
    file.write("\n")

file.close()

print("\nTraffic Alerts Saved Successfully")

# 9. Sort Junctions

print("\n========== SORTED JUNCTIONS ==========")

for j in junctions:
    print(j["Junction ID"], "-", round(j["Congestion Score"], 2))

# 10. Display Top 5 Congestion Points

print("\n========== TOP 5 CONGESTION POINTS ==========")

count = 0

for j in junctions:
    if count < 5:
        print(j["Junction ID"], "-", round(j["Congestion Score"], 2))
        count += 1

# Read Alerts File

print("\n========== READING TRAFFIC ALERTS ==========\n")

file = open("traffic_alerts.txt", "r")
print(file.read())
file.close()
