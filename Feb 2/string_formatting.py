#########################################
# 2/2 Class Code
#########################################

# Method 1: Commas
name = "Skyler"
print("My name is", name)

# Method 2: Concatenation
state = "Arkansas"
print("I am from " + state + ".")

# Method 3: Old Style Strings
cat = "Samson"
weight = 10
print("Our cat %s weighs %s pounds." % (cat, weight))

# Method 4: .format()
number = 5
print("My favorite number is {}.".format(number))

# Method 5: fstrings
# This method is recommended!
thing = "bird"
place = "window"

# Standard
print(f'The {thing} is in the {place}.')

# Center Justify
print(f'The {thing:^10s} is in the {place:^10s}.')

# Left Justify
print(f'The {thing:<10s} is in the {place:<10s}.')

# Right Justify
print(f'The {thing:>10s} is in the {place:>10s}.')

# Fill Character
print(f'The {thing:_^10s} is in the {place:_^10s}.')