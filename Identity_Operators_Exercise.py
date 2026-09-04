#Identity Operators Exercise
#is identity operator
a=[7,8,9]
b=a
result=b is a 
print("result of" ,b, "is" ,a, "is :" ,result)
a=[7,18,45]
b=[7,18,45]
result=b is a
print("result of" ,b, "is" ,a, "is :", result)
#is not identity operator
a=[2,5,8]
b=a
result=b is not a 
print("result of" ,b, "is not" ,a, "is :" ,result)
a=[7,18,45]
b=[7,18,45]
result=b is not a
print("result of" ,b, "is not" ,a, "is :", result)