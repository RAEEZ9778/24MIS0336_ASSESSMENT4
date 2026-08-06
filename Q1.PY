faculty = [
    {
        "Faculty ID":101,
        "Faculty Name":"Alice",
        "Department":"CSE",
        "Publications":40,
        "H-index":18,
        "Budget":120000,
        "Collaboration":80
    },

    {
        "Faculty ID":102,
        "Faculty Name":"Bob",
        "Department":"ECE",
        "Publications":30,
        "H-index":15,
        "Budget":95000,
        "Collaboration":70
    },

    {
        "Faculty ID":103,
        "Faculty Name":"Charlie",
        "Department":"IT",
        "Publications":50,
        "H-index":22,
        "Budget":150000,
        "Collaboration":90
    }
]

# 1. Calculate Research Score

for f in faculty:
    f["Research Score"] = (
        0.4 * f["Publications"] +
        0.3 * f["H-index"] +
        0.3 * f["Collaboration"]
    )

# 2. Allocate Grants according to Research Score

print("Grant Allocation")

for f in faculty:
    print(f["Faculty Name"], ":", round(f["Research Score"],2))

# 3. Faculty receiving grants above $100000

print("\nFaculty receiving grant above 100000")

for f in faculty:
    if f["Budget"] > 100000:
        print(f["Faculty Name"], f["Budget"])

# 4. Department receiving maximum funding

department = {}

for f in faculty:

    if f["Department"] in department:
        department[f["Department"]] += f["Budget"]
    else:
        department[f["Department"]] = f["Budget"]

max_department = max(department, key=department.get)

print("\nDepartment with Maximum Funding")
print(max_department)

# 5. Rank Faculty Members

faculty.sort(key=lambda x:x["Research Score"], reverse=True)

print("\nFaculty Ranking")

rank = 1

for f in faculty:
    print(rank, f["Faculty Name"], round(f["Research Score"],2))
    rank += 1

# 6. Average Research Score

total = 0

for f in faculty:
    total += f["Research Score"]

average = total / len(faculty)

print("\nAverage Research Score =", round(average,2))

# 7. Top Performer

print("\nTop Performer")
print(faculty[0]["Faculty Name"])

# 8. Save Ranking to File

file = open("ranking.txt","w")

for f in faculty:
    file.write(str(f))
    file.write("\n")

file.close()

# 9. Read Ranking File

print("\nContents of ranking.txt")

file = open("ranking.txt","r")

print(file.read())

file.close()

# 10. Handle Invalid Budget

try:

    budget = int(input("\nEnter Project Budget : "))

    if budget < 0:
        raise ValueError

    print("Valid Budget")

except ValueError:
    print("Invalid Budget")
