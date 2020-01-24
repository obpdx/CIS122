__author__ = 'Olive Baldwin'

miles_per_gallon = 0
tank_size = 0
range = 0


def get_inputs():
    miles_per_gallon = int(input("How many miles per gallon does your car get?"))
    tank_size = int(input("How big in gallons is your tank?"))
    return miles_per_gallon, tank_size


def calculate_range(miles_per_gallon, tank_size):
    range = miles_per_gallon * tank_size
    return range


def display_outputs(miles_per_gallon, tank_size, range):
    print("Your car gets", miles_per_gallon, tank_size, range)
    print("Your total range is", range, "miles")


def main():
    miles_per_gallon, tank_size = get_inputs()
    range = calculate_range(miles_per_gallon, tank_size)
    display_outputs(miles_per_gallon, tank_size, range)


main()