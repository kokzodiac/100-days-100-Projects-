import random
names_string = input("Give me everybody's names, separated by a comma. ")
# Split string to a list method
names = names_string.split(", ")
# Give the total number of names
numb_of_names = len(names)
# The random choice computer will give
random_choice = random.randint(0,numb_of_names-1)

random_people = names[random_choice]

print(f"{random_people} is the one needs to pay the bill.")
