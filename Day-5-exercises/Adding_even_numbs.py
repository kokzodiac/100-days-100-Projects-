first_n = int(input("What is the first number of the range you want to add evenly? "))
second_n = int(input("How about the second number of the range? "))

total_even_n = 0
for n in range (first_n,second_n,2):
    total_even_n += n

print(total_even_n)

# Another way of solving this problem

total_even_n2 = 0
for n in range (first_n,second_n):
    if n % 2 == 0:
        total_even_n2 += n
print(total_even_n2)
