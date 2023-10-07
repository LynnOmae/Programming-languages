#LYNN NYANDUKO OMAE
#SCT211-0092/2022

total_bill_amount=int(input("Please enter the total bill amount:"))
print(f"The tip percentage options are 0.1, 0.12 and 0.15")
tip_amount=float(input("Enter the tip percentage of the total bill from the options above:"))
people=int(input("Enter the number of people splitting the bill:"))

tip= total_bill_amount*tip_amount

total=total_bill_amount+tip

amount_each=total/people

print(f"The amount for each person is {amount_each:.2f}")