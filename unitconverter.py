# Unit Converter Tool (CLI)

def length_converter():
    print("\nLength Converter")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")

    choice = input("Choose option: ")

    if choice == '1':
        km = float(input("Enter value in kilometers: "))
        print("Meters:", km * 1000)

    elif choice == '2':
        m = float(input("Enter value in meters: "))
        print("Kilometers:", m / 1000)

    else:
        print("Invalid choice")


def weight_converter():
    print("\nWeight Converter")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")

    choice = input("Choose option: ")

    if choice == '1':
        kg = float(input("Enter value in kg: "))
        print("Grams:", kg * 1000)

    elif choice == '2':
        g = float(input("Enter value in grams: "))
        print("Kilograms:", g / 1000)

    else:
        print("Invalid choice")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose option: ")

    if choice == '1':
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5) + 32)

    elif choice == '2':
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", (f - 32) * 5/9)

    else:
        print("Invalid choice")


# Main Program
while True:
    print("\n=== Unit Converter ===")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == '1':
        length_converter()
    elif choice == '2':
        weight_converter()
    elif choice == '3':
        temperature_converter()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice")