import math

def loan(age, salary, existing, credit, emp, loan_amt, years):
    try:
        if age < 18 or age > 60:
            return "Invalid Age"

        if salary <= 0 or loan_amt <= 0 or years <= 0:
            return "Invalid Input"

        dti = existing / salary

        if credit >= 750:
            rate = 8.5
            eligible = salary * 60
        elif credit >= 650:
            rate = 10.5
            eligible = salary * 40
        else:
            rate = 13.5
            eligible = salary * 20

        if emp == "Government":
            eligible *= 1.2
        elif emp == "Self":
            eligible *= 0.8

        r = rate / 1200
        n = years * 12
        emi = loan_amt * r * (1+r)**n / ((1+r)**n-1)

        if credit < 600:
            return "Poor Credit Score"
        elif existing > 1000000:
            return "Existing Loan Exceeded"
        elif dti > 0.5:
            return "High DTI"
        elif loan_amt > eligible:
            return "Rejected"
        else:
            return "Approved | EMI = " + str(round(emi,2))

    except Exception:
        return "Exception Handled"

print("TC1 Minimum Age:", loan(18,50000,0,750,"Private",100000,5))
print("TC2 Maximum Age:", loan(60,60000,0,760,"Government",200000,5))
print("TC3 Invalid Salary:", loan(30,0,0,700,"Private",100000,5))
print("TC4 Poor Credit:", loan(30,50000,0,550,"Private",100000,5))
print("TC5 Existing Loan:", loan(30,50000,1500000,750,"Private",100000,5))
print("TC6 High DTI:", loan(30,20000,15000,700,"Private",100000,5))
print("TC7 Government:", loan(30,50000,0,760,"Government",200000,5))
print("TC8 Private:", loan(30,50000,0,760,"Private",200000,5))
print("TC9 Self:", loan(30,50000,0,760,"Self",200000,5))
print("TC10 Boundary Loan:", loan(30,50000,0,650,"Private",2000000,20))
print("TC11 EMI Accuracy:", loan(30,50000,10000,750,"Private",300000,5))

try:
    print("TC12 Exception:", loan(30,None,1000,700,"Private",100000,5))
except:
    print("TC12 Exception Handled")
