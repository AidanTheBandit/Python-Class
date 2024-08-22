# Input logic
name = input("What's your name? ")
thing = input("What's your favorite thing? ")
age = int(input("Whats your age "))
siblings = int(input("How many siblings do you have? "))
# Prints the types
print("Name type: ", type(name), "\n", "Thing type: ", type(thing), "\n", "Age type: ", type(age), "\n", "Siblings type: ", (siblings))

# Decides wheather or not to print "no siblings" or print sibling if the user has one sibling or add print siblings if the user has more than one sibling
if siblings == 1 | siblings == -1:
    sibling = str(siblings) + " sibling"
elif siblings == 0 | siblings == -0:
    sibling = "no siblings"
else:
    sibling = str(siblings) + " siblings"    

# Prints the results
print(name + "'s favorite thing is the " + thing)
print(name + " is " + str(age) + " years old")
print(name, "has", str(sibling))


# N + A <3