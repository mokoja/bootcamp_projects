print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print ("You can ride.")
  age = int(input("What's your age? "))
  if age < 12:
    print ("Ride is $5.")
  elif age <= 18:
    print ("Ride is $7")
  else:
    print ("ride is $11.")
else:
  print ("Sorry! You can't ride.")

