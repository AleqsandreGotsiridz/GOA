
operator = input("Enter the operator (+, -, *, //): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3nd number: "))
numi = 5
if operator == "+":
        result = num1 + num2 + num3
        print(round(result,4 ))
elif operator == "-":
        result = num1 - num2 - num3
        print(round(result,4 ))
elif operator == "*":
        result = num1 * num2 * num3
        print(round(result,4 ))
elif operator == "//":
        result = num1 // num2 // num3
        print(round(result,4 ))
else:
        print(f"{operator} is not a valid operator! Please use one of the following: +, -, *, //")
