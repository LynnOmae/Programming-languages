#LYNN NYANDUKO OMAE
#SCT211-0092/2022

weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in meters:"))

#calculating the BMI
BMI=weight/(height**2)

if BMI < 18.5:
    print(f"Underweight")

elif BMI > 24.9:
    print(f"Overweight")

else:
    print(f"Normal Weight")