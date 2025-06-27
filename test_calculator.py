print("Welcome to the Bill Split Calculator.")

bill_amount = float(input("Please input the total bill amount. "))
tip_percentage = float(input("What is the tip amount you are giving? "))
people_amount = float(input("How many people are you splitting the bill between? "))

tip_amount = (tip_percentage / 100) * bill_amount

total_amount = (bill_amount + tip_amount)

amount_by_person = (total_amount / people_amount)

print(f"Total (including tip): ${total_amount: .2f}")

print(f"Each person pays: ${amount_by_person: .2f}")

print("Thank you for using the Bill Split Calculator!")
