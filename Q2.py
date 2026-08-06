
machines = [
    {
        "Machine ID": "M101",
        "Plant Name": "Plant A",
        "Operating Hours": 200,
        "Downtime": 20,
        "Energy Consumption": 1000,
        "Units Produced": 5000,
        "Maintenance Cost": 25000
    },
    {
        "Machine ID": "M102",
        "Plant Name": "Plant B",
        "Operating Hours": 180,
        "Downtime": 30,
        "Energy Consumption": 900,
        "Units Produced": 4000,
        "Maintenance Cost": 30000
    },
    {
        "Machine ID": "M103",
        "Plant Name": "Plant A",
        "Operating Hours": 220,
        "Downtime": 10,
        "Energy Consumption": 1100,
        "Units Produced": 6000,
        "Maintenance Cost": 20000
    }
]


print("========== MACHINE EFFICIENCY ==========")

for m in machines:
    m["Efficiency"] = m["Units Produced"] / (m["Operating Hours"] - m["Downtime"])
    print(m["Machine ID"], "=", round(m["Efficiency"], 2))


print("\n========== PRODUCTION COST PER UNIT ==========")

for m in machines:
    m["Cost Per Unit"] = m["Maintenance Cost"] / m["Units Produced"]
    print(m["Machine ID"], "=", round(m["Cost Per Unit"], 2))


print("\n========== INEFFICIENT MACHINES ==========")

found = False

for m in machines:
    if m["Efficiency"] < 25:
        print(m["Machine ID"])
        found = True

if not found:
    print("No Inefficient Machines")


highest = machines[0]

for m in machines:
    if m["Maintenance Cost"] > highest["Maintenance Cost"]:
        highest = m

print("\n========== HIGHEST MAINTENANCE COST ==========")
print("Machine ID :", highest["Machine ID"])
print("Maintenance Cost :", highest["Maintenance Cost"])
print("\n========== PLANT-WISE EFFICIENCY ==========")

plants = {}

for m in machines:
    plant = m["Plant Name"]

    if plant not in plants:
        plants[plant] = [0, 0]

    plants[plant][0] += m["Efficiency"]
    plants[plant][1] += 1

for plant in plants:
    average = plants[plant][0] / plants[plant][1]
    print(plant, "=", round(average, 2))



print("\n========== PREVENTIVE MAINTENANCE ==========")

for m in machines:
    if m["Maintenance Cost"] > 25000:
        print(m["Machine ID"])


machines.sort(key=lambda x: x["Efficiency"], reverse=True)

print("\n========== MACHINES SORTED BY EFFICIENCY ==========")

rank = 1

for m in machines:
    print(rank, ".", m["Machine ID"], "-", round(m["Efficiency"], 2))
    rank += 1


print("\n========== MAINTENANCE REPORT ==========")

for m in machines:
    print("---------------------------------------")
    print("Machine ID        :", m["Machine ID"])
    print("Plant Name        :", m["Plant Name"])
    print("Efficiency        :", round(m["Efficiency"], 2))
    print("Cost Per Unit     :", round(m["Cost Per Unit"], 2))
    print("Maintenance Cost  :", m["Maintenance Cost"])


file = open("maintenance_report.txt", "w")

for m in machines:
    file.write("---------------------------------------\n")
    file.write("Machine ID       : " + m["Machine ID"] + "\n")
    file.write("Plant Name       : " + m["Plant Name"] + "\n")
    file.write("Efficiency       : " + str(round(m["Efficiency"], 2)) + "\n")
    file.write("Cost Per Unit    : " + str(round(m["Cost Per Unit"], 2)) + "\n")
    file.write("Maintenance Cost : " + str(m["Maintenance Cost"]) + "\n")

file.close()

print("\nMaintenance Report Saved Successfully")


print("\n========== READING MAINTENANCE REPORT ==========\n")

file = open("maintenance_report.txt", "r")
print(file.read())
file.close()