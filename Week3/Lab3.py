__author__ = 'Olive Baldwin'

# Calculates the height difference between user and Shaquille O'Neal, then determines
# type of height-augmenting footwear needed to kiss him on the forehead (if any).
#
# Inputs: height_raw
# Outputs: height_diff, shoes

# Declare Integer height_ft
# Declare Integer height_in
# Declare Integer total_height_in
# Declare Integer height_diff
# Declare String shoes
# Constant Integer SHAQ_HEIGHT
#
# Function get_input()
#   Display prompt for user's height
#   Input height_ft, height_in
#   Return height_ft, height_in
# End function
#
# Function calc_height(height_ft, height_in)
#   Set total_height_in = (height_ft * 12) + height_in
#   Return total_height_in
# End function
#
# Function calc_diff(total_height_in)
#   Set height_diff = SHAQ_HEIGHT - total_height_in
#   Return height_diff
# End function
#
# Function choose_shoe(height_diff)
#   If height_diff <= -6 Then
#       Set shoes = "to crouch"
#   Else If height_diff <= 0 Then
#       Set shoes = "nothing"
#   Else If height_diff <= 6 Then
#       Set shoes = "platform boots"
#   Else If height_diff <= 12 Then
#       Set shoes = "stilts"
#   Else If height_diff <= 18 Then
#       Set shoes = "a step stool"
#   Else
#       Set shoes = "a ladder"
#   Return shoes
# End function
#
# Function display_diff(height_diff)
#   If height_diff < 0 Then
#       Set height_diff = -height_diff
#       Display "You are", height_diff, "inches taller than Shaq."
#   Else If height_diff == 0 Then
#       Display "You are the same height as Shaq."
#   Else If height diff > 0 Then
#       Display "You are", height_diff, "inches shorter than Shaq."
#   End If
# End function
#
# Function display_shoes(shoes)
#   Display "You would need", shoes, "to kiss Shaq on his head."
# End function
#
# Module main()
#   Set height_ft, height_in = get_input()
#   Set total_height_in = calc_height(height_ft, height_in)
#   Set height_diff = calc_diff(total_height_in)
#   Set shoes = choose_shoe(height_diff)
#   Call display_diff(height_diff)
#   Call display_shoes(shoes)
# End module
#
# Call main()

height_ft = 0
height_in = 0
total_height_in = 0
height_diff = 0
shoes = ""
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


def choose_shoe(height_diff):
    if height_diff <= -6:
        shoes = "to crouch"
    elif height_diff <= 0:
        shoes = "nothing"
    elif height_diff <= 6:
        shoes = "platform boots"
    elif height_diff <= 12:
        shoes = "stilts"
    elif height_diff <= 18:
        shoes = "a step stool"
    else:
        shoes = "a ladder"
    return shoes


def display_diff(height_diff):
    if height_diff < 0:
        print("You are {:d} inches taller than Shaq.".format(-height_diff))
    if height_diff == 0:
        print("You are the same height as Shaq.")
    if height_diff > 0:
        print("You are {:d} inches shorter than Shaq.".format(height_diff))


def display_shoes(shoes):
    print("You would need {:s} to kiss Shaq on his head.".format(shoes))


def main():
    height_ft, height_in = get_input()
    total_height_in = calc_height(height_ft, height_in)
    height_diff = calc_diff(total_height_in)
    shoes = choose_shoe(height_diff)
    display_diff(height_diff)
    display_shoes(shoes)


main()