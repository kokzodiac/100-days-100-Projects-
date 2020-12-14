print ("Welcome to Auckland airport! \n")
place = str(input ("Where do you want to go in New Zealand? \n" "For example, Christchurch, Wellington, Otago. "))
if place in ['Christchurch', 'christchurch']:
    age = int(input("Type in your age to see the fee that you need to pay. "))
    if age <= 10:
        print("You need to pay $100 for the flight.")
    elif age <=16:
        print("You need to pay $200 for the flight.")
    elif age > 45 and age < 55:
        print("You get it free.")
    else:
        print("You need to pay $300 for the flight.")
elif place in ['Wellington', 'wellington']:
    age = int(input("Type in your age to see the fee that you need to pay. "))
    if age <= 10:
        print("You need to pay $50 for the flight.")
    elif age <=16:
        print("You need to pay $150 for the flight.")
    elif age > 45 and age < 55:
        print("You get it free.")
    else:
        print("You need to pay $250 for the flight.")
else:
    age = int(input("Type in your age to see the fee that you need to pay. "))
    if age <= 10:
        print("You need to pay $150 for the flight.")
    elif age <=16:
        print("You need to pay $250 for the flight.")
    elif age > 45 and age < 55:
        print("You get it free.")
    else:
        print("You need to pay $350 for the flight.")
