name = input("What's your name? ")
thing = input("What's your favorite thing? ")
age = int(input("Whats your age "))
siblings = int(input("How many siblings do you have? "))
print("Name type: ", type(name), "\n", "Thing type: ", type(thing), "\n", "Age type: ", type(age), "\n", "Siblings type: ", (siblings))


if siblings == 1:
    sibling = str(siblings) + " sibling"
elif siblings == 0:
    sibling = "no siblings"
else:
    sibling = str(siblings) + " siblings"    

print(name + "'s favorite thing is the " + thing)
print(name + " is " + str(age) + " years old")
print(name, "has", str(sibling))