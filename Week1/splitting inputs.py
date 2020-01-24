__author__ = 'Olive Baldwin'

# input data
inp = input("Enter '[width],[unit],[height],[unit],[target unit]' to calculate a rectangle's area: ")
width_input, wunit, height_input, hunit, tunit = inp.split(", ")
print("Width:", width_input, wunit)
print("Height:", height_input, hunit)
print("Target Unit:", tunit)

# convert units
if wunit == "ft" or "feet" or "foot":
    width_inches = float(width_input) * 12
    print("width_inches:", width_inches)
elif wunit == "in" or "inches" or "inch":
    width_inches = float(width_input)
    print("width_inches:", width_inches)
else:
    exit("Invalid width unit")

if hunit == "ft" or "feet" or "foot":
    height_inches = float(height_input) * 12
    print("height_inches:", height_inches)
elif hunit == "in" or "inches" or "inch":
    height_inches = float(height_input)
    print("height_inches:", height_inches)
else:
    print("Invalid height unit")
    exit(1)

# calculate area
area_inches = float(width_inches) * float(height_inches)
print("area_inches:", area_inches)

if tunit == "ft" or "feet" or "foot":
    tarea = area_inches / 144
elif tunit == "in" or "inches" or "inch":
    tarea = area_inches
else:
    print("Invalid target unit")
    exit(1)

# display result
print("The area is", tarea, "sq.", tunit, end=".")