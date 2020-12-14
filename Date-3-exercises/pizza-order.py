print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size in ['s','S','small','SMALL']:
    bill += 15
    if add_pepperoni in ['y','Y','Yes','YES','yes']:
        bill +=2
        if extra_cheese in ['y','Y','Yes','YES','yes']:
            bill +=1
        else:
            bill +=0
if size in ['m','M','medium','MEDIUM']:
    bill += 20
    if add_pepperoni in ['y','Y','Yes','YES','yes']:
        bill +=3
        if extra_cheese in ['y','Y','Yes','YES','yes']:
            bill +=1
        else:
            bill +=0
if size in ['l','L','large','LARGE']:
    bill += 25
    if add_pepperoni in ['y','Y','Yes','YES','yes']:
        bill +=3
        if extra_cheese in ['y','Y','Yes','YES','yes']:
            bill +=1
        else:
            bill +=0
print(f"Your final bill is ${bill}")
