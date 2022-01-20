#BMI Calculator
#Ask user height and weight
height=float(input("Enter your height in m : "))
weight=float(input("Enter your weight in kg : "))

#calculate the BMI value
bmi=round(weight/height**2,2)
print(bmi)
#find the range of bmi
if bmi<18.5:
    print(f"your bmi is {bmi}, you are underweight")
elif bmi<25 :
    print(f"your bmi is {bmi}, you are normal weight")
elif bmi<30 :
    print(f"your bmi is {bmi}, you are overweight") 
elif bmi<35 :
    print(f"your bmi is {bmi}, you are obese") 
else :
    print(f"your bmi is {bmi}, you are clinical obese")              
