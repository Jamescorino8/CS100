#James Corino 5/20/21
car1cost = 18000
car1mpg = 24
car1value = 7200

car2cost = 16580
car2mpg = 22
car2value = float(3846.56)

nummiles = 13500
costpergal = float(2.94)

car1total = car1mpg / costpergal
car1total = (nummiles * car1total) + car1cost
car1total = round(car1total)

car2total = car2mpg / costpergal
car2total = (nummiles * car2total) + car2cost
car2total = round(car2total)

print("Car A:")
print("Cost: " + str(car1cost))
print("Miles to the gallon: " + str(car1mpg))
print("Resale value after 5 years:  " + str(car1value))
print("The total cost of ownership after 5 years: " + str(car1total) + '\n')

print("Car B:")
print("Cost:  " + str(car2cost))
print("Miles to the gallon: " + str(car2mpg))
print("Resale value after 5 years:  " + str(car2value))
print("The total cost of ownership after 5 years: " + str(car2total) + '\n')

answer = input("Would you like to buy Car A or Car B? ")
print("\nCongratulations, you have purchased " + str(answer))