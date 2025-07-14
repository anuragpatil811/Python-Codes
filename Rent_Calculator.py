#Inputs we need from the user
#Total Rent
#Total food ordered for snacking 
#Electricity units spend
#Charge per unit
#Number of people living in room/flat
##Output
#Total amount you have to pay
rent = int(input("Enter your hostel/flat rent:"))
food = int(input("Enter the amount of food ordered="))
electricity_spend = int(input("Enter the total of electricity spent = "))
charge_per_unit = int(input("Enter the charge per unit = "))
People = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend  * charge_per_unit 
print(total_bill)
output = (food + rent + total_bill)//People
print("Each person will pay = ", output)