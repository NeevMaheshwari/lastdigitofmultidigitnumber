number = int(input("Enter a multidigit number: "))
digits = int(input("How many digits do you want? "))
power = int(input("Enter the power to raise the number to: "))

result = str(number ** power)
print("The last", digits, "digits of", number, "raised to the power", power, "are:", result[-digits:])
