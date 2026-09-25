#Voting Eligibility
age=int(input("Enter age in years:"))
if age >= 18:
    print(f"Age is {age} years: Eligible to vote")
else:
    print(f"Age is {age} years: Not eligible to vote")