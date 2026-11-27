#to convert temperature from Celsius to Fahrenheit (Celsius as parameter) and returns the result
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit =", fahrenheit)
