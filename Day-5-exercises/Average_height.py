student_heights = input("Input a list of student heights in cm. ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
    # or total_height = (old) total_height + height

numb_of_students = 0
for student in student_heights:
    numb_of_students += 1
    # or numb_of_students = (old) numb_of_students + 1

average = round(total_height / numb_of_students)
print(average)