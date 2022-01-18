print("welcome to the Mph to Mps conversion app !!")

#getting input from the user as a number n't in string
mph = float(input("Enter your speed in Miles per hour here: "))

#converting mph to mps
conversion = mph*0.4474

#rounding to 2 decimal places
rounded_value = round(conversion,2)
print("your speed in meter per second is", rounded_value)