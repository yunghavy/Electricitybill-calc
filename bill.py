# Get user input
print("ELECTRICITY BILL BASED ON UNITS CONSUMED")
house = str(input("Which house do you live in?"))
renter = str(input("What's your last name as appeared in ID?"))
socialId = int(input("Enter your social ID number:"))
usage = float(input("Enter the electricity units:"))

# Rates defining
rateA = 0.50
rateB = 1.00
rateC = 1.20
rateD = 1.50

# Calculating cost based on usage

if usage > 0 and usage <= 50:
    total = usage * rateA
    print("{}'s cost is {:.2f}".format(renter, total))
elif usage > 50 and usage <= 100:
    total = usage * rateB
    print("{}'s cost is {:.2f}".format(renter, total))
elif usage > 100 and usage <= 200:
    total = usage * rateC
    print("{}'s cost is {:.2f}".format(renter, total))
elif usage > 200 and usage <= 250:
    total = usage * rateD
    print("{}'s cost is {:.2f}".format(renter, total))
else:
    print("{}'s usage of {} is not valid for house {}. Please enter a valid usage.".format(renter, usage, house))e))


