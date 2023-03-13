# Defining constants
ERROR_MESSAGE = "Please enter a valid input."
USAGE_ERROR_MESSAGE = "Usage must be a positive number."
ID_ERROR_MESSAGE = "Huduma ID number must be a valid number."

RATE_TABLE = {
    (0, 50): 0.50,
    (51, 100): 1.00,
    (101, 200): 1.20,
    (201, 250): 1.50,
}

# Defining functions
def calculate_total_cost(usage):
    for range_, rate in RATE_TABLE.items():
        if usage >= range_[0] and usage <= range_[1]:
            return usage * rate
    return None

# Getting user input
print("ELECTRICITY BILL BASED ON UNITS CONSUMED")
num_houses = int(input("How many houses do you want to calculate? "))

for i in range(num_houses):
    print(f"\nHOUSE {i+1}")
    house = input("Which house do you live in? ")
    renter = input("What's your last name as appeared in ID? ")

    # Validating huduma ID number
    while True:
        hudumaId_str = input("Enter the huduma ID number: ")
        try:
            hudumaId = int(hudumaId_str)
            break
        except ValueError:
            print(ID_ERROR_MESSAGE)

    # Validating usage
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

    # Calculate total cost based on usage
    total = calculate_total_cost(usage)
    if total is not None:
        print(f"{renter}'s cost is {total:.2f}")
    else:
        print(f"{renter}'s usage of {usage} is not valid for house {house}. Please enter a valid usage.")

    # Print summary of input and output
    print(f"House: {house}")
    print(f"Renter: {renter}")
    print(f"Social ID number: {hudumaId}")
    print(f"Usage: {usage}")
    print(f"Total cost: {total:.2f}" if total is not None else "N/A")
