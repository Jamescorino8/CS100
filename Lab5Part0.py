#James Corino 5/18/21
cents = int(input("Enter the number of pennies: "))
print("")

print(str(cents) + " pennies is equivelent to: ")

dollars = cents // 100
print(str(dollars) + " Dollars")
cents = cents % 100

quarters = cents // 25
print(str(quarters) + " Quarters")
cents = cents % 25

dime = cents // 10
print(str(dime) + " Dimes")
cents = cents % 10

nickels = cents // 5
print(str(nickels) + " Nickels")
cents = cents % 5

pennies = cents // 1
print(str(pennies) + " Pennies")