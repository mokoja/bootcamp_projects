#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇

print ("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
n_people = int(input("How many people to split the bill? "))

tip_perc = 1+ tip/100
total_per_person = (total / n_people) * tip_perc
final_amount = "{:.2f}".format(total_per_person)
print (f"Each person should pay: ${final_amount}")
