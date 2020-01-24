__author__ = 'Olive Baldwin'

w = 0
h = 0
area = 0


def get_width_and_height():
    w = int(input("How wide is the bo x?"))
    h = int(input("How tall is the box?"))
    return w, h


def calculate_area(w, h):
    area = w * h
    return area


def display_area(w, h, area):
    print("A box that is {:.0f} units wide and {:.1f} units high".format(w, h))
    print("has an area of {:.2f} square units.".format(int(area)))


def main():
    w, h = get_width_and_height()
    area = calculate_area(w, h)
    display_area(w, h, area)


main()