#Tip Calculator


print("Welcome to the tip calculator!")
total_bill = float(input("What was the total Bill? ₹"))
tip_percent = int(input("How much tip would you like to give? 10 ,12 ,or 15 ?"))
people = int(input("How many people to split the bill?"))

tip = (tip_percent / 100) * total_bill
total_amount = total_bill + tip
split = total_amount / people
print("Each person should pay :",round(split,2))