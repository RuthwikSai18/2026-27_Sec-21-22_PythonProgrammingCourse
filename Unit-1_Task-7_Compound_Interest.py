#Calculating COMPOUND INTEREST
p=int(input("Enter the principal amount:"))
r=float(input("Enter the rate of interest:"))
n=float(input("Enter the number of times interest is compunded in every year:"))
t=float(input("Enter the time in years:"))
ci=p*(1+r/n)**(n*t)
print(ci)
