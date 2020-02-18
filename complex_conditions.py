gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# if gpa >= 0.85:
#     if lowest_grade >= 0.70:
#         print('You made the honour role!')

# if gpa >= 0.85 and lowest_grade >= 0.70:
#     print('You made the honour role!')

if gpa >= 0.85 and lowest_grade >= 0.70:
    honour = True
else:
    honour = False

if honour:
    print('You made the honour role!')
else:
    print('You have not made the honour role!')
