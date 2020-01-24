__author__ = 'Olive Baldwin'

f = 0.00
c = 0.00

def get_input():
    f = float(input("Enter temperature in degrees Fahrenheit: "))
    return f

def convert_temp(f):
    c = (f - 32) * 5/9
    return c

def display_temp(f, c):
    print("If the temperature is", f, "degrees Fahrenheit, it is", c, "degrees Celsius.")

def main():
    f = get_input()
    c = convert_temp(f)
    display_temp(f, c)


main()