print("Welcome to the tip calculator")
bill = float(input("What was the total bill: "))
tip_percent = int(input("What percentage tip would you like to give? 10,12, or 15? "))
people = int(input("How many people to split the bill: "))

tip = bill*(tip_percent/100)
total_bill = bill + tip

final = round(total_bill / people , 2)

print(f"Each person should pay: {final}")