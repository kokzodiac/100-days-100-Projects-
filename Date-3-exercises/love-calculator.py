print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
combined_name = name1+name2
lower_case_both_name = combined_name.lower()

t = lower_case_both_name.count('t')
r = lower_case_both_name.count('r')
u = lower_case_both_name.count('u')
e = lower_case_both_name.count('e')
true = t+r+u+e

l = lower_case_both_name.count('l')
o = lower_case_both_name.count('o')
v = lower_case_both_name.count('v')
e = lower_case_both_name.count('e')
love = l+o+v+e

true_love = int(str(true)+str(love))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos")
elif true_love > 40 and true_love < 50:
    print(f"Your score is {true_love}, you are alright together")
else:
    print(f"Your score is {true_love}, which is bad xd.")
