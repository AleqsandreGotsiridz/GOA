operator = input("Enter the operator (+, -, *, //): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
if operator == "+":
        result = num1 + num2
        print(round(result,3 ))
elif operator == "-":
        result = num1 - num2 
        print(round(result,3 ))
elif operator == "*":
        result = num1 * num2
        print(round(result,3 ))
elif operator == "//":
        result = num1 // num2
        print(round(result,3 ))
else:
        print(f"{operator} is not a valid operator! Please use one of the following: +, -, *, //")
