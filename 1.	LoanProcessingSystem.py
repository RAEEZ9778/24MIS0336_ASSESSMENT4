import math

customer_id = "C101"
age = 30
salary = 50000
existing_loan = 10000
credit_score = 720
employment = "Private"
requested_loan = 300000
loan_tenure = 5

dti = existing_loan / salary

# Interest Rate & Eligible Loan
if credit_score >= 750:
    interest = 8.5
    eligible = salary * 60
elif credit_score >= 650:
    interest = 10.5
    eligible = salary * 40
else:
    interest = 13.5
    eligible = salary * 20

if employment == "Government":
    eligible *= 1.2
elif employment == "Self":
    eligible *= 0.8


r = interest / (12 * 100)
n = loan_tenure * 12
emi = requested_loan * r * (1 + r) ** n / ((1 + r) ** n - 1)


if age < 18 or age > 60:
    status = "REJECTED"
elif salary <= 0:
    status = "REJECTED"
elif credit_score < 600:
    status = "REJECTED"
elif existing_loan > 1000000:
    status = "REJECTED"
elif dti > 0.5:
    status = "REJECTED"
elif requested_loan > eligible:
    status = "REJECTED"
else:
    status = "APPROVED"

print("Customer ID :", customer_id)
print("Age :", age)
print("Salary :", salary)
print("Existing Loan :", existing_loan)
print("Credit Score :", credit_score)
print("Employment :", employment)
print("Requested Loan :", requested_loan)
print("Loan Tenure :", loan_tenure)
print("DTI :", round(dti, 2))
print("Eligible Loan :", eligible)
print("Interest Rate :", interest, "%")
print("EMI :", round(emi, 2))
print("Status :", status)
