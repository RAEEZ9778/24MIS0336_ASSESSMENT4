
faculty = [
    {
        "Faculty ID": 101,
        "Faculty Name": "Alice",
        "Department": "CSE",
        "Publications": 40,
        "H-index": 18,
        "Budget": 120000,
        "Collaboration": 80
    },
    {
        "Faculty ID": 102,
        "Faculty Name": "Bob",
        "Department": "ECE",
        "Publications": 30,
        "H-index": 15,
        "Budget": 95000,
        "Collaboration": 70
    },
    {
        "Faculty ID": 103,
        "Faculty Name": "Charlie",
        "Department": "IT",
        "Publications": 50,
        "H-index": 22,
        "Budget": 150000,
        "Collaboration": 90
    }
]
print("Research Scores")

for f in faculty:
    score = (0.4 * f["Publications"]) + (0.3 * f["H-index"]) + (0.3 * f["Collaboration"])
    f["Research Score"] = score
    print(f["Faculty Name"], "=", round(score, 2))

print("\nGrant Allocation")

for f in faculty:
    print(f["Faculty Name"], "Research Score =", round(f["Research Score"], 2))

print("\nFaculty Receiving Grants Above $100000")

for f in faculty:
    if f["Budget"] > 100000:
        print(f["Faculty Name"], "-", f["Budget"])

department = {}

for f in faculty:
    dept = f["Department"]

    if dept in department:
        department[dept] += f["Budget"]
    else:
        department[dept] = f["Budget"]

max_dept = max(department, key=department.get)

print("\nDepartment Receiving Maximum Funding")
print(max_dept, "-", department[max_dept])

faculty.sort(key=lambda x: x["Research Score"], reverse=True)

print("\nFaculty Ranking")

rank = 1

for f in faculty:
    print(rank, ".", f["Faculty Name"], "-", round(f["Research Score"], 2))
    rank += 1


total = 0

for f in faculty:
    total += f["Research Score"]

average = total / len(faculty)

print("\nAverage Research Score =", round(average, 2))


print("\nTop Performer")
print(faculty[0]["Faculty Name"])

file = open("ranking.txt", "w")

for f in faculty:
    file.write(str(f))
    file.write("\n")

file.close()

print("\nRanking Saved Successfully")


print("\nReading Ranking File")

file = open("ranking.txt", "r")

print(file.read())

file.close()

print("Checking Budgets")

try:
    for f in faculty:
        if f["Budget"] < 0:
            raise ValueError("Invalid Budget Found")

    print("All Budgets are Valid")

except ValueError as e:
    print(e)
