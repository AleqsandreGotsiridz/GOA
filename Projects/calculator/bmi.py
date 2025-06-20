    #Bmi
while True:
    Input = input("Hi it's a BMI Lets GO!:")#input
    age = float(input("enter your age:"))#age
    weight = float(input("enter your weigth:"))#weight
    height = float(input("enter your heigth:"))#height
    heigth_in_meters = height / 100#height in meters 
    bmi = weight / (heigth_in_meters ** 2)#squaring
    print("your bmi is:",bmi)#print

    if bmi < 18.5:
        print("You're underweight!")
    elif 18.5 <= bmi < 25:
        print("You're a normal weight!")
    elif 25 <= bmi < 30:
        print("You're overweight!")
    else:
        print("You're fat!")