print("ELECTRICITY BILL BASED ON UNITS CONSUMED")
house = str(input("Which house do you live in?"))
renter = str(input("What's your last name as appeared in ID?"))
socialId = int(input("Enter your social ID number:"))
usage = float(input("Enter the electricity units:"))
a = 0.50
b = 1.00
c = 1.20
d = 1.50

if usage > 0 and usage <= 50:
    totalA = usage * a
    print(renter,"The cost is {}".format(totalA))
elif usage >= 51 and usage <= 100:
    totalB = usage * b
    print(renter, "The cost is {}".format(totalB))
elif usage >= 101 and usage <= 200:
    totalC = usage * c
    print(renter, "The cost is {}".format(totalC))
elif usage >= 201 or usage >= 250:
    totalD = usage * d
    print(renter, "The cost is {}".format(totalD))
else:
    print(renter,"Please input the correct unit of house {}".format(house))
