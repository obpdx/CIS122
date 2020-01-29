__author__ = 'Olive Baldwin'

# Calculates the height difference between user and Shaquille O'Neal.
# Inputs: height_raw
# Outputs: height_diff

# Declare Integer height_ft
# Declare Integer height_in
# Declare Integer total_height_in
# Declare Integer height_diff
#
# Declare Constant SHAQ_HEIGHT
#
# Module get_input()
#   Display prompt for height input
#   Input height_ft, height_in
# End module
#
# Function calc_height()
#   Set total_height_in = (height_ft * 12) + height_in
# End function
#
# Function calc_diff()
#   Set height_diff = SHAQ_HEIGHT - total_height_in
# End function
#
# Function display_diff()
#   If height_diff < 0
#       Set height_diff = -height_diff
#       Display "You are [height_diff] inches taller than Shaq."
#   Else if height_diff == 0
#       Display "You are the same height as Shaq."
#   Else if height diff > 0
#       Display "You are [height_diff] inches shorter than Shaq."
#   End if
# End function
#
# Module main()
#   Set height_ft, height_in = get_input()
#   Set total_height_in = calc_height(height_ft, height_in)
#   Set height_diff = calc_diff(total_height_in)
#   Call display_diff(height_diff)

height_ft = 0
height_in = 0
total_height_in = 0
height_diff = 0

SHAQ_HEIGHT = 85


def get_input():
    height_ft, height_in = input("Enter your height in feet and inches, e.g. '5 10' or '6 0': ").split()
    return height_ft, height_in


def calc_height(height_ft, height_in):
    total_height_in = (int(height_ft) * 12) + int(height_in)
    return total_height_in


def calc_diff(total_height_in):
    height_diff = SHAQ_HEIGHT - total_height_in
    return height_diff


def display_diff(height_diff):
    if height_diff < 0:
        print("You are {:d} inches taller than Shaq.".format(-height_diff))
    if height_diff == 0:
        print("You are the same height as Shaq.")
    if height_diff > 0:
        print("You are {:d} inches shorter than Shaq.".format(height_diff))


def main():
    height_ft, height_in = get_input()
    total_height_in = calc_height(height_ft, height_in)
    height_diff = calc_diff(total_height_in)
    display_diff(height_diff)


main()
