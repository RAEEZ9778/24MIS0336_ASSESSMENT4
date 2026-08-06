
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

# 1. Calculate Machine Efficiency

print("Machine Efficiency")

for m in machines:
    efficiency = m["Units Produced"] / (m["Operating Hours"] - m["Downtime"])
    m["Efficiency"] = efficiency
    print(m["Machine ID"], "=", round(efficiency, 2))

# 2. Calculate Production Cost Per Unit

print("\nProduction Cost Per Unit")

for m in machines:
    cost = m["Maintenance Cost"] / m["Units Produced"]
    m["Cost Per Unit"] = cost
    print(m["Machine ID"], "=", round(cost, 2))

# 3. Identify Inefficient Machines

print("\nInefficient Machines")

for m in machines:
    if m["Efficiency"] < 25:
        print(m["Machine ID"])

# 4. Machine with Highest Maintenance Cost

highest = machines[0]

for m in machines:
    if m["Maintenance Cost"] > highest["Maintenance Cost"]:
        highest = m

print("\nHighest Maintenance Cost")
print(highest["Machine ID"], "-", highest["Maintenance Cost"])

# 5. Plant-wise Efficiency

print("\nPlant-wise Efficiency")

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

# 6. Machines Requiring Preventive Maintenance

print("\nMachines Requiring Preventive Maintenance")

for m in machines:
    if m["Maintenance Cost"] > 25000:
        print(m["Machine ID"])

# 7. Sort Machines by Efficiency

machines.sort(key=lambda x: x["Efficiency"], reverse=True)

print("\nMachines Sorted by Efficiency")

rank = 1

for m in machines:
    print(rank, ".", m["Machine ID"], "-", round(m["Efficiency"], 2))
    rank += 1

# 8. Generate Maintenance Report

print("\nMaintenance Report")

for m in machines:
    print(m)

# 9. Save Report to File

file = open("maintenance_report.txt", "w")

for m in machines:
    file.write(str(m))
    file.write("\n")

file.close()

print("\nMaintenance Report Saved Successfully")

# 10. Read the Report

print("\nReading Maintenance Report")

file = open("maintenance_report.txt", "r")

print(file.read())

file.close()
