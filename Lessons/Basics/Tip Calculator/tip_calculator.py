# set bill amount, tip percentage, and number of people variables
bill_amount = float(input("Bill Amount: "))
tip_percentage = float(input("Tip Percentage: "))
number_of_people = int(input("Number of People: "))

# calculate the tip amount, total amount, and amount each person should pay
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / number_of_people

# print the results
print("Bill Amount: ${:.2f}".format(bill_amount))
print("Tip Percent: {:.0f}%".format(tip_percentage))
print("Tip Amount: ${:.2f}".format(tip_amount))
print("Total Amount: ${:.2f}".format(total_amount))
print("Amount Per Person: ${:.2f}".format(amount_per_person))