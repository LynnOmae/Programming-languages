#LYNN NYANDUKO OMAE 
#SCT211-0092/2022

from datetime import datetime

current_date=datetime.now()

#get the user's birth info
year_of_birth=int(input("Enter your year of birth:"))
month_of_birth=int(input("Enter the number of you month of birth:"))
date_of_birth=int(input("Enter the date of birth:"))

#calculating the age
age_in_years= current_date.year-year_of_birth
age_in_months= current_date.month-month_of_birth
age_in_days= current_date.day-date_of_birth

name=input("Enter name:")

print(f"Hello,{name}.Lets do some calculations")
value1=int (input("Enter the first number"))
value2=int (input("Enter the second number"))
sum=value1+value2
print(f"Your age is {age_in_years} years, {age_in_months} months, {age_in_days}days. " )
print(f"The sum of {value1} and {value2} is {sum}" )