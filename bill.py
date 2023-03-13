# Define constants
RATE_A = 0.50
RATE_B = 1.00
RATE_C = 1.20
RATE_D = 1.50

ERROR_MESSAGE = "Please enter a valid input."
USAGE_ERROR_MESSAGE = "Usage must be a positive number."
ID_ERROR_MESSAGE = "Huduma ID number must be a valid number."

# Get user input
print("ELECTRICITY BILL BASED ON UNITS CONSUMED")
house = input("Which house do you live in? ")
renter = input("What's your last name as appeared in ID? ")

# Validate social ID number
while True:
    hudumaId_str = input("Enter the Huduma ID number: ")
    try:
        hudumaId = int(hudumaId_str)
        break
    except ValueError:
        print(ID_ERROR_MESSAGE)

# Validate usage
while True:
    usage_str = input("Enter the electricity units: ")
    try:
        usage = float(usage_str)
        if usage < 0:
            print(USAGE_ERROR_MESSAGE)
        else:
            break
    except ValueError:
        print(USAGE_ERROR_MESSAGE)

# Calculate cost based on usage
if usage <= 50:
    total = usage * RATE_A
    print("{}'s cost is {:.2f}".format(renter, total))
elif usage <= 100:
    total = usage * RATE_B
    print("{}'s cost is {:.2f}".format(renter, total))
elif usage <= 200:
    total = usage * RATE_C
    print("{}'s cost is {:.2f}".format(renter, total))
elif usage <= 250:
    total = usage * RATE_D
    print("{}'s cost is {:.2f}".format(renter, total))
else:
    print("{}'s usage of {} is not valid for house {}. Please enter a valid usage.".format(renter, usage, house))

# Print summary of input and output
print("House:", house)
print("Renter:", renter)
print("Huduma ID number:", hudumaId)
print("Usage:", usage)
print("Total cost:", total)
